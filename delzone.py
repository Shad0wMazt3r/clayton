MAX_POPULATION  = 1000  # Maximum population of a zone
def readZones(ZoneName,operation):
    fileReader = open("Files/zone.txt", "r")
    ZoneList = []
    for line in fileReader:
        lineSplit = line.split(";")
        lineSplit[2] = lineSplit[2].replace("\n", "")
        if lineSplit[2] == ZoneName:
            ZoneList.append(line.replace("\n", ""))
    if operation == "num":
        return len(ZoneList)
    elif operation == "list":
        return ZoneList

def addSub(name, zip, zone):
    fileWriter = open("Files/zone.txt", "a")
    population = readZones(zone, "num")
    if population < MAX_POPULATION:
        fileWriter.write(name + ";" + zip + ";" + zone + "\n")
        return True
    else:
        zone = int(zone)
        zone += 1
        zone = str(zone)
        population = readZones(zone, "num")
        if population < MAX_POPULATION:
            fileWriter.write(name + ";" + zip + ";" + zone + "\n")
            return True
        else:
            zone = int(zone)
            zone -= 2
            zone = str(zone)
            population = readZones(zone, "num")
            if population < MAX_POPULATION:
                fileWriter.write(name + ";" + zip + ";" + zone + "\n")
                return True
            else:
                return False
print(addSub("hello", "50012", "1"))