numbers = [1,2,3]
print(sum(numbers))

for i in range(1,11):
    print(i)

string = ""
for i in range(1,6):
    string += str(i)
print(string)

operators = ['+', '-', '*', '/']
operators_dict = {}
for i in range(len(operators)):
    operators_dict[i] = operators[i]
print(operators_dict)

print(int(4.6))
print(round(4.6))

indexing = "hello"
print(indexing[0])
print(indexing[-1]+indexing[-2])
print(indexing[1:-1])
print(indexing[1:])
print(indexing[:2])

strings = ["hello", "hi"]
print(strings[0][2])

def sys():
    print("Apples")
    print("Bananas")
sys()

def nothing():
    pass
nothing()

hot = True
print(hot)
def cold():
    hot = False
    print(hot)
cold()
print(str(hot)+"(Doesn't change out of function")

def value():
    value = 1+2
    return value
print(value())
