import sys

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Use arguments.")
        exit(1)

    fn_in = sys.argv[1]
    fn_out = sys.argv[2]

    with open(fn_in) as file_in:
        lines = file_in.readlines()

    adj = {}
    index = {}

    ptr = 0
    for line in lines:
        a, b = line.strip().split("-")

        if a in adj:
            adj[a].add(b)
        else:
            adj[a] = set([b])
            index[a] = ptr
            ptr += 1
        if b in adj:
            adj[b].add(a)
        else:
            adj[b] = set([a])
            index[b] = ptr
            ptr += 1

    n = len(adj)

    m = sum([len(adj[el]) for el in adj])

    lowers = [index[s] for s in adj if s == s.lower() and s != "start" and s != "end"]
    print(lowers)

    s = index["start"]
    e = index["end"]

    with open(fn_out, "w") as file_out:
        file_out.write(f"{n} {m} {len(lowers)}\n")
        file_out.write(f"{s} {e}\n")
        file_out.write(" ".join([str(n) for n in lowers]))
        file_out.write("\n")

        for a in adj:
            for b in adj[a]:
                file_out.write(f"{index[a]} {index[b]}\n")
