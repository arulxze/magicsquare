nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]          # Numbers involved in the magic square
sidesum = sum(x for x in nums) / 3          # Sum of side

def sum_to_n(n, size, limit=None):
    """ Produce all lists of `size` positive integers in decreasing order
    that add up to `n`.
        
        FLAGS
        -----
        - Remove duplicates in the list
        - Remove numbers out of the range in the list n
    """
    if size == 1:
        yield [n]
        return
    if limit is None:
        limit = n
    start = (n + size - 1) // size
    stop = min(limit, n - size + 1) + 1
    for i in range(start, stop):
        for tail in sum_to_n(n - i, size - 1, i):
            yield [i] + tail

tot = []                                    # Total possibilites

for side in sum_to_n(sidesum, 3):
    if len(side) == len(set(side)):         # Check for duplicates
        if all(x < 10 for x in side):       # Make this statement more generic
                                            # The highest element may not be n
                                            # FLAG: check if x is equal to any
                                            # element in nums
                                            
            side.sort()                     # PROB: sort the list
            tot.append(side)
            
print tot                                   # FLAG: temp

# FLAG: dependent
# IMPR: use dynamic programming

for x in xrange (0, len(tot)):
    for y in xrange(0, len(tot)):
        temp = tot[x] + tot[y]
        if len(temp) == len(set(temp)):
            continue
        for z in xrange(0, len(tot)):
            temp += tot[z]
            print tot
            
            
# 0 1 2
# 3 4 5
# 6 7 8
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
