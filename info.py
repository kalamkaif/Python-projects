import json
import os.path

class Register:
    dict = {}
    def __init__(self):
        self.load()
        self.view()

    def add(self, item, quantity):
        q = 0
        if item in self.dict:
            v = self.dict[item]
            q = v + quantity
        else:
            q = quantity
        self.dict[item] =q
        print(f'Item {item} of {quantity} quantity added')
        print(f'total {item}: {self.dict[item]}')

    def remove(self, item, quantity):
        if item not in self.dict:
            print(f'{item} not present')
            return
        q = 0
        if item in self.dict:
            v = self.dict[item]
            q = v - quantity
        if q>=0:
            self.dict[item] = q
            print(f'Item {item} of {quantity} quantity removed')
        else:
            print(f'Removing {quantity} is not possible')
        print(f'total {item}: {self.dict[item]}')

    def view(self):
        for item, value in self.dict.items():
            print(f'{item} : {value}')

    def save(self):
        with open('register.txt', 'w') as f:
            json.dump(self.dict, f)
        print('Saved')

    def load(self):
        if not os.path.exists('register.txt'):
            print('Nothing to load')
            return
        with open('register.txt', 'r') as f:
            self.dict = json.load(f)
        print('Register loaded Successfully')

def main():
    reg = Register()
    while True:
        print('*' * 30)
        operation = input('Operations:\nadd, remove, view, save, exit : ')
        if operation == 'exit':
            break
        if operation == 'add' or operation == 'remove':
            item = input('enter item name: ')
            qty = int(input('enter the quantity: '))
            if operation == 'add':
                reg.add(item, qty)
            if operation == 'remove':
                reg.remove(item, qty)

        if operation == 'view':
            reg.view()
        if operation == 'save':
            reg.view()
            reg.save()
    reg.save()

if __name__ == '__main__':
    main()