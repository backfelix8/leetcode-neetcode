class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets=[]

        for i in range(len(nums)):
            if i >0 and nums[i] == nums[i-1]:
                continue
            
            index2 = i + 1
            index3 = len(nums) - 1

            while index2 < index3:
                total = nums[i] + nums[index2] + nums[index3]
    
                if total == 0:
                    triplets.append([nums[i], nums[index2], nums[index3]])
                    index2 += 1
                    index3 -= 1

                    while index2 < index3 and nums[index2] == nums[index2 - 1]:
                        index2 += 1

                elif total < 0:
                    index2 += 1
                
                elif total > 0:
                    index3 -= 1

        return triplets