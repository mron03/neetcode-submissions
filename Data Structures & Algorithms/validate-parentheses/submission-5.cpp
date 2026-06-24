class Solution {
public:
    bool isValid(string s) {
        stack<char> st;

        unordered_map<char, char> mapping = {
            {'{', '}'},
            {'(', ')'},
            {'[', ']'}
        };

        for (char c : s) {
            if (mapping.count(c)){
                st.push(c);
                continue;
            }

            if (st.empty() || mapping[st.top()] != c){
                return false;
            }

            st.pop();
        }

        if (st.empty() == false) return false;

        return true;
    }
};
