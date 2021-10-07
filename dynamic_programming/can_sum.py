###
# Write a function that return boolean indicating whether it is possible
# to generate the targetSum using numbers from the array.
#
# Element of the array may be used as many times as needed.
# All input numbers are non-negative.

# m = targetSum; n=numbers.length
# time: O(n^m); space: O(m)
def can_sum_brute(target_num, numbers):
    if target_num == 0:
        return True
    if target_num < 0:
        return False

    for number in numbers:
        reminder = target_num - number
        if can_sum(reminder, numbers):
            return True

    return False


def can_sum_memo(target_num, numbers):
    return can_sum(target_num, numbers, {})


# m = targetSum; n=numbers.length
# time: O(n*m); space: O(m)
def can_sum(target_num, numbers, memo):
    if target_num == 0:
        return True
    if target_num < 0:
        return False
    if target_num in memo:
        return memo[target_num]

    for number in numbers:
        reminder = target_num - number
        if can_sum(reminder, numbers, memo):
            memo[target_num] = True
            return True
    memo[target_num] = False
    return False


print(can_sum_memo(7, (2, 3)))  # true
print(can_sum_memo(7, (5, 3, 4, 7)))  # true
print(can_sum_memo(7, (2, 4)))  # false
print(can_sum_memo(8, (2, 3, 5)))  # true
print(can_sum_memo(300, (7, 14)))  # false
