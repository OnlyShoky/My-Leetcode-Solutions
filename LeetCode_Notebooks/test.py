class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n1 = len(text1)
        n2 = len(text2)
        
        setText1 = set(text1)
        setText2 = set(text2)
        
        finalResult = 0
        for i in range(n1):
            print(f"i: {i}")
            if(text1[i] in setText2):
                k = i
                result = 0
                for j in range(n2):
                    print(f"  j: {j}, k: {k}")
                    if k < n1 and text1[k] == text2[j]:
                        k+= 1
                        result += 1
                        
                    while k < n1 and text1[k] not in setText2 :
                        k+=1
                finalResult = max(finalResult,result)
                
        return finalResult
# Create an instance of Solution
solution = Solution()

# Test cases
print("Longest Common Subsequence:")

text1="pmjghexybyrgzczy"
text2="hafcdqbgncrcbihkd"
expected4 = 4
print(f"Input: text1 = {text1}, text2 = {text2}")
print(f"Output: {solution.longestCommonSubsequence(text1, text2)}, Expected: {expected4}\n")