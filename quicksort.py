import random
def quicksort (List):
    if len (List) <= 1 : return List
    rnd = random.randint(0 , len(List)-1)
    pivot = List[rnd]
    less = [i for i in List if i < pivot]
    great = [i for i in List if i > pivot]
    equal = [i for i in List if i== pivot]
    less = quicksort (less)
    great = quicksort (great)
    return less + equal + great

List = [7,11,5,4,10,12,15,13]
Answer = quicksort(List)
print (Answer)

    
