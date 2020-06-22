# O(n^2) time | O(1) space

def solutionOne(array, targetSum):
    for i in range(len(array) - 1):
        firstNum = array[i]
        for j in range(len(array)):
            secondNum = array[j]
            if firstNum + secondNum == targetSum:
                return [firstNum, secondNum]
    return []

print('Double loop', solutionOne([1, 9, 3, 4, 5], 7))

# O(n) time | O(n) space

def solutionTwo(array, targetSum):
    numsHash = {}
    for num in array:
        potentialMatch = targetSum - num
        if potentialMatch in numsHash:
            return [potentialMatch, num]
        else:
            numsHash[num] = True
    return []

print('Using hash table', solutionTwo([1, 9, 3, 4, 5], 7))

# O(n.log(n)) time | O(1) space

def solutionThree(array, targetSum):
    array.sort()
    left = 0
    right = len(array) - 1

    while left < right:
        if array[left] + array[right] == targetSum:
            return [array[left], array[right]]
        elif array[left] + array[right] < targetSum:
            left += 1
        else:
            right -= 1

    return []

print('Using left and right pointer', solutionThree([1, 9, 3, 4, 5], 7))
