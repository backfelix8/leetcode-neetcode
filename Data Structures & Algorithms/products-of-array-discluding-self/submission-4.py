class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        prod_nonzero = 1
        zero_amount = 0

        for num in nums:
            prod *= num
            if num == 0:
                zero_amount += 1
                continue
            prod_nonzero *= num
        
        result = []

        for num in nums:
            if num != 0:
                result.append(int(prod/num))
            elif num == 0 and zero_amount < 2:
                result.append(int(prod_nonzero))
            else:
                result.append(0)

        return result