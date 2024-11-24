class Bibtex:
    def __init__(self, content: tuple):
        self.id = content[0]
        self.label = content[1]
        self.type = content[2]
        self.creation_time = content[3]
        self.modified_time = content[4]
        self.data = content[5]

    def __str__(self):
        starting_string = f"@{self.type}{{{self.label},\n"
        for k, v in self.data.items():
            next_line = f"    {k} = {{{v}}},\n"
            starting_string = starting_string + next_line
        starting_string = starting_string[:-2]
        starting_string = starting_string + "\n}"
        return starting_string
