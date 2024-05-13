


a = [1, 3, 5, 7, 9]
k = 2

# 找到有多少个pair, 每个pair是两个index的组合, 两个index加一起的pair 能整除于 k
def solution(a, k):
    remainderDict = {}
    numOfAns = 0

    for num in a:
        remainder = num % k
        remainderDict[remainder] = remainderDict.get(remainder, 0) + 1
    for num in a:
        currentRemainder = num % k

        # if remainder is 0, it can be pair with other numbers has remainder is also 0
        if (currentRemainder == 0):
                                                     # if two reminder are the same, minus current reminder
            numOfAns += remainderDict.get(currentRemainder, 0) - 1

        # we can pair currentRemainder and pairRemainderValue together, and the sum is divisible by k 
        else:
            pairRemainderValue = k - currentRemainder
            if (currentRemainder == pairRemainderValue):
                                            # if two reminder are the same, minus current reminder
                numOfAns += remainderDict.get(pairRemainderValue, 0) - 1
            else:
                numOfAns += remainderDict.get(pairRemainderValue, 0)
    
    # since we pairing twice, diveide by 2
    return numOfAns // 2



print(solution(a,k))