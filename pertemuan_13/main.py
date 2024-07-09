from class_exercase import Stack
stack = Stack()
stack.push(10)
stack.push(30)
stack.push(15)
stack.pops()
print(f'Data yang tertinggi: {stack.peek()}')
print(f'Cek Data Kosong: {stack.isMT()}')
stack.print()