def numbers():
    yield 1
    yield 2
    yield 3

for n in numbers():
    print(n)

print('-------------------------')
    
print(numbers())
print(numbers())
print(numbers())
print(numbers())