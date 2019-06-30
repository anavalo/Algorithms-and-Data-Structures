
def kadanesAlgorithm(array):
    lidx = int(len(array)/2)
    ridx = int((len(array)/2)+1)
    while True:
        currentsum = (sum(array[lidx:ridx]))
        maxsum = sum(array)















ex1 = [3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4]

kadanesAlgorithm(ex1)