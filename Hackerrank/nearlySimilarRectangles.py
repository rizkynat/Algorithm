
def nearlySimilarRectangles(sides):
    n = len(sides)
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            if(sides[i][0]/sides[i][1] == sides[j][0]/sides[j][1]):
                count+=1
    print(count)

from collections import defaultdict
def nearlySimilarRectangles1(sides):
    # Write your code here
    ans = 0
    umap = defaultdict(int)
    for i in range(len(sides)):
 
        ratio = sides[i][0] / sides[i][1]
        umap[ratio] += 1
 
    # Calculate pairs of similar rectangles from its common ratio
    for x in umap:
 
        value = umap[x]
        if (value > 1):
            ans += (value * (value - 1)) / 2
 
    return int(ans)


side = [[4,8],[15,30],[25,50]]
sides=[[2,1],[10,7],[9,6],[6,9],[7,3]]
nearlySimilarRectangles(side)