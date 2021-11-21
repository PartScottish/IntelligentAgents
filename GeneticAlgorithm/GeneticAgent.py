from numpy import random
import numpy

from GeneticAlgorithm.Genome import Genome
from Maze import Node

class GeneticAgent:
    def __init__(self, genomeLength, populationSize):
        self._genomeLength = genomeLength
        self._popSize = populationSize
        self._fitChildrenNum = 4
        self._mutationNum = 4
        self._population = [None]*populationSize
        #random.seed(3)
        for i in range(populationSize):
            genome = random.randint(4, size=genomeLength).tolist()
            self._population[i] = Genome(genome)

    def createNextGen(self):
        #sortedPopulation to allow for selected first and last with highest and lowest fitness respectively
        sortedPopulation = sorted(self._population, key=lambda g: g.fitness())
        breedingPopulation = sortedPopulation[0:(-1*( self._fitChildrenNum))]
        newPopulation = [None]*self._popSize

        for i in range(self._fitChildrenNum):
            newPopulation[i] = Genome(sortedPopulation[i].getGenome())
        for i in range( self._fitChildrenNum, self._popSize):
            newPopulation[i] = self.crossBreed(breedingPopulation)

        self._population = newPopulation
        self.mutate()

    def walkThroughMaze(self, nodes: [Node], finalNode :Node):
        visitedNodes = []
        for genome in self._population:
            currentNode: Node = nodes[0]
            for direction in genome.getGenome():
                nextNode = currentNode.branches[direction]
                if (nextNode == None):
                    genome.punish()
                else:
                    if (visitedNodes.__contains__(nextNode)):
                        genome.punish()
                    else:
                        visitedNodes.append(nextNode)
                    currentNode = nextNode
                    if finalNode.ycoord == currentNode.ycoord:
                        genome.setComplete()
                        break
            genome.fitnessFunction(finalNode, currentNode)
            #genome.fitnessFunctionCheat(finalNode, currentNode, nodes)

    def getGenome(self, position):
        return self._population[position]

    def completeGenome(self, finalNode: Node):
        for genome in self._population:
            if (genome.isComplete()):
                return genome
        return None

    def crossBreed(self, breedingPopulation: [Genome]):
        genome1 = breedingPopulation[random.randint(self._popSize - self._fitChildrenNum)].getGenome()
        genome2 = breedingPopulation[random.randint(self._popSize - self._fitChildrenNum)].getGenome()

        split = random.randint(len(genome1))

        part1 = genome1[:split]
        part2 = genome2[split:]
        addedArray = part1 + part2
        return Genome(addedArray)

    def mutate(self):
        for x in range(self._mutationNum, self._popSize):
            genome = self._population[x]
            for i in range(self._genomeLength):
                mutationChance = random.randint(100)
                if (mutationChance > 50):
                    genome.mutateGene(i, random.randint(4))

