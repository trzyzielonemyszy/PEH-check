from PEH.user import User
from PEH.product import Product
from PEH.ingredient import Ingredient
from pathlib import Path
import csv

def read_file(self,source_file,obj):
    """
    :param self:
    :param source_file: string, source file name
    :param obj: object type
    :return: dict: dictionary of each object with its name as key
    """
    base_path = Path(__file__).parent
    file_path = (base_path / f"../data/{source_file}.csv").resolve()
    # with open(file_path) as f:
    #    test = [line for line in csv.reader(f)]
    object_list = {}
    with open(file_path, newline='') as source:
        csv_reader = csv.reader(source, delimiter=',')
        for row in csv_reader:
            object_list[row[0]]=obj(row)
    return object_list

class Db:
    def __init__(self):
        self.users = read_file(self,'users',User)
        self.products = read_file(self,'products',Product)
        self.ingredients = read_file(self,'ingredients',Ingredient)

    def check_ingredients(self):
        for (k,v) in self.products.items():
            print(k)
            for i in v.get_ingredients_raw():
                i_fix=i.lstrip()
                if i_fix in self.ingredients:
                    v.add_ingredient(self.ingredients[i_fix])
                else:
                    print(f'Unrecognized ingredient: {i_fix}')

    def report(self):
        print('REPORTING PRODUCTS:')
        for p in self.products.values():
            print(p.describe())





