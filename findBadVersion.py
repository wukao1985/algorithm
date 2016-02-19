#!/usr/bin/python
# This implementation works on local, but lintcode
# returns error for n=10 case, which I have the 
# unit test showing is working.
# Let's see what might going wrong?

A = [False] * 9 + [True]
print (A)
def isBadVersion(index):
    return A[index-1]

def findFirstBadVersion(n):
    # write your code here
    index = 1
    
    while index < n:
        if isBadVersion(index) == False:
            index = 2*index + 1
        else:
            break
        
    # if index is > n
    # we should do binary search between index/2 to n
    # otherwise we should do binary search between 0 to index
    if index > n:
        start = index/2
        end = n
    else:
        start = 1
        end = index

    while end > start:
        mid = (end+start)/2
        if isBadVersion(mid) == False and isBadVersion(mid+1) == True:
            return mid+1
        else:
            if isBadVersion(mid) == False:
                start = mid+1
            else:
                end = mid-1
    return end

print 'the bad version is', findFirstBadVersion(10)