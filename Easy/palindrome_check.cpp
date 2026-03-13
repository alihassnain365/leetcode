class Solution {
public:
    bool isPalindrome(int x) { 
        if (x == 0) return true;
        if(x<0 or x %10 == 0) return false;
        // now doin the number reverse
        long int reversed = 0;
        long int num = x;
        while (x >0)
        {
            long int temp = x % 10 ;
            x = x / 10;
            reversed = reversed*10 + temp;

        }
        if(reversed == num) return true;
        else return false;
        
    }
};
