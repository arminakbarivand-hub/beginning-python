def bublesort ( List):
    for i in range (0 , len(List)):
        for j in range (0 ,len(List)-i-1):
            if List[j] > List [j+1]:
                M = List[j]
                List[j] = List[j+1]
                List[j+1]=M

    return List

List = [ 100,25,250,146,36,3,85,194]
Answer = bublesort(List)
print (Answer)
