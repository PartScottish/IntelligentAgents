class Genome:
    def __init__(self, genomeArray):
        self._genomeArray = genomeArray
        self._fitness = 0
        self._penalty = 0
        self._isComplete = False

    def fitnessFunction(self, finishingNode, deathNode):
        self._fitness = abs(finishingNode.xcoord - deathNode.xcoord) + abs(finishingNode.ycoord - deathNode.ycoord) + self._penalty
        # TODO: Add penalty to non-novel moves


    def fitness(self):
        return self._fitness

    def punish(self):
        self._penalty += 1

    def setComplete(self):
        self._isComplete = True

    def isComplete(self):
        return self._isComplete

    def getGenome(self):
        return self._genomeArray

    def mutateGene(self, position, value):
        self._genomeArray[position] = value

    #This is for logging only
    def printInfo(self):
        print(f' Penalty:{self._penalty}')


