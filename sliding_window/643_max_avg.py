def findMaxAverage(nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
    
        prev_idx = 0
        next_idx = k

        # finding the first window than add or remove elements in it so far
        max_sum = 0
        for n in range (0,k):
            max_sum += nums[n]
        
        win_s = 1
        win_e = win_s + k-1

        while next_idx < len(nums):
            temp_sum = max_sum
            max_sum = max_sum - nums[prev_idx] + nums[next_idx]
            next_idx += 1
            prev_idx += 1

            if max_sum < temp_sum:
                max_sum = temp_sum

        


        return max_sum/k

print(findMaxAverage([1,12,-5,-6,50,3],4))



     

        


        
        
