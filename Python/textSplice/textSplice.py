em = input("One file? True/False:: ")
if em == "True":
    file = open("a.txt")
    print("Reading a.txt")
    fileA = file.readlines()
    length = len(fileA)
    if length % 2 != 0:
        length -= 1
    length = round(length/2)
    print("Length:", length)

    file = open("splice.txt", "w")
    for i in range(length):
        file.write(fileA[i].strip())
        file.write("\n")
        file.write(fileA[i + length].strip())
        file.write("\n")
    file.close()

    print("Est. Length:", length * 2 + 1)
else:
    file = open("a.txt")
    print("Reading a.txt")
    fileA = file.readlines()
    print("Length:", len(fileA))
    file = open("b.txt")
    print("Reading b.txt")
    fileB = file.readlines()
    print("Length:", len(fileB))

    file = open("splice.txt", "w")
    for i in range(min(len(fileA), len(fileB))):
        file.write(fileA[i].strip())
        file.write("\n")
        file.write(fileB[i].strip())
        file.write("\n")
    file.close()

    print("Est. Length:", min(len(fileA), len(fileB)) * 2 + 1)
