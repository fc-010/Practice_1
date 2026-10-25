def stats(nums):
    lo = min(nums)
    hi = max(nums)
    avg = sum(nums) / len(nums)
    return lo, hi, avg


def grade(marks, passing=50):
    if marks >= passing:
        return "Pass"
    else:
        return "Fail"


numbers = [4, 8, 15, 16, 23, 42]

lo, hi, avg = stats(numbers)
print(lo, hi, avg)

print(grade(55), grade(55, passing=60))
