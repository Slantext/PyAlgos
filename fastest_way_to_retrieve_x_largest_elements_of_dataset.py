import heapq

x = input("Number of largest elements: ")   # How many of the largest elements we want to retreive
dataset = input("Input dataset: ")          # Takes in a set of n elements

heapq.nlargest(x, dataset)      # retieves the x largest elements in dataset
