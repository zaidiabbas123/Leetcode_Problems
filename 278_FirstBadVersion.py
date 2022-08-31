// The API isBadVersion is defined for you.
// bool isBadVersion(int version);

class Solution {
public:
    int firstBadVersion(int n) {
        int a=n/2;
        if(isBadVersion(a)==true)
        {
            for(int i=1;i<=a;i++){
                if(isBadVersion(i)){
                    return i;
                }
            }
        }
        else{
             for(int i=a;i<=n;i++){
                if(isBadVersion(i)){
                    return i;
                }
            }
        }
        return 0;
    }
};