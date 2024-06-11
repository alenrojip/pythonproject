#Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.
def permute(nums):
    def backtrack(start):
        if start==len(nums):
            permutations.append(nums[:])
            return
        
        for i in range(start,len(nums)):
            nums[start],nums[i]=nums[i],nums[start]
            backtrack(start+1)
            nums[start],nums[i]=nums[i],nums[start]
    
    permutations=[]
    backtrack(0)
    return permutations

nums=[354,716,128,90378]
print(permute(nums))