def mostActive(customers):
    # Write your code here
    n=len(customers)
    res=dict()
    for i in customers:
        if i not in res:
            res[i]=1
        else:
            res[i]+=1
    perc=dict()
    for i in res:
        perc[i]= (res[i]/n)*100
    b=[]
    for i in perc:
        if perc[i]>=5:
            b.append(i)
    return(sorted(b))

customers = ["Bigcorp", "Bigcorp", "Acme", "Bigcorp", "Zork", "Zork", "Abc", "Bigcorp", "Acme", "Bigcorp", "Bigcorp", "Zork", "Bigcorp", "Zork", "Zork", "Bigcorp", "Acme", "Bigcorp", "Acme", "Bigcorp", "Acme", "Littlecorp", "Nadircorp"]
print(mostActive(customers))