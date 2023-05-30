def all_permutations(nums):
    permutations = []
    if len(nums)==0: return [[]]
    def helper(nums,i):
        if i == len(nums) -1:
            permutations.append(nums.copy())
            return
        for j in range(i,len(nums)):
            nums[i],nums[j] = nums[j],nums[i]
            helper(nums,i+1)
            nums[i],nums[j] = nums[j],nums[i]
    helper(nums,0)
    return permutations


array = [1,2,3]
print(all_permutations(array))
