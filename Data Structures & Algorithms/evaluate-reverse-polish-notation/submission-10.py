import math


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []

        for tok in tokens:
            if tok not in ['+', '-', '*', '/']:
                st.append(int(tok))
                continue
            
            b = st.pop()
            a = st.pop()

            if tok == '+':
                st.append(a + b)
            elif tok == '-':
                st.append(a - b)
            elif tok == '*':
                st.append(a * b)
            elif tok == '/':
                st.append(int(a / b))

        return st.pop()

            
            
            
