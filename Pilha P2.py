class Pilha:
    def __init__(self):
        self.items = []

    def is_empty(self):
        """
        Verifica se a pilha ta vazia
        """
        return not bool(self.items)

    def push(self, item):
        """
        Insere um elemento no topo da pilha
        """
        self.items.append(item)

    def pop(self):
        """
        Remove o elemento do topo da pilha
        """
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        """
        Retorna o elemento no topo da pilha sem removê-lo
        """
        if not self.is_empty():
            return self.items[-1]

pilha = Pilha()
pilha.push(1)
pilha.push(2)
pilha.push(3)
print(pilha.peek())
print(pilha.pop())
print(pilha.peek())
print(pilha.pop())
print(pilha.is_empty())

'''
.   _____ _____ _   _ _  _____    _  _    ___  _  _   
.  |_   _| ____| \ | | |/ / _ \  | || |  / _ \| || |  
.    | | |  _| |  \| | ' / | | | | || |_| | | | || |_ 
.    | | | |___| |\  | . \ |_| | |__   _| |_| |__   _|
.    |_| |_____|_| \_|_|\_\___/     |_|  \___/   |_|  
                                                    
'''