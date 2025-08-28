def checksorted(a):
    length = len(a)

    if length == 1 or length ==0:
        return True
    
    return a[0] <= a[1] and checksorted(a[1:])

a = [1,2,3,4,5]

if checksorted(a):
    print("\nYes given array is sorted!")
else:
    print("\nNo given array is not sorted:(")