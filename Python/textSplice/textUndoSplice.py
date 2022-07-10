file = open("splice.txt")
print("Reading splice.txt")
file = file.readlines()
length = len(file)
if length % 2 != 0:
    length -= 1
print("Length:", length)

em = input("One file? True/False:: ")
if em == "True":
    fileA = open("a.txt", "w")
    i = 0
    while i < length:
        fileA.write(file[i].strip())
        fileA.write("\n")
        i += 2
    i = 1
    while i < length:
        fileA.write(file[i].strip())
        fileA.write("\n")
        i += 2
    fileA.close()

    print("Est. Length:", length + 1)
else:
    fileA = open("a.txt", "w")
    fileB = open("b.txt", "w")
    i = 0
    while i < length:
        fileA.write(file[i].strip())
        fileA.write("\n")
        fileB.write(file[i + 1].strip())
        fileB.write("\n")
        i += 2
    fileA.close()
    fileB.close()

    print("Est. Length:", round(length / 2) + 1)
