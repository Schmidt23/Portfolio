

def merge_sort(lst):
    if len(lst) <= 1:
        return lst

    left = []
    right = []

    for i in xrange(len(lst)):
        if i % 2 == 0:
            left.append(lst[i])
        else:
            right.append(lst[i])

    left = merge_sort(left)
    right = merge_sort(right)
    #print "l, r", left, right
    return merge(left, right)


def merge(left, right):

    result = []

    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))

    while len(left) > 0:
        result.append(left.pop(0))

    while len(right) > 0:
        result.append(right.pop(0))

    #print result
    return result

b = [1,4,3,7,5,9,2,8,6]

print merge_sort(b)