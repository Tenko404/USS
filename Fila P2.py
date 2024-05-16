class Fila:
    def __init__(self):
        self.items = []

    def is_empty(self):
        """
        Verifica se a fila ta vazia
        """
        return not bool(self.items)

    def enqueue(self, item):
        """
        Insere um elemento na frente da fila
        """
        self.items.insert(0, item)

    def dequeue(self):
        """
        Remove o elemento da frente da fila
        """
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        """
        Retorna o elemento na frente da fila sem removê-lo
        """
        if not self.is_empty():
            return self.items[0]

fila = Fila()
fila.enqueue(1)
fila.enqueue(2)
fila.enqueue(3)
print(fila.peek())
print(fila.dequeue())
print(fila.peek())
print(fila.dequeue())
print(fila.is_empty())

'''
.   _____ _____ _   _ _  _____    _  _    ___  _  _   
.  |_   _| ____| \ | | |/ / _ \  | || |  / _ \| || |  
.    | | |  _| |  \| | ' / | | | | || |_| | | | || |_ 
.    | | | |___| |\  | . \ |_| | |__   _| |_| |__   _|
.    |_| |_____|_| \_|_|\_\___/     |_|  \___/   |_|  
                                                    
'''