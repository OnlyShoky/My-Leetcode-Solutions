from typing import List
import time


class Solution:
    # Problem 1: Combination Sum
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            if i >= len(nums) or total > target:
                return

            cur.append(nums[i])
            dfs(i, cur, total + nums[i])
            cur.pop()
            dfs(i + 1, cur, total)

        dfs(0, [], 0)
        return res
            


    # Problem 2: Word Search
    def exist(self, board, word):
        start = time.time()
        
        res = False
        # board[3][0]
        def dfs(board,i,j,curr,visited):
            nonlocal res
            if res:
                return
            
            if len(curr) > len(word) or i> (len(board)-1) or j >(len(board[0])-1) or i < 0 or j < 0 :
                return

             
                
            curr.append(board[i][j])
            currentMove = (i,j)
            visited.append(currentMove)
            
            if ''.join(curr) == word:
                res = True
                
            if word.startswith(''.join(curr)):
                if (i+1,j) not in visited:
                    dfs(board,i+1,j,curr, visited.copy())
                if (i,j+1) not in visited:
                    dfs(board,i,j+1,curr, visited.copy())
                if (i-1,j) not in visited:
                    dfs(board,i-1,j,curr, visited.copy())
                if (i,j-1) not in visited:
                    dfs(board,i,j-1,curr, visited.copy())
            else:
                curr.pop()
                visited.pop()
            
            print(curr)
            # curr.pop()
            
                
                  
        # dfs(board, 0,0,[],[(-1,-1),])
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                dfs(board,i,j,[],[(-1,-1),])
        
        end = time.time()
        print("{:.6f}".format(end - start))
        
        return res
        

# Create an instance of Solution
solution = Solution()

# Example for Combination Sum
print("Combination Sum:")
candidates = [2,3,6,7]
target = 7
print(f"Input: candidates = {candidates}, target = {target}")
print(f"Output: {solution.combinationSum(candidates, target)}\n")

# Example for Word Search
print("Word Search:")
board = [["C","A","A"],
 ["A","A","A"],
 ["B","C","D"]]

word = "AAB"

print(f"Input: board = {board}, word = \"{word}\"")
print(f"Output: {solution.exist(board, word)}")