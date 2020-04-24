from time import *
start = clock()

def merge_sort(li):
    if len(li) < 2: return li
    m = len(li) / 2
    return merge(merge_sort(li[:m]), merge_sort(li[m:]))

def merge(l, r):
    result = []
    i = j = 0
    while i < len(l) and j < len(r):
        if l[i] < r[j]:
            result.append(l[i])
            i += 1
        else:
            result.append(r[j])
            j += 1            
    result += l[i:]
    result += r[j:]
    return result

list1 = []
with open('IntegerArray.txt','r') as f:
    for line in f.readlines():
        list1.append(int(line))

print clock() - start