def power_set (nums):
    output = []
    def helper (nums,i,subset):
        if i == len(nums):
            output.append(subset.copy())
            return
        helper(nums,i+1,subset)
        subset.append(nums[i])
        helper(nums,i+1,subset)
        subset.pop()
    helper(nums,0,[])
    return output


array = [1,8,7]
print(power_set(array))
