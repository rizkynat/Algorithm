import pandas as pd
import numpy as np

def normalization(table,row, col, r, cost):
    #initilize array
    for x in range(row):
        for y in range(col):
            if(table.columns[y] not in cost):
                r[x][y] = round(table[table.columns[y]][x]/max(table[table.columns[y]]), 2)
            else:
                r[x][y] = round(min(table[table.columns[y]])/table[table.columns[y]][x], 2)

#print(table.columns[2])
    print(r)

def ranked(row, col, weight, r):
    #ranked process
    maxRanked=0
    v = [0 for x in range(row)]
    for x in range(row):
        data=0
        for y in range(col):
            data += r[x][y]*weight[y]
        v[x]=round(data,3)
        if(x>1):
            if(v[x]>v[x-1]):
             maxRanked=x
        print('V'+str(x+1),':',v[x])

    print('The Best alternative is V'+str(maxRanked+1)+' with value ',max(v))

def main():
    #table
    content_table=np.array([[70, 50, 80, 60],
                            [50, 60, 82, 70],
                            [85, 55, 80, 75],
                            [82, 70, 65, 85],
                            [75, 75, 85, 74],
                            [62, 50, 75, 80]])
    #weight or bobot
    weight = [0.35, 0.25, 0.25, 0.15]
    #list of criteria
    index_criteria = ['c1','c2','c3','c4']    
    cost = np.array([])
    #list of alternatif
    index_alternatif = ['rina','rani','reni','renu','roni','rossy']
    #table
    table = pd.DataFrame(content_table, columns=index_criteria, index=index_alternatif)   
    row = table.shape[0]
    col = table.shape[1]
    size = table.size
    r = [[0 for x in range(col)] for y in range(row)]
    normalization(table, row, col, r, cost)
    ranked(row, col, weight, r)

if __name__ == "__main__":
    main() 