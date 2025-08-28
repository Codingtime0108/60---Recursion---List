def arraySum(a):
    length = len(a)

    if length == 1:
        return a[0]
    
    return a[0]+ arraySum(a[1:])

a = [1,2,3,6,9]


print("Array total sum: ", arraySum(a))