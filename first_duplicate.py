def first_duplicate(arr):
    arr1=[]
    for value in range(len(arr)):
        if arr[value] in arr1:
            return arr[value]
        else:
            arr1.append(arr[value])
print(first_duplicate([1,2,3,2,1])
