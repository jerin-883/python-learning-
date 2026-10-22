
def checkfun(arr2):
    
    n = len(arr2)
    for i in range(n-1):         
        if arr2[i] > arr2[i+1]:

            for i in range(n-1):         
                    if arr2[i] < arr2[i+1]:
                        return False
                    return True
    return True


arr2 =[0,1,2,3,4,5,6,7,8,9,10]
# arr2 = [2,4,5,7,3,1,10,9,0,1,6]
# arr2 = [10,9,8,7,6,5,4,3,2,1,0]


checkfun(arr2)
print (checkfun(arr2))