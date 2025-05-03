

def find_match(nums):
    for i in range(len(nums)):
        target = nums[i]
        others=nums[:i] + nums[i+1:]
        if target == sum(others):
            print(f"find match {target} == {others}")
            return True

    print("no match found")
    return False

nums = [5, 2, 11, 3]
print(find_match(nums))