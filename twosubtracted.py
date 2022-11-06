# Similar to the twosum but two subtracted
def twosubtracted(nums, target):
    d = {}
    nums.sort(reverse=True)
    for i in range(len(nums)):
        key = target + nums[i]
        if key in d:
            return [i, d[key]]
        d[nums[i]] = i


print(
    twosubtracted(
        [
            2,
            4,
            5,
            10,
            22,
            333,
            4,
            5,
            7,
            8,
            9,
            10,
            4,
            6,
            8,
            9345,
            6788,
            876,
            4,
            5,
            7,
            9,
            10,
        ],
        2557,
    )
)
