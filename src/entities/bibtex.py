class Bibtex:
    #todo fiksaa nää
    def __init__(self, id, content):
        self.id = id
        self.content = content

    def __str__(self):
        return f"{self.content}"
