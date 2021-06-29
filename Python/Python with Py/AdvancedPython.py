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
