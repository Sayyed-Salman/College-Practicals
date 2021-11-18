
# Merge Sort 
def mergesort(ALIST):
    if len(ALIST) > 1:
        mid = len(ALIST)//2
        lefthalf = ALIST[:mid]
        righthalf = ALIST[mid:]

        mergesort(lefthalf)
        mergesort(righthalf)
        i = 0   
        j = 0
        k = 0

        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                ALIST [k] = lefthalf[i]
                i = i + 1
            
            else:
                ALIST[k] = righthalf[j]
                j = j+1
            k = k+1
        
        while i < len(lefthalf):
            ALIST[k] = lefthalf[i]
            i = i+1
            k = k+1

        while j < len(righthalf):
            ALIST[k] = righthalf[i]
            j = j+1
            k = k+1

ALIST = [1,2,5,6,2]
print("Unsorted List:{}".format(ALIST))
mergesort(ALIST)
print("Sorted List :{}".format(ALIST))
print("123")
