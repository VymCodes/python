import array as arr 


array_num = arr.array("i",[1,2,3,5,3,7,9,3])
print("Original array: "+str(array_num))


print("Number of occurrences of the number 3 in the said array:"+str(array_num.count(3)))


array_num.reverse()
print("Reverse the orger of the items:")
print(str(array_num))
print(array_num[::-1])

print(array_num[::1])

    
