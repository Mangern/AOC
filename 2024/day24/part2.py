from math import exp
from sys import stdin
import random
from tqdm import tqdm
class Gate:
    def __init__(self, name: str):
        self.value = -1
        self.name = name

    def func(self, input_1: int, input_2: int) -> int:
        raise NotImplementedError

    def apply(self, input_1: int, input_2: int):
        self.value = self.func(input_1, input_2)

    def reset(self):
        self.value = -1

    def has_value(self):
        return self.value != -1

    def get_value(self):
        assert self.has_value
        return self.value

class XOR(Gate):
    def func(self, input_1: int, input_2: int) -> int:
        return input_1 ^ input_2

class AND(Gate):
    def func(self, input_1: int, input_2: int) -> int:
        return input_1 & input_2

class OR(Gate):
    def func(self, input_1: int, input_2: int) -> int:
        return input_1 | input_2

class Circuit:
    def __init__(self, bits_in: int, bits_out: int):
        self.graph: dict[str, tuple[str,str]] = {}
        self.inputs: tuple[list[int], list[int]] = (
            [0] * bits_in,
            [0] * bits_in
        )
        self.input_xs = [f"x{i:02d}" for i in range(bits_in)]
        self.input_ys = [f"y{i:02d}" for i in range(bits_in)]
        self.output_zs = [f"z{i:02d}" for i in range(bits_out)]
        self.outputs: list[int] = [0] * bits_out
        self.gates: dict[str, Gate] = {}
        self.swappable: dict[str, set[str]] = {}
        self.hadwrong: set[str] = set()

    def add_gate(self, input_gate_1: str, input_gate_2: str, output_gate: str, function: str):
        assert function in ["XOR", "AND", "OR"]
        gate_type = XOR if function == "XOR" else (AND if function == "AND" else OR)
        if input_gate_1 > input_gate_2:
            input_gate_1, input_gate_2 = input_gate_2, input_gate_1
        self.graph[output_gate] = (input_gate_1, input_gate_2)
        self.gates[output_gate] = gate_type(output_gate)

    def swap_gates(self, gate_1: str, gate_2: str):
        inp1 = self.graph[gate_1]
        g1 = self.gates[gate_1]
        self.graph[gate_1] = self.graph[gate_2]
        self.gates[gate_1] = self.gates[gate_2]

        self.graph[gate_2] = inp1
        self.gates[gate_2] = g1

    def set_inputs(self, x_vals: list[int], y_vals: list[int]):
        assert len(x_vals) == len(self.inputs[0]), "Invalid input length for x_vals"
        assert len(y_vals) == len(self.inputs[1]), "Invalid input length for y_vals"
        self.inputs = ([x for x in x_vals], [y for y in y_vals])

        for gate in self.gates.values():
            gate.reset()

    def get_input_value(self, input_name: str) -> int:
        if input_name in self.input_xs:
            return self.inputs[0][self.input_xs.index(input_name)]
        elif input_name in self.input_ys:
            return self.inputs[1][self.input_ys.index(input_name)]
        else:
            assert False, f"Unknown gate {input_name}"
    
    def get_gate_value(self, gate_name: str) -> int:
        if gate_name not in self.gates:
            return self.get_input_value(gate_name)

        gate = self.gates[gate_name]
        if gate.has_value():
            return gate.get_value()

        input_1, input_2 = self.graph[gate_name]
        gate.apply(self.get_gate_value(input_1), self.get_gate_value(input_2))
        assert gate.has_value()
        return gate.get_value()


    def get_outputs(self) -> list[int]:
        return [self.get_gate_value(z) for z in self.output_zs]

    def init_swappable(self):
        for gate in self.gates:
            self.swappable[gate] = {g for g in self.gates if g != gate}

    def expect_gate(self, gate_name: str, expected_val: int, should0: set[str], should1: set[str]):
        if gate_name not in self.gates:
            #return self.get_input_value(gate_name) == expected_val
            return

        gate = self.gates[gate_name]
        if gate.get_value() == expected_val:
            return 

        if expected_val == 0:
            should0.add(gate_name)
        else:
            should1.add(gate_name)

        input_1, input_2 = self.graph[gate_name]
        self.hadwrong.add(gate_name)

        if type(gate) == AND:
            if expected_val == 0:
                self.expect_gate(input_1, 0, should0, should1)
                self.expect_gate(input_2, 0, should0, should1)
            else:
                self.expect_gate(input_1, 1, should0, should1)
                self.expect_gate(input_2, 1, should0, should1)
        elif type(gate) == OR:
            if expected_val == 0:
                self.expect_gate(input_1, 0, should0, should1)
                self.expect_gate(input_2, 0, should0, should1)
            else:
                self.expect_gate(input_1, 1, should0, should1)
                self.expect_gate(input_2, 1, should0, should1)
        elif type(gate) == XOR:
            if expected_val == 0:
                self.expect_gate(input_1, self.get_gate_value(input_2), should0, should1)
                self.expect_gate(input_2, self.get_gate_value(input_1), should0, should1)
            else:
                self.expect_gate(input_1, 1 ^ self.get_gate_value(input_2), should0, should1)
                self.expect_gate(input_2, 1 ^ self.get_gate_value(input_1), should0, should1)
        else:
            assert False, f"Unknown gate type {type(gate)}"

    def expect_output(self, expected_output: list[int]):
        assert len(expected_output) == len(self.output_zs)
        self.get_outputs()
        should0: set[str] = set()
        should1: set[str] = set()

        for out_name, expected_val in zip(self.output_zs, expected_output):
            self.expect_gate(out_name, expected_val, should0, should1)

        was0 = {g for g in self.gates if self.gates[g].get_value() == 0}
        was1 = {g for g in self.gates if self.gates[g].get_value() == 1}

        for gate_name in should0:
            #self.swappable[gate_name] &= was0
            #self.swappable[gate_name] -= was1
            cur = [x for x in self.swappable[gate_name]]
            for g in cur:
                if g not in was0:
                    self.swappable[gate_name].remove(g)
                    self.swappable[g].remove(gate_name)
            for g in was1:
                if g in self.swappable[gate_name]:
                    self.swappable[gate_name].remove(g)
                    self.swappable[g].remove(gate_name)
        for gate_name in should1:
            #self.swappable[gate_name] &= was1
            #self.swappable[gate_name] -= was0
            cur = [x for x in self.swappable[gate_name]]
            for g in cur:
                if g not in was1:
                    self.swappable[gate_name].remove(g)
                    self.swappable[g].remove(gate_name)
            for g in was0:
                if g in self.swappable[gate_name]:
                    self.swappable[gate_name].remove(g)
                    self.swappable[g].remove(gate_name)

