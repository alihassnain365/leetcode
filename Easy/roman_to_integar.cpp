// in this leetcode problem you are given a Roman numbers in the form of the string, 
// you have to convert those Roman strings to the integar numbers and return

class Solution {
public:
    int romanToInt(string s) {
        // creating the map 
        unordered_map <char,int> mp;
        mp['I'] = 1;
        mp['V'] = 5;
        mp['X'] = 10;
        mp['L'] = 50;
        mp['C'] = 100;
        mp['D'] = 500;
        mp['M'] = 1000;
        int sum = 0;

        for (int i = 0; i<=s.length()-1; i++)
        {
            if(mp[s[i]] < mp[s[i+1]])
            {
                sum -=  mp[s[i]];
            }
            else
            {
                sum += mp[s[i]];
            }
        } 
        return sum;
    }
    
};
