class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [1] * len(nums)
        post = [1] * len(nums)
        out = [1] * len(nums)

        prod = 1
        for i, n in enumerate(nums):
            pre[i] = prod * n
            prod = pre[i]

        prod = 1
        for i in range(len(nums) - 1, 0, -1):
            post[i] = prod = prod * nums[i]

        out[0] = post[1]
        out[len(nums)-1] = pre[len(nums)-2]
        for i in range(1, len(nums)-1, 1):
            out[i] = pre[i-1] * post[i+1]

        return out
        