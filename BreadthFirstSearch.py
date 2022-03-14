#Austin Neumann Amnd7d
#Homework 3 4050
#BFS Algorithm

from itertools import count


def BFS(matrix, nodes, start):
    visited = [nodes]
    nextLayer = [start]
    currentLayer = []
    num = 0
    visited[start] = True
    while(nextLayer.count != 0):
        currentLayer = nextLayer
        nextLayer = []
        print(num)
        num += 1
        j = 0
        for i in range(currentLayer.count):
            node = currentLayer[i]
            print(node)
            while(j < nodes):
                if(matrix[node][j] == 1 and visited == False):
                    nextLayer.append(j)
                    visited[j] = True

while(True):

    #try:
    filename = input("Enter a file to be analyzed: ")
    f = open(filename, "r")
        #continue
    #except: Exception
    mergedList = []   
    for msg in f.readlines():   
        msg = msg.strip('\n') 
        adm = msg.split(' ') 
        mergedList.append(adm) 
    number = mergedList.count
    BFS(mergedList, number, mergedList[0][0])

    


    