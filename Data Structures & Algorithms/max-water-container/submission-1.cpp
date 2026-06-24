class Solution {
public:
    int maxArea(vector<int>& heights) {

        int max_vol = 0;

        int l = 0, r = heights.size() - 1;

        while (l < r) {

            int cur_vol = (r - l) * min(heights[l], heights[r]);

            max_vol = max(max_vol, cur_vol);

            if (heights[l] < heights[r]) 
                ++l;
            else
                --r;
        }

        return max_vol;
        
    }
};
