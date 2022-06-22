from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        
        def dfs(currCombination, total, remainingCandidates):
            # Solved Case
            if total == target:
                res.append(currCombination.copy())
                return
            # For every option
            for i, c in enumerate(remainingCandidates):
                # If fail, continue to next option
                if total + c > target:
                    return
                # Add option flags
                currCombination.append(c)
                #   Call next backtrack iteration
                dfs(currCombination, total + c, remainingCandidates[i:])
                # Remove flags so we can move onto next option
                currCombination.pop()
        
        # Call initial backtrack
        dfs([], 0, candidates)
        # Return everything we found
        return res