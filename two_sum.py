# def twoSum(nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         for first in range(0,len(nums)):
#             # if the number at first is greater than target
#             if nums[first] > target:
#                 continue
#             elif nums[first] == target:
#                 return [first]
#             for second in range(first+1,len(nums)):
#                 if nums[second] > target:
#                     continue
#                 elif nums[second] == target:
#                     return [second]  
#                 elif nums[first] + nums[second] == target:
#                     return [first,second] 

# print(twoSum([3,2,4],6))

""" a better approach"""

def twoSum(nums:list, target:int) ->list:
    """returns the index of the two numbers that sums to the target"""
    seen = dict()

    for index,num in enumerate(nums):
        candidate = target-num
        if candidate in seen:
            return [index,seen.get(candidate)]
        else:
            seen.update({num:index})


print(twoSum([3,3],6))
