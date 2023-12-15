text = open("list.txt", "r").read().replace("\t", " ")
text = text.split("\n")

count = 0
while count < len(text):
    if text[count].index(":") == 1:
        text[count] = "0" + text[count]
    text[count] = text[count] + " " + text.pop(count + 1) + " " + text.pop(count + 1) + " " + text.pop(count + 1)
    count += 1

text.sort()
for i in text:
    print(i)
