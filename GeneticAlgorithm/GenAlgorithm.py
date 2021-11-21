from GeneticAlgorithm.GeneticAgent import GeneticAgent
from Maze import Node

from ImageLoader import ImageLoader
from ImageOptions import ImageOptions


class GenAlgorithm:
    def __init__(self, nodes):
        # The size of each generation - where geneticAgent[1] below is size (200).
        self._geneticAgent = GeneticAgent(int(len(nodes)), 200)
        self._nodes = nodes

    def name(self):
        return "Genetic Algorithm"

    def execute(self):
        # see if a child makes it to the end
        # run the genomes across the maze and get fitness function(method in genetic algorithm)
        generation = 0
        solution = None
        while (solution == None):
            print(f'Generation {generation}')
            generation += 1
            self._geneticAgent.walkThroughMaze(self._nodes, self._nodes[-1])
            solution = self._geneticAgent.completeGenome(self._nodes[-1])

            # Fitness and penalty logging only
            # for i in range(5):
            #     genome = self._geneticAgent.getGenome(i)
            #     print(f'    {i}: fitness:{genome.fitness()}', end="")
            #     genome.printInfo()

            self._geneticAgent.createNextGen()

            # Printing 5 in-progress solutions for improving algorithm
            # change the 20 in the following line to print out the peeks at different generation intervals. 20 means they print out every 20th generation.
            # if (generation % 20 == 0):
            #     imagedrawer = ImageLoader()
            #     options = ImageOptions()
            #     for i in range(5):
            #         genome = self._geneticAgent.getGenome(i)
            #         nodeList = self.convertToNodeList(self._nodes, genome)
            #         destinationFile = f'./Maps/Peek{i}.png'
            #         imagedrawer.saveWithNodeData(options.smallMaze, destinationFile, nodeList)

        # Something to turn a genome in to a list of nodes
        print('Found a solution')
        return self.convertToNodeList(self._nodes, solution)

    def convertToNodeList(self, nodes: [Node], solution):
        # converting the solution into a printable one for solution.png
        nodeList = []
        nodeList.append(nodes[0])
        currentNode = nodes[0]
        finalNode = nodes[-1]
        for direction in solution.getGenome():
            if (direction > 3):
                continue
            nextNode = currentNode.branches[direction]
            if (nextNode != None):
                nodeList.append(nextNode)
                currentNode = nextNode
                if finalNode.ycoord == currentNode.ycoord:
                    break
        return nodeList
