'''You are given as input an unsorted array of n distinct numbers,
where n is a power of 2. Give an algorithm that identifies the second-largest
number in the array, and that uses at most n+log2n−2 comparisons. '''


def Largest(a_list):
    if len(a_list) <= 1:
        return a_list[0], []
    elif len(a_list) == 2:  #n^0.5 comparisons
        if a_list[0] > a_list[1]:
            largest = a_list[0]
            SL_list = [a_list[1]]
        else:
            largest = a_list[1]
            SL_list = [a_list[0]]
        return largest, SL_list

    mid = len(a_list) // 2
    left = a_list[:mid]
    right = a_list[mid:]
    largestL, SL_list_L = Largest(left)
    largestR, SL_list_R = Largest(right)

    if largestL >= largestR:    #n^0.5 - 1 comparisons
        SL_list_L.append(largestR)
        return largestL, SL_list_L
    else:
        count +=1
        SL_list_R.append(largestL)
        return largestR, SL_list_R

def secondLargest(a_list):
    largest, SL_list = Largest(a_list)
    sLargest = SL_list[0]
    #log2(n) - 1 comparisons
    for num in SL_list[1:]:
        if num > sLargest:
            sLargest = num
    return sLargest


a_list = [44,31,5,24,3,6,12,111,84,54,91,75,68,109,80,18]
sLargest = secondLargest(a_list)
print("Second Largest:", sLargest)
