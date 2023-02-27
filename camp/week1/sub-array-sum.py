class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ps_map = {0: 1}
        count = 0
        ps = 0
        for n in nums:
            ps += n
            if ps - k in ps_map:
                count += ps_map[ps - k]
            ps_map[ps] = ps_map.get(ps, 0) + 1

        return count