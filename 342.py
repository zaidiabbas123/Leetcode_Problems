class Solution {
public:
    bool isPowerOfFour(int n) {
        if(n==1){
            return true;
        }
        int d=0;
        while(n>4)
        {
            d=n%4;
            n=n/4;
            if(d!=0){
                return false;
            }
            
        }
        if(n==4){
            return true;
        }
        return false;
    }
};