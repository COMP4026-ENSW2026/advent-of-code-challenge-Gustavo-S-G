

class SimpleCPU:
    def __init__(self) -> None:
        self.register_X = 1
        self.cycle = 1
        self.waiting_add = 0
        self.wait = -1
        self.sum_of_registers = 0
        self.display = ""

    def run_command(self, command):
        if 'addx' in command:
            add_nr = int(command.split(' ')[1])
            self.wait = 2
            self.waiting_add = add_nr

    def advance_cycle(self):
        if self.cycle in [20, 60, 100, 140, 180, 220]:
            self.sum_of_registers += self.cycle * self.register_X
        self.cycle += 1
        self.wait -= 1
        if self.wait == 0:
            self.register_X += self.waiting_add

    def print_cpu_state(self, part):
        if part == 1:
            if self.cycle in [20, 60, 100, 140, 180, 220]:
                print(f"Completed cycles: {self.cycle}, register: {self.register_X}")
                if self.wait > 0:
                    print(f"waiting add: {self.waiting_add} in {self.wait} cycles")
                print('-----')
        else:
            sprite = [self.register_X - 1, self.register_X, self.register_X + 1]
            if (self.cycle-1) % 40 in sprite:
                self.display += "O"
            else:
                self.display += "_"
            if len(self.display) == 40:
                print(self.display)
                self.display = "" 

def solve(file, part=1):
    with open(file, 'r') as f:
        lines = f.readlines()
        lines = [entry.strip() for entry in lines]

    cpu = SimpleCPU()

    while len(lines) > 0 or cpu.wait > 0:
        if cpu.wait > 0:
            pass
        else:
            line = lines.pop(0)
            cpu.run_command(line)
        cpu.print_cpu_state(part=part)
        cpu.advance_cycle()
    if part == 1:
        print('sum of signal strenghts', cpu.sum_of_registers)

solve('sample.in', part=1)