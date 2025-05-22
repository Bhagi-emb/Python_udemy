#Remove Duplicates from Sorted Array
# /* https://leetcode.com/explore/featured/card/top-interview-questions-easy/92/array/727/ */
# /*
# Input: nums = [0,0,1,1,1,2,2,3,3,4]
# Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
# Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).
# */

array = [0, 1, 1, 3, 3, 1, 2, 4, 3, 1, 4]
print("Input array:", array)
print("Input array length:", len(array))  # 11


#functions# Remove duplicates from sorted array
def removeDuplicates(array, len_array):
    if len_array == 0:
        return 0
    
    #sort the array
    array.sort()
    print("Sorted array:", array)

    #remove duplicates
    unique_index = 1
    for i in range(1, len_array):
        if array[i] != array[i-1]:
            array[unique_index] = array[i]
            unique_index += 1
    #fill the rest of the array with underscores
    for i in range(unique_index,len_array):
        array[i] = '_'
    print("Sorted array:", array)
    return unique_index  # Return the length of unique elements

### main
len_array = len(array)
unique_len = removeDuplicates(array, len_array)
print("Length after removing duplicates:", unique_len) 

