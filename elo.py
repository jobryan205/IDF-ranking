from race import Race, Racer

SAMPLE_HEATS = [
    [0, 1, 2, 3],
    [4, 5, 6, 7],
    [0, 4, 2, 6],
    [1, 5, 3, 7]
]

def createHeatsByIds(heatsByIds, racers):
    heats = []
    for heatById in heatsByIds:
            heat = []
            for racerId in heatById:
                racer = next((r for r in racers if (r.id == racerId)))
                heat.append(racer)
            heats.append(heat)
    return heats

def createHeatsByNames(heatsByNames, racers):
    heats = []
    for heatById in heatsByIds:
            heat = []
            for racerId in heatById:
                racer = next((r for r in racers if (r.id == racerId)))
                heat.append(racer)
            heats.append(heat)
    return heats

racers = []
kieraFile = open('kiera.txt', 'r')
for i in range(0, 64):
    racerName = kiera.readline()
    racer = Racer(i, racerName)

kieraHeats = createHeatsByNames()

# racers = []
# for i in range(0, 8):
#     racer = Racer(i, "test")
#     racers.append(racer)

# heats = createHeatsByIds(SAMPLE_HEATS, racers)
# race = Race(heats, racers)
# race.initializeBeatersAndLosers()

for i in range(0, 10):
    race.computeScores()
    race.printRacers()
    print "\n"




