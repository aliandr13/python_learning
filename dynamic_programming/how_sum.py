# The function should return an array containing any combination of
# elements that add up to exactly the targetSum. If there is no combination that adds up
# to the targetSum, then return null.
# <p>
# If there are multiple combinations possible, return any single one.

# m - targetSum; n = numbers.length
# time: O(n^m); space(m)
def how_sum_brute(target_sum, numbers):
    if target_sum == 0:
        return []
    if target_sum < 0:
        return None

    for num in numbers:
        remainder = target_sum - num
        result = how_sum(remainder, numbers)
        if result is not None:
            result.append(num)
            return result
    return None


def how_sum(target_sum, numbers):
    return how_sum_memo(target_sum, numbers, {})


# time: O(n*m); space(m)
def how_sum_memo(target_sum, numbers, memo):
    if target_sum == 0:
        return []
    if target_sum < 0:
        return None
    if target_sum in memo:
        return memo[target_sum]

    for num in numbers:
        remainder = target_sum - num
        result = how_sum_memo(remainder, numbers, memo)
        if result is not None:
            result.append(num)
            memo[target_sum] = result
            return result

    memo[target_sum] = None
    return None


print(how_sum(7, [2, 3]))  # [3, 2, 2]
print(how_sum(7, [5, 3, 4, 7]))  # [4, 3]
print(how_sum(7, [2, 4]))  # None
print(how_sum(8, [2, 3, 5]))  # [2, 2, 2, 2]
print(how_sum(400, [7, 14]))  # None
