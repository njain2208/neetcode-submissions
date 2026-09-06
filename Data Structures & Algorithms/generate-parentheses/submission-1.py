class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        openParentheses = 0
        ans = []
        substring = []

        def dfs(n, openParentheses):
            nonlocal ans, substring
            if n == 0:
                for _ in range(openParentheses):
                    substring.append(")")

                ans.append("".join(substring))

                for _ in range(openParentheses):
                    substring.pop()
                return

            if openParentheses > 0:
                substring.append(")")
                dfs(n, openParentheses-1)

                substring.pop()

            substring.append("(")
            dfs(n-1, openParentheses+1)
            substring.pop()
        dfs(n, openParentheses)
        return ans

        