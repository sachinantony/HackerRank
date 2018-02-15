def  solve_minesweeper(puzzle_array):
    n = len(puzzle_array)
    resultMat = [[0 for i in range(n)] for j in range(n)]
    adjacentList = []
    belowList = []
    rightList = []
    oddRowList = []
    cornerList = []
    mineList = []
    oddList = []
    for j in range(n):    
        for i in range(n):
            if(puzzle_array[j][i] == 'm'):  
                mineList.append([j,i])
                if j%2 == 1:
                    oddList.append(j)                    
                
                #top left diagonal 
                if i-1 >= 0 and j-1 >= 0:
					if [j-1,i-1] not in cornerList:
						cornerList.append([j-1,i-1])
                    resultMat[j-1][i-1] += 1
                #top right diagonal 
                if i+1 < n and j-1 >= 0:
					if [j-1,i+1] not in cornerList:
						cornerList.append([j-1,i+1])
                    resultMat[j-1][i+1] += 1
                #bottom left diagonal 
                if i-1 >= 0 and j+1 < n:
					if [j+1,i-1] not in cornerList:
						cornerList.append([j+1,i-1])
                    resultMat[j+1][i-1] += 1
                #bottom right diagonal 
                if i+1 < n and j+1 < n:
					if [j+1,i+1] not in cornerList:
						cornerList.append([j+1,i+1])
                    resultMat[j+1][i+1] += 1
                    
                #below     
                if j+1 < n:
                    resultMat[j+1][i] += 1
                    belowList.append([j+1,i])
                    
                #top
                if j-1 >= 0:
                    resultMat[j-1][i] += 1
                    
                #left
                if i-1 >=0:
                    resultMat[j][i-1] += 1
                
                #right
                if i+1 < n:
                    resultMat[j][i+1] += 1
                    rightList.append([j,i+1])
					
    for j,i in belowList:
        resultMat[j][i] = 2
		
    for j,i in rightList:
        resultMat[j][i] = 0
		
    for j in oddList:
        for i in range(n):
            resultMat[j][i] = resultMat[j][i] * 3
			
    for j,i in cornerList:
        resultMat[j][i] = resultMat[j][i] * 2
		
    for j,i in mineList:
        resultMat[j][i] = -1
		
    return resultMat