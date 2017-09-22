#This snippet will sort an array with Insertion sort
array=[]
check=True
while check==True:
    a=input("Enter Number \n  Or Press Q to Stop  ")
    if (a=="Q") or (a=="q"):
        break
    else:
     array.append(int(a))

length=len(array)
print("Total Elements To Be Sorted Are", length)
print("Unsorted Array = ",array)

temp=0
for i in range(1,length):
    temp=array[i]
    j=i
    while j>0 and array[j-1]>temp:
        array[j]=array[j-1]
        j=j-1        # Consider this decrement
    array[j]=temp    # when replacing array value
print("Sorted Array = ",array)#with temp