import sys

def diagonalDifference(a):
    n = len(a)
    # Complete this function
    i=0
    j=0
    l=n-1
    sum1 = 0
    sum2 = 0
    for jj in range(0,n):
        sum1 += a[i][j]        
        sum2 += a[i][l]
        i+=1
        j+=1
        l-=1
    return abs(sum1-sum2)

if __name__ == "__main__":
    n = int(input().strip())
    a = []
    for a_i in range(n):
       a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
       a.append(a_t)
    result = diagonalDifference(a)
    print(result)
