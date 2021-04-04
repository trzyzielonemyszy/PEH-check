
class Product:
    def __init__(self, entry):
        self.name=entry[0]
        self.ingredients_raw=entry[1:]
        self.ingredients= set()
        print(f'Created product: {self.name}')

    def get_ingredients_raw(self):
        return(self.ingredients_raw)

    def add_ingredient(self,i):
        self.ingredients.add(i)

    def describe(self):
        ingredients_string=''
        for i in self.ingredients: ingredients_string=ingredients_string+i.describe()
        return f"Product: {self.name}, important ingredients: {ingredients_string}"




