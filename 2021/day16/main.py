# One hell of a problem (implementation)
def p1():
    # could probably do this more concise but idk
    hex_map = {
        "0": "0000",
        "1": "0001",
        "2": "0010",
        "3": "0011",
        "4": "0100",
        "5": "0101",
        "6": "0110",
        "7": "0111",
        "8": "1000",
        "9": "1001",
        "A": "1010",
        "B": "1011",
        "C": "1100",
        "D": "1101",
        "E": "1110",
        "F": "1111",

    }

    with open("input.txt") as f:
        packet = "".join([hex_map[c] for c in f.read().strip()])



    def get_num(idx):
        """ idx: start of num """
        """ returns num, end of num """
        n_str = ""
        while True:
            n_str += packet[idx+1:idx+5]
            idx += 5

            if packet[idx-5] == '0':
                break

        return int(n_str,2), idx 

    #print(packet)
    
    def version_sum(idx):
        """ idx: start of packet """
        """ returns v_sum, next_idx"""

        v_no = int(packet[idx:idx+3],2)
        idx += 3
        t_id = packet[idx:idx+3]
        idx += 3

        if t_id == '100':
            #print(f"Unpack literal packet, starting at col: {idx-6+1}")
            
            num, idx = get_num(idx)
            #print(f"Literal contained {num=}")
            return v_no, idx 
        else:
            t_type = packet[idx]
            idx += 1

            if t_type == '0':
                #print(f"Unpack length-based packet, starting at col: {idx-7+1}")
                sub_len = int(packet[idx:idx+15], 2)
                #print(f"Length = {sub_len}")
                idx += 15

                v_sum = v_no 
                len_cnt = 0
                while len_cnt < sub_len:
                    sub_v_sum, next_idx = version_sum(idx)

                    v_sum += sub_v_sum
                    len_cnt += next_idx - idx
                    idx = next_idx
                return v_sum, idx
            else:
                #print(f"Unpack count-based packet, starting at col: {idx-7+1}")
                sub_cnt = int(packet[idx:idx+11], 2)
                idx += 11

                v_sum = v_no
                num_cnt = 0

                while num_cnt < sub_cnt:
                    sub_v_sum, next_idx = version_sum(idx)
                    v_sum += sub_v_sum
                    num_cnt += 1
                    idx = next_idx
                return v_sum, idx

    v_sum, _ = version_sum(0)
    print(v_sum)

def p2():
    # mapping from hex digit to 4-digit binary number
    # could probably do this more concise but idk
    hex_map = {
        "0": "0000",
        "1": "0001",
        "2": "0010",
        "3": "0011",
        "4": "0100",
        "5": "0101",
        "6": "0110",
        "7": "0111",
        "8": "1000",
        "9": "1001",
        "A": "1010",
        "B": "1011",
        "C": "1100",
        "D": "1101",
        "E": "1110",
        "F": "1111",

    }

    with open("input.txt") as f:
        # read file and translate to binary in one swoop
        # binary number written as string (indexing and leading zeros all good)
        packet = "".join([hex_map[c] for c in f.read().strip()])



    # function to read a number from a literal-packet
    # idx should point to first index of number bits
    def get_num(idx):
        """ idx: start of num """
        """ returns num, end of num """
        # string to store result
        n_str = ""
        # we loop until we encounter a 5er starting with a '0'
        # the last 5er should also be included, hence the while True
        while True:
            # simply append the bits
            n_str += packet[idx+1:idx+5]
            idx += 5

            # this was last
            if packet[idx-5] == '0':
                break

        # convert to int using base-2
        # also, we return first index AFTER the literal-packet
        return int(n_str,2), idx 

    
    # function to evaluate a packet
    # returns evaluated number and first index after packet
    # idx should point to first bit in packet
    # expects packet header and correct format
    def parse(idx):
        """ idx: start of packet """
        """ returns packet value, next_idx"""

        # parse version number as base-2-int
        # not necessary for problem 2
        v_no = int(packet[idx:idx+3],2)

        # always increase idx after chop so we can retu
        idx += 3
        t_id = packet[idx:idx+3]
        idx += 3

        # t_id = 4 means packet is a literal-packet
        if t_id == '100':
            #print(f"Unpack literal packet, starting at col: {idx-6+1}")
            
            num, idx = get_num(idx)
            #print(f"Literal contained {num=}")

            # idx is now next idx after packet
            return num, idx 
        else:
            # two types: length based and count based
            t_type = packet[idx]
            idx += 1

            # stores integers after evaluation of sub-packets
            sub_values = []

            if t_type == '0':
                #print(f"Unpack length-based packet, starting at col: {idx-7+1}")

                # length-based packet. should parse until a specific number of bits have been parsed
                # first read this specific number (15 bits)
                sub_len = int(packet[idx:idx+15], 2)
                #print(f"Length = {sub_len}")
                idx += 15

                # len_cnt represent total number of bits parsed
                len_cnt = 0
                while len_cnt < sub_len:
                    # sub_v should now be an integer representing the value of recursively evaluated sub-packet
                    # this is why we needed to return index after each packet because we may not know total length up front
                    sub_v, next_idx = parse(idx)

                    sub_values.append(sub_v)

                    # add number of bits parsed to running total
                    len_cnt += next_idx - idx
                    idx = next_idx
            else:
                #print(f"Unpack count-based packet, starting at col: {idx-7+1}")

                # count-based packet. should parse until a specific number of sub-packets have been parsed 
                # (not counting sub-sub packets and so on)
                # first, read number of packets (11 bits)
                sub_cnt = int(packet[idx:idx+11], 2)
                idx += 11

                # num_cnt represents running total number of packets parsed
                num_cnt = 0

                while num_cnt < sub_cnt:
                    # recursively evaluate sub-packet
                    sub_v, next_idx = parse(idx)

                    sub_values.append(sub_v)
                    num_cnt += 1
                    idx = next_idx

            # apply correct function so sub-packet-values based on type id
            if   t_id == '000':
                ret_val = sum(sub_values)
            elif t_id == '001':
                ret_val = 1 
                for val in sub_values:
                    ret_val *= val
            elif t_id == '010':
                ret_val = min(sub_values)
            elif t_id == '011':
                ret_val = max(sub_values)
            elif t_id == '101':
                ret_val = 1 if sub_values[0] > sub_values[1] else 0
            elif t_id == '110':
                ret_val = 1 if sub_values[0] < sub_values[1] else 0
            elif t_id == '111':
                ret_val = 1 if sub_values[0] == sub_values[1] else 0
            else:
                assert False, "Exhaustive type id handling. Error in file parsing"

            return ret_val, idx

    ans, _ = parse(0)
    print(ans)

p2()
