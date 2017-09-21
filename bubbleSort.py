# This snippet will use bubble sort algorithm for sorting an array
array = [5, 7, 81, 1, 5, 1, 2, 5, 2, 1, 0, 48]
length = len(array)
print("Total Elements To Be Sorted Are", length)
print(array)

for i in range(0, length-2):
    for j in range(0, length-1):
        if array[j] > array[j + 1]:         #
            temp = array[j]                 #this tripple variable swap can
            array[j] = array[j + 1]         #be done in python as
            array[j + 1] = temp             #a,b=b.a

print(array)
