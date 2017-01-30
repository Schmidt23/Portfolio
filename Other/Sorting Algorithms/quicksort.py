

unsorted = [0,11,4,8,3,7,12,33]
pivot = unsorted[0]

def qsort(lis):
    pivotList = []
    lesser = []
    more =  []

    if len(lis) <= 1:
        return lis
    else:
        pivot = lis[0]
        for i in lis:
            if i < pivot:
                lesser.append(i)

            elif i > pivot:
                more.append(i)
            else:
                pivotList.append(i)
        lesser = qsort(lesser)
        more = qsort(more)

    return lesser + pivotList + more

sortd = qsort(unsorted)

print sortd
