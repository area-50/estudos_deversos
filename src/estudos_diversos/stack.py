class Stack:
    def __init__(self):
        self.__stack: list = []

    def push(self, item) -> None:
        self.__stack.append(item)
        print(f'Foram adicionados a pilha o item: {item!s}')

    def pop(self, item=None):
        if item is not None:
            try:
                print(f'Foram retirados da pilha o item: {item} {self.__stack.remove(item)}')
            except ValueError:
                print('Item não existe na pilha.')
        else:
            if len(self.__stack) > 0:
                print(f'Foram retirados da pilha o item: {self.__stack.pop()}')

    def __str__(self):
        return str(self.__stack.__str__())


class OperationOnStack:
    def __init__(self, stack: Stack) ->  None:
        self.stack = stack

    def increase_from_items(self, item=None) -> None:
        if items:
            stack.push(item)

    def decrease_from_stack(self, item=None) -> None:
        self.stack.pop(item)



class Display:
    def __init__(self, stack: Stack, items=None):
        self._stack = stack if stack is not None else None
        self._items = items if items is not None else []
        self._operational_comands = OperationOnStack(self._stack)

    def items(self) -> None:
        print(
            f'''
            Itens: {self._items}
            '''
        )

    def options(self) -> int:

        self.items()

        print('Entre esses itens: escolha uma opção abaixo para adiconar a pilha:\n')

        print("S: Sair")

        items_available: list = []

        for i, item in enumerate(self._items):
            payload = str(i), item
            items_available.append(payload)
            print(f'{i}: {item}')

        print('\n')
        print(f'Situação da pilha: {self._stack!s}')


        operation = ''
        while operation not in ['p', 'P', 'd', 'D']:
            operation = input('digite P para empilhar ou D para desempilhar: ')

        if operation in ['d', 'D']:
            self._operational_comands.decrease_from_stack()
        else:
            option = input('Digite uma opção: ')

            if option in 'Ss':
                return 1
            
            for item in items_available:
                if item[0] == option:
                    self._operational_comands.increase_from_items(item[1])

        return 0

    def run(self):
        flag: int = 0
        while not flag:
            flag = self.options()
        print('Programa encerrado.')


if __name__ == '__main__':
    items: list = ['banana', 'maça', 'uva', 'pêra', 'salada mista', 'Opala ss 6 caneco', 'Xicara']
    stack = Stack()
    diplay = Display(stack, items)

    diplay.run()