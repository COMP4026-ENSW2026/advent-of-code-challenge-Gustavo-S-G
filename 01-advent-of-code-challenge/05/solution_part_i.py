

with open('sample.in', 'r') as f:
    linhas = f.readlines()
    linhas = [entry for entry in linhas]
linhas


class Pilha_caixas:
    def __init__(self) -> None:
        self.content = []

    def add_item_on_top(self, item):
        self.content.append(item)

    def take_x_crates(self, x, mover_varias):
        caixas_retornadas = self.content[-x:]
        self.content = self.content[:-x]
        if mover_varias:
            return caixas_retornadas
        else:
            return reversed(caixas_retornadas)
    
    def add_crates(self, novas_caixas):
        self.content += novas_caixas

    def get_top_content(self):
        return self.content[-1] if len(self.content) > 0 else ""

class CargoBay:
    def __init__(self, num_caixas):
        self.num_caixas = num_caixas
        self.crates = [Pilha_caixas() for _ in range(num_caixas)]

    def add_items_to_crates(self, items):
        for crate, item in zip(self.crates, items):
            if item != ' ':
                crate.add_item_on_top(item)

    def move_items(self, amount, source, target, mover_varias):
        moving_crates = self.crates[source].take_x_crates(amount, mover_varias)
        self.crates[target].add_crates(moving_crates)

    def get_top_stacks(self):
        return_message = ""
        for crate in self.crates:
            return_message += crate.get_top_content()
        return return_message

    def print_crates(self):
        for crate in self.crates:
            print(crate.content)
        print('-----')

def solve(file_name, part_2=False, print_crates=False):
    with open(file_name, 'r') as f:
        linhas = f.readlines()
        linhas = [entry for entry in linhas]

    num_caixas = len(linhas[0])//4
    cargo_bay = CargoBay(num_caixas)

    # everything before the empty line (minus the ' 1   2   3...' line are crate linhas)
    crate_lines = linhas[:linhas.index('\n')-1]
    # iterate over the crates from the bottom to the top
    for line in reversed(crate_lines):
        items = list(line)[1:-1:4]
        cargo_bay.add_items_to_crates(items)
    
    # everything after the empty line are moving linhas
    moving_lines = linhas[linhas.index('\n')+1:]
    for line in moving_lines:
        if print_crates:
            cargo_bay.print_crates()
        amount, source, target = [int(entry) for entry in line.strip().split(' ') if entry.isdigit()]
        cargo_bay.move_items(amount, source-1, target-1, part_2)
    
    print(cargo_bay.get_top_stacks())

solve('sample.in', part_2=False, print_crates=True)