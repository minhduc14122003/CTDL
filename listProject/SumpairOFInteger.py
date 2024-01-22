def twoSum(nums,target):
    pairs = []
    for i,num in enumerate(nums):
        remain = target - num
        for j, numb in enumerate(nums):
            if numb == remain and[i,j] not in pairs and [j,i] not in pairs:
                pairs.append([i,j])
    return pairs
import array
nums = array.array("i",[2,3,5,7,9])
target = 7
result = twoSum(nums,target)

if result:
    for el in result:
        print(el)
else:
    print("No pairs found.")