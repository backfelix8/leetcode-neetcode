class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        elements = {}
        for num in nums:
            elements[num] = elements.get(num, 0) + 1

        frequencies = []
        for num, freq in elements.items():
            frequencies.append([freq, num])
        
        frequencies.sort()
        frequencies.reverse()
        frequencies = frequencies[:k]

        result = []
        for frequency in frequencies:
            result.append(frequency[1])

        return result


         
