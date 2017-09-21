# This snippet will use bubble sort algorithm for sorting an array
array=[]
check=True
while check==True:
    a=input("Enter Number \n  Or Press Q to Stop  ")
    if (a=="Q") or (a=="q"):
        break
    else:
        array.append(int(a))

length = len(array)
print("Total Elements To Be Sorted Are", length)
print("Unsorted Array = ",array)

for i in range(0, length-2):
    for j in range(0, length-1):
        if array[j] > array[j + 1]:         #
            temp = array[j]                 #this tripple variable swap can
            array[j] = array[j + 1]         #be done in python as
            array[j + 1] = temp             #a,b=b.a

print("Sorted Array = ",array)
