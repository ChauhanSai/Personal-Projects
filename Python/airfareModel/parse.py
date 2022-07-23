IATA = {}

data = open("GlobalAirportDatabase.txt", "r")
file = data.readlines()
for line in file:
    line = line.strip().split(":")
    if line[5] != "000" and line[0][:1] in "ECKML":
        IATA[line[1]] = [float(line[14]), float(line[15])]
        print(IATA[line[1]])
data.close()

print(IATA)