def isMissing(nums:list):
    """retuns the missing element"""
    nums.sort()
    clone = [i for i in range(nums[0],nums[-1])]
    return list(set(clone)-set(nums))
    



print(isMissing([1,2,5,4]))

    
