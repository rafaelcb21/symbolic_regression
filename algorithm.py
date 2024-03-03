def study1(n): # N^2
    for i in range(n):
        for j in range(i):
            pass

def study2(n): # sqrt(2)
    p = 0
    for i in range(n):
        p = p + i

# SORTING
# https://rosettacode.org/wiki/Sorting_algorithms/Insertion_sort#Python
def insertion_sort(L): # N and N^2 
    for i in range(1, len(L)):
        j = i-1 
        key = L[i]
        while j >= 0 and L[j] > key:
           L[j+1] = L[j]
           j -= 1
        L[j+1] = key

def insertion_sort_bin(seq): # N and N^2 
    for i in range(1, len(seq)):
        key = seq[i]
        low, up = 0, i
        while up > low:
            middle = (low + up) // 2
            if seq[middle] < key:
                low = middle + 1              
            else:
                up = middle
        seq[:] = seq[:low] + [key] + seq[low:i] + seq[i + 1:]

# https://rosettacode.org/wiki/Sorting_algorithms/Selection_sort#Python
def selection_sort(lst): # N^2
    for i, e in enumerate(lst):
        mn = min(range(i,len(lst)), key=lst.__getitem__)
        lst[i], lst[mn] = lst[mn], e

# https://rosettacode.org/wiki/Sorting_algorithms/Shell_sort#Python
def shell(seq): # N log N ou N^6/5 
    inc = len(seq) // 2
    while inc:
        for i, el in enumerate(seq[inc:], inc):
            while i >= inc and seq[i - inc] > el:
                seq[i] = seq[i - inc]
                i -= inc
            seq[i] = el
        inc = 1 if inc == 2 else inc * 5 // 11

# https://rosettacode.org/wiki/Sorting_algorithms/Quicksort#Python
def quick_sort(sequence): # N log N 
    lesser = []
    equal = []
    greater = []
    if len(sequence) <= 1:
        return sequence
    pivot = sequence[0]
    for element in sequence:
        if element < pivot:
            lesser.append(element)
        elif element > pivot:
            greater.append(element)
        else:
            equal.append(element)
    lesser = quick_sort(lesser)
    greater = quick_sort(greater)
    return lesser + equal + greater

# https://rosettacode.org/wiki/Sorting_algorithms/Heapsort#Python
def heapsort(lst): # N log N 
  ''' Heapsort. Note: this function sorts in-place (it mutates the list). '''

  # in pseudo-code, heapify only called once, so inline it here
  for start in range(int((len(lst)-2)/2), -1, -1):
    siftdown(lst, start, len(lst)-1)

  for end in range(int(len(lst)-1), 0, -1):
    lst[end], lst[0] = lst[0], lst[end]
    siftdown(lst, 0, end - 1)

def siftdown(lst, start, end):
  root = start
  while True:
    child = root * 2 + 1
    if child > end: break
    if child + 1 <= end and lst[child] < lst[child + 1]:
      child += 1
    if lst[root] < lst[child]:
      lst[root], lst[child] = lst[child], lst[root]
      root = child
    else:
      break

# SEARCHING
# https://rosettacode.org/wiki/Binary_search#Python
# Log N 
def binary_search(l, value=10001): # o numero 10001 serve para nao encontrar o numero, dessa forma entra no pior caso
    low = 0
    high = len(l)-1
    while low <= high: 
        mid = (low+high)//2
        if l[mid] > value: high = mid-1
        elif l[mid] < value: low = mid+1
        else: return mid
# Log N 
def binary_search_recursive(l, value=10001, low = 0, high = -1): # o numero 10001 serve para nao encontrar o numero, dessa forma entra no pior caso
    if not l: return -1
    if(high == -1): high = len(l)-1
    if low >= high:
        if l[low] == value: return low
        else: return -1
    mid = (low+high)//2
    if l[mid] > value: return binary_search_recursive(l, value, low, mid-1)
    elif l[mid] < value: return binary_search_recursive(l, value, mid+1, high)
    else: return mid

# DYNAMIC PROGRAMING
# https://rosettacode.org/wiki/Levenshtein_distance#Python
#def levenshteinDistance(str1, str2): # M*N
#    m = len(str1)
#    n = len(str2)
#    d = [[i] for i in range(1, m + 1)]   # d matrix rows
#    d.insert(0, list(range(0, n + 1)))   # d matrix columns
#    for j in range(1, n + 1):
#        for i in range(1, m + 1):
#            if str1[i - 1] == str2[j - 1]:   # Python (string) is 0-based
#                substitutionCost = 0
#            else:
#                substitutionCost = 1
#            d[i].insert(j, min(d[i - 1][j] + 1,
#                               d[i][j - 1] + 1,
#                               d[i - 1][j - 1] + substitutionCost))
