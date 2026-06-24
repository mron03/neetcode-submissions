class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        st = [0]

        res = [0] * len(temperatures)


        for i in range(1, len(temperatures)):

            while st and temperatures[st[-1]] < temperatures[i]:

                res[st[-1]] = i - st[-1]

                st.pop()

            st.append(i)

        
        
        return [r if r is not None else 0 for r in res]





        