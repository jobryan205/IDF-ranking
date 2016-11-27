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

class Race:
    def __init__(self, heats, racers):
        self.heats = []
        self.racers = racers
        self.heats = heats


    # def printRaceHeats(self):
    #     for heat in self.heats:
    #         print "HEAT:"
    #         for racer in heat:
    #             print "Racer id: " + str(racer.id) + ", score: " + str(racer.rating)

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