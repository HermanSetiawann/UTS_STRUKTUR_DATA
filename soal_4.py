class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

# Contoh penggunaan
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print("Isi tumpukan:", stack.items)
print("Ukuran tumpukan:", stack.size())
print("Elemen teratas tumpukan:", stack.peek())
print("Mengeluarkan elemen teratas:", stack.pop())
print("Isi tumpukan setelah pop:", stack.items)
