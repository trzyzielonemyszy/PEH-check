class Ingredient:
    def __init__(self, entry):
        self.name=entry[0]
        self.group=entry[1]
        print(f'Created ingredient: {self.name}')


