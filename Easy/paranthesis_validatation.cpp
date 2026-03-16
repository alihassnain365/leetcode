class Solution {
public:
    bool isValid(string s) {
        if (s.length() % 2 != 0) return false;

        unordered_map<char, char> mp;
        mp['('] = ')';
        mp['{'] = '}';
        mp['['] = ']';

        // Manual stack (using new)
        char* stack = new char[s.length()];
        int topStack = -1;

        for (int i = 0; i < s.length(); i++) {
            char current = s[i];

            // 1. Check if it's an opening bracket (Fixed the ']')
            if (current == '(' || current == '{' || current == '[') {
                topStack++;
                stack[topStack] = current;
            } 
            else {
                // 2. If we see a closing bracket but stack is empty, it's invalid
                if (topStack == -1) {
                    delete[] stack; // Clean up memory!
                    return false;
                }

                // 3. Check if the closing bracket matches the top of stack
                if (mp[stack[topStack]] == current) {
                    topStack--;
                } else {
                    delete[] stack; // Clean up memory!
                    return false;
                }
            }
        }

        bool result = (topStack == -1);
        delete[] stack; // Don't forget to free the memory!
        return result;
    }
};
