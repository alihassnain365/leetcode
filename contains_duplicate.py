from collections import defaultdict
def containsDuplicate(nums):
    num_count = defaultdict(int)

    for num in nums:
        num_count[num] +=1
        if(num_count.get(num) ==2 ):
            return False
    print(num_count)
    
    return True
print(
containsDuplicate([1,2,3,1]))
