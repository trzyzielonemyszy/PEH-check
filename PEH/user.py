class User:
    def __init__(self, entry):
        self.name = entry[0]
        self.products = {}
        print(f'Created user: {self.name}')

    def add_product(self, product):
        self.product.add(product)
