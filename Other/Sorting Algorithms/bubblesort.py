

def bubblesort(list):
    for i in xrange (len(list)-1):
        try:
            if list[i] > list[i+1]:
                list[i], list[i+1] = list[i+1], list[i]
                bubblesort(list)
            else:
                continue
        except Exception, e:
            print e
            continue

    return list

fu = [2,4,3,1,23, 12, 8]

print bubblesort(fu)
