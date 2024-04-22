# 752. Open the Lock
from collections import deque

class Solution(object):
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        if "0000" in deadends:
            return -1
        if target == "0000":
            return 0

        def findChildren(password):
            res = []
            for i in range(4):
                digit = str((int(password[i]) + 1) % 10)
                res.append(password[:i] + digit + password[i+1:])
                
                digit = str((int(password[i]) - 1 + 10) % 10)
                res.append(password[:i] + digit + password[i+1:])

            return res
    
        queue = deque()
        queue.append(["0000", 0])
        # assign deadends
        visit = set(deadends)
        while queue:
            password, turns = queue.popleft()
            if (password == target):
                return turns
            for child in findChildren(password):
                if (child not in visit):
                    visit.add(child)
                    queue.append([child, turns + 1])

        return -1


def closestWayToTarget(currNum, targetNum):
    step = 0
    # increase the num to target
    if ((targetNum - currNum) < (currNum + 9 - targetNum)):
        while (currNum != targetNum):
            currNum += 1
            print(currNum)
            step += 1
    # decrease the num to target
    else:
        while (currNum != targetNum):
            if (currNum > 0):
                currNum -= 1
            else:
                currNum = 9
            print(currNum)
            step += 1
    return step

def checkDeadLock(deadends, curr):
    for deadend in deadends:
        if (curr == deadend):
            return True
    return False
