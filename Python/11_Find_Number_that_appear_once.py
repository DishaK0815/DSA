
# brute force method 
def chek_number_appear_once_brute(arr):
    n = len(arr)
    for i in  range(n):
        count = 0
        for j in range(n):
            if arr[i] == arr[j]:
                count += 1
        if count == 1:
            return arr[i]

arr = [4,3,2,8,1,4,2,3,1]
print("Brute force: ", chek_number_appear_once_brute(arr))  # Output: 8


# better appraoch using hashmap
def check_number_appear_once_better(arr):
    num_count = {}
    for num in arr:
        if num in num_count:
            num_count[num] += 1
        else:
            num_count[num] = 1
    for num, count in num_count.items():
        if count == 1:
            return num
arr = [4,3,2,8,1,4,2,3,1]
print("Better approach: ", check_number_appear_once_better(arr))  # Output: 8


# optimal approach using XOR
def check_number_appear_once_optimal(arr):
    result = 0
    for num in arr:
        result ^= num
    return result
arr = [4,3,2,8,1,4,2,3,1]
print("Optimal approach: ", check_number_appear_once_optimal(arr))  # Output: 8