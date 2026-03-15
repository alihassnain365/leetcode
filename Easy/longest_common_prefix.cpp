class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        // string arr is empty
        if (strs.empty()) return "";
        if (strs.size()==1) return strs[0];
        string common;
        common = strs[0];
        for (int i = 1; i<strs.size(); i++)
        {
            char ch;
            int count = 0;
            string to_check = strs[i];
            if (to_check.size() < common.size()) common.resize(to_check.size());
            while(count<to_check.size())
            {
                if(to_check[count]==common[count])
                {
                    count++;
                    continue;
                }
                else
                {
                    common.resize(count);
                    break;
                }
            }
        }
        return common;
        
    }
};
