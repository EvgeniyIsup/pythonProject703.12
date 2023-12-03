nums = [3, 2, 4]
target = 6

def twoSum(nums, target):
    answer = 'В массиве нет такой пары чисел'
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if target == nums[i] + nums[j]:
                answer = 'Ответ: ' + str(i) + ' и ' + str(j)
    return answer

print(twoSum(nums, target))