def circuit_from_input(lines: list[str]) -> tuple[Circuit, list[int], list[int]]:
    init_lines = [line for line in lines if ":" in line]
    rules = [line.split() for line in lines if "->" in line]
    xs = {x.strip(): int(v.strip()) for x, v in [line.split(":") for line in init_lines if line[0] == 'x']}
    ys = {x.strip(): int(v.strip()) for x, v in [line.split(":") for line in init_lines if line[0] == 'y']}
    assert len(xs) == len(ys)
    num_inputs = len(xs)
    num_outputs = len([rule for rule in rules if rule[-1].startswith('z')])
    circuit = Circuit(num_inputs, num_outputs)

    for input_1, op, input_2, _, output in rules:
        circuit.add_gate(input_1, input_2, output, op)

    init_x = [v for k,v in sorted(xs.items())]
    init_y = [v for k,v in sorted(ys.items())]
    circuit.init_swappable()
    return (circuit, init_x, init_y)

def tobits(x: int, l: int) -> list[int]:
    bits = []
    while x:
        bits.append(x & 1)
        x >>= 1
    while len(bits) < l:
        bits.append(0)
    assert len(bits) == l, f"Invalid tobits: {x}" 
    return bits

def frombits(x: list[int]) -> int:
    return int("".join(map(str, x))[::-1], 2)

