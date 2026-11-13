class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        numset = set(nums)
        max_seq = 1
        
        for num in numset:
            max_inner = 1
            next_num = num + 1
            
            if (num - 1) not in numset:
                while next_num in numset:
                    max_inner +=1
                    next_num += 1

            if max_inner > max_seq:
                max_seq = max_inner

        return max_seq 