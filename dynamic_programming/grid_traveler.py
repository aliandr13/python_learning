# How man ways you can travel to the goal on grid with dimension m * n
# start at top left corner
# target bottom right corner
# only down or right moves

# time: O(2^(m+n))
# space: O(m+n)
def grid_traveler(m, n):
    if m == 1 and n == 1:
        return 1
    if m < 1 or n < 1:
        return 0
    return grid_traveler(m - 1, n) + grid_traveler(m, n - 1)


# time: O(m+n)
# space: O(m+n)
def grid_traveler_memo(m, n, memo={}):
    if m == 1 and n == 1:
        return 1
    if m < 1 or n < 1:
        return 0
    key = str(m) + ',' + str(n)
    if key in memo:
        return memo[key]
    memo[key] = grid_traveler_memo(m - 1, n, memo) + grid_traveler_memo(m, n - 1, memo)
    return memo[key]


print(grid_traveler_memo(1, 1))  # 1
print(grid_traveler_memo(2, 3))  # 3
print(grid_traveler_memo(3, 2))  # 3
print(grid_traveler_memo(3, 3))  # 6
print(grid_traveler_memo(18, 18))  # 2333606220
