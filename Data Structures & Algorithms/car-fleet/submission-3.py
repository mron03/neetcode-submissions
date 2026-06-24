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

        print(position)

        for p in position:
            print(st)
            if len(st) == 0:
                st.append(p)
                continue

            top_pos = st[-1]

            if mapp[top_pos] >= mapp[p]:
                st.append(p)
                continue
 
            x = (top_pos - p) / (mapp[p] - mapp[top_pos])
            print(top_pos, p, x)

            if p + x * mapp[p] > target:
                st.append(p)


        return len(st)            

