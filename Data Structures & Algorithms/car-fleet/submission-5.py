class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        # 10 - 4 = 6  / 2 = 3
        # 10 - 1 = 9 / 2 = 4.5
        # 10 - 0 = 10 / 1 = 10
        # 10 - 7 = 3 / 1 = 3


        # [1, 2, 2, 1]

        # 7   4   1 0


        # (7 - 4 + x) = 2x
        # 3 = x

        # if 4 + 3*2 > target: 
        #     7, 4

        # else:
        #     4

        mapp = {k:v for k, v in zip(position, speed)}
        position.sort(reverse=True)
        st = []


        for cur in position:
            if len(st) == 0:
                st.append(cur)
                continue

            top = st[-1]

            if mapp[top] >= mapp[cur]:
                st.append(cur)
                continue
 
            top_time = (target - top) / mapp[top]
            cur_time = (target - cur) / mapp[cur]

            if top_time < cur_time:
                st.append(cur)


        return len(st)            

