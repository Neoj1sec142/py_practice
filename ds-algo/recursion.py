# No recursion
# def sum(nums):
#     tot = 0
#     for num in nums:
#         tot += num
#     return tot

lst = [2,1,4,6,4,2]
# Using recursion and slice
def recursive_sum(nums):
    if not nums:
        return 0
    # print("Calling rec-sum(%s)"%nums[1:])
    remaining_sum = recursive_sum(nums[1:])
    # print("Call to sum(%s) returning %d + %d" % (nums, nums[0], remaining_sum))
    return nums[0] + remaining_sum

# print(recursive_sum(lst))
