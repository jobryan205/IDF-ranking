from PyMongo import MongoClient

class Racer:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.rating = 400
        self.numMatches = 0
        self.beaters = []
        self.losers = []

    def printData(self):
        print "Racer id: " + str(self.id) + ", score: " + str(self.rating)
        print "Racer beaters: " + str([r.id for r in self.beaters]) 
        print "Racer losers: " + str([r.id for r in self.losers])

    def saveRacerToDb():
        

class Race:
    def __init__(self, heats, racers):
        self.heats = []
        self.racers = racers
        self.heats = heats

    def printRacers(self):
        racersByScore = sorted(self.racers, key=lambda r: r.rating, reverse=True)
        for racer in racersByScore:
            racer.printData()
            
    def initializeBeatersAndLosers(self):
        for heat in self.heats:
            for i, winner in enumerate(heat):
                for loser in heat[(i + 1):]:
                    winner.losers.append(loser)
                    winner.numMatches += 1
                    loser.beaters.append(winner)
                    loser.numMatches += 1

    def computeScores(self):
        for racer in self.racers:
            opponentsTotalRating = sum([r.rating for r in racer.beaters]) + sum([r.rating for r in racer.losers]) 
            winsMinusLosses = len(racer.losers) - len(racer.beaters)
            newRating = (opponentsTotalRating + 400 * winsMinusLosses) / racer.numMatches
            racer.newRating = newRating

        for racer in self.racers:
            racer.rating = racer.newRating


# ~~~DRIVER~~~

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

if __name__ == "__main__":




