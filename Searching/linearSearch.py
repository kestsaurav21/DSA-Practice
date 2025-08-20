
def linearSearch(arr, key):
    
    for i in arr:
        if key == i:
            return "Found key"
        
    return -1   



arr = [2,4,1,6,8,9,10,-1]
key = 6
print(linearSearch(arr, key))