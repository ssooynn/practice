'''
How to solve it 
1. Find longest non-increasing suffix
2. Find the pivot: Look at the element immediately to the left of the suffix (it must be smaller than the head of the suffix)
3. Select the smallest element in the suffix that is bigger than the pivot
4. Swap the pivot and the element
5. Reverse the suffix
'''

def biggerIsGreater(w):
    w = list(w)
    i = len(w) - 1
    while i >= 0 and w[i-1] >= w[i]:
        i -= 1

        if i <= 0:
            return "no answer"
        
    j = len(w) - 1
    while w[j] <= w[i-1]:
        j -= 1

    w[i-1], w[j] = w[j], w[i-1]

    j = len(w) - 1
    while i < j :
        w[i], w[j] = w[j], w[i]
        i += 1
        j -= 1

    return ''.join(w)
    
