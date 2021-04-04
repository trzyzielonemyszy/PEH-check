
class Product:
    def __init__(self, entry):
        self.name=entry[0]
        self.indgredients_raw=entry[1:]
        self.indgredients=set()
        print(f'Created product: {self.name}')

    def get_ingredients_raw(self):
        return(self.indgredients_raw)

    def add_ingredient(self,i):
        self.ingredients.add(i)




