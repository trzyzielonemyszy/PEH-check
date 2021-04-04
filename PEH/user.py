class User:
    def __init__(self, name='Anonymous'):
        self.name = name
        self.products = {}
        print(f'Created user: {self.name}')

    def add_product(self, product):
        self.product.add(product)