def old():
    inp = [line for line in stdin]
    circuit, init_x, init_y = circuit_from_input(inp)
    n_in = len(init_x)
    n_out = len(circuit.outputs)
    for _ in tqdm(range(50000)):
        x, y = random.randint(0, (1<<n_in)-1), random.randint(0, (1<<n_in)-1)
        circuit.set_inputs(tobits(x, n_in), tobits(y, n_in))
        expected = x + y
        circuit.expect_output(tobits(expected, n_out))

    interesting = []
    for k, v in circuit.swappable.items():
        #print(k, v)
        if len(v) < len(circuit.graph) and k in circuit.hadwrong:
            interesting.append(k)
    print(interesting)
    print(circuit.hadwrong)

if __name__ == "__main__":
    # circuit: Circuit = circuit_from_input
    # while num_candidates :
    #   draw x, y randomly
    #   circuit.set_inputs(bits(x), bits(y))
    #   z = int(circuit.get_outputs())
    #   expected = x + y (or x & y)
    #   circuit.update_candidates(expected)
    inp = [line for line in stdin]
    circuit, init_x, init_y = circuit_from_input(inp)

    SWAP_ANS = []

    def check(tup):
        return tup[0][0] == 'x' and tup[1][0] == 'y'

    while True:
        initial_xors = [g for g in circuit.gates if type(circuit.gates[g]) == XOR and check(circuit.graph[g])]
        initial_ands = [g for g in circuit.gates if type(circuit.gates[g]) == AND and check(circuit.graph[g])]

        carrys = [g for g in initial_ands if circuit.graph[g] == ("x00", "y00")]
        initial_xors.sort(key=lambda g: circuit.graph[g])
        next_xors = [None]
        next_ands = [None]
        wrong_fst_xors = []
        for xor in initial_xors[1:]:
            l = [g for g in circuit.gates if type(circuit.gates[g]) == XOR and xor in circuit.graph[g]]
            if len(l) == 0:
                wrong_fst_xors.append(xor)
                next_xors.append(None)
            else:
                assert len(l) == 1
                next_xors.append(l[0])

            l = [g for g in circuit.gates if type(circuit.gates[g]) == AND and xor in circuit.graph[g]]
            if len(l) == 0:
                next_ands.append(None)
            else:
                assert len(l) == 1
                next_ands.append(l[0])

        missing_xor = [g for g in circuit.gates if type(circuit.gates[g]) == XOR and g not in initial_xors and g not in next_xors]
        missing_and = [g for g in circuit.gates if type(circuit.gates[g]) == AND and g not in initial_ands and g not in next_ands]

        wrong_zs = [g for g in initial_ands if g in circuit.output_zs]
        if len(wrong_zs):
            wrong_z = wrong_zs[0]
            idx = int(wrong_z[1:])
            swap = next_xors[idx]

            print("Swapping", wrong_z, swap)
            circuit.swap_gates(wrong_z, swap)
            SWAP_ANS.append(wrong_z)
            SWAP_ANS.append(swap)
            continue

        wrong_zs = [i for i,g in enumerate(next_xors) if g is not None and g[0] != 'z']
        if len(wrong_zs):
            idx = wrong_zs[0]
            wrong_z = f"z{idx:02d}"
            swap = next_xors[idx]
            print("Swapping", wrong_z, swap)
            circuit.swap_gates(wrong_z, swap)
            SWAP_ANS.append(wrong_z)
            SWAP_ANS.append(swap)
            continue

        if len(wrong_fst_xors):
            # Very manual
            SWAP_ANS.append("wkr")
            SWAP_ANS.append("nvr")
            print("Swapping wkr, nvr")
            circuit.swap_gates("wkr", "nvr")
            continue
        else:
            print('Done!')
        break
    print(",".join(sorted(SWAP_ANS)))
