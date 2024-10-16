class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        # one line solutionm
        #return len(s) == len(goal) and goal in s+s

        #dumb way
        # check the length
        if len(s) != len(goal):
            return False 

        for i in range(len(s)): 
            shifted = s[i:] + s[:i]

            if shifted == goal: 
                return True
        return False

        