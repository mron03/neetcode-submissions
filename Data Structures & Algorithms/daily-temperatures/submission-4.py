class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        st = []
        res = [0] * len(temperatures)


        for i, t in enumerate(temperatures):
            while st and temperatures[st[-1]] < t:

                res[st[-1]] = i - st[-1]

                st.pop()

            st.append(i)

        
        
        return res





        