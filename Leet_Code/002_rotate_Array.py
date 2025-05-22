# Rotate Array
# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation: nums = [1,2,3,4,5,6,7]
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]

list = [1,2,3,4,5,6,7]
size = len(list)
k =3

k =k %size

# rotate the list
list.reverse()
print("Reversed list:",list)  # Output: [7,6,5,4,3,2,1]
list[0:k] = list[0:k][::-1]  # list[0:k].reverse() -> return none
list[k:size] =list[k:size][::-1]  # list[k:size].reverse() -> return none

print("Roatating list:",list)  # Output: [5,6,7,1,2,3,4]