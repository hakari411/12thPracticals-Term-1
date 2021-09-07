def linear_search(li,element):
    '''
    Search using linear search method
    '''
    index=-1
    for i in li:
        index+=1
        if i==element:
            return index
            break
    else:
        return 0

def binary_search(li, element):
    '''
    Search using binary search method
    '''
    li.sort()
    start=0
    end=len(li)
    while True:
        index=(start+end)//2
        mid=li[index]
        
        if mid == element:            
            return index
        if mid<element:
            start+=1
        if mid>element:
            end-=1

        if start==end:
            return -1

    
