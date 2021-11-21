import time

from ImageOptions import ImageOptions
from ImageLoader import ImageLoader
from BreadthFirst import BreadthFirst
from DepthFirst import DepthFirst
from Dijkstra import Dijkstra
from AStar import AStar
from GeneticAlgorithm import GenAlgorithm


def printline(text):
    print(text)


# class Mazes:
def main():
    #	def __init__(self):

    options = ImageOptions()
    loader = ImageLoader()
    # Load the image as a usable graph

    # See ImageOptions for maze options. Return options. and the maze you want to use
    # !Caution advised when running 2k or 4k mazes, they take a LONG time
    maze = options.braid200Maze

    print(f"------------------------------------------- \nBuilding node graph for chosen Maze")
    t0 = time.time()
    data = loader.getImageData(maze)
    t1 = time.time()
    print(f"Time taken equals {t1 - t0} seconds")
    print(f'There are {len(data)} nodes in the Maze \n -------------------------------------------')

    print('Running the solving method')
    t0 = time.time()

    # Remove ONE # below to enable this as the search algorithm to be used in the solution
    #algorithm = Dijkstra(data)
    algorithm = AStar(data)
    #algorithm = BreadthFirst(data)
    #algorithm = DepthFirst(data)
    #algorithm = GenAlgorithm.GenAlgorithm(data)
    solution = algorithm.execute()
    t1 = time.time()

    print(f"Time taken equals {t1 - t0} seconds to solve using {algorithm.name()} search algorithm")
    print(f'Using {len(solution)} number of nodes in the solution \n -------------------------------------------')
    if t1 - t0 < 0.0004:
        print(
            f"Time recorded 0.0, time taken was < 0.00039 seconds\nCongratulations {algorithm.name()}, you're faster than python!\n -------------------------------------------")

    # for logging only:
    # for i in solution:
    # 	print(f'({i.coord.x},{i.coord.y})')
    # loader.saveWithPath(options.bigBoyMaze, options.solution, solution)
    loader.saveWithNodeData(maze, options.solution, solution)
    loader.saveWithNodes(options.solution, options.solution, solution)


main()
# see /Maps/solution.png for the maze with a solution drawn
