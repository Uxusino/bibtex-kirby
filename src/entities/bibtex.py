class Bibtex:
    #todo fiksaa nää
    def __init__(self, content: tuple):
        self.id = content[0]
        self.label = content[1]
        self.type = content[2]
        self.creation_time = content[3]
        self.modified_time = content[4]
        self.data = content[5]

    def __str__(self):
        return f"{self.id} {self.type}: {self.label}"
