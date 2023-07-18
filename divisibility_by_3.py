def divisibility_by_3(array):
    sum=0
    for i in range(len(array)):
        sum+=array[i]
    if sum%3==0:
        return 1
    else:
        return 0


array=list(map(int,input("Enter the Array Elements : ").split()))
print(divisibility_by_3(array))