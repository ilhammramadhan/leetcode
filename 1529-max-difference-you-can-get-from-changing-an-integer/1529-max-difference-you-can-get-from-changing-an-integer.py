class Solution:
    def maxDiff(self, num: int) -> int:
        numStr = str(num)
        numLen = len(numStr)
        
        # Find the maximum number
        maxNum = numStr
        for digit in numStr:
            if digit != '9':
                maxNum = numStr.replace(digit, '9')
                break
        #Case 1 The first digit is not 1 
        minNum = numStr
        if numStr[0] != '1':
            digit_to_replace = numStr[0]
            minNum = numStr.replace(digit_to_replace, '1')
        #Case 2 The first digit is 1
        else: 
            for digit in range(1,numLen):
                if numStr[digit] not in ('0','1'):
                    digit_to_replace = numStr[digit]
                    minNum = numStr.replace(digit_to_replace, '0')
                    break
        return int(maxNum) - int(minNum)