class Solution {
public:
    void sortColors(vector<int>& nums) {
        int c0=0;
        int c1=0;
        int c2=0;
        vector<int> vect(nums);
        int l=vect.size();
        for(int i=0;i<l;i++)
        {
            if(vect[i]==0){
                c0++;
            }
            else if(vect[i]==1){
                c1++;
            }
            else{
                c2++;
            }
        }
        for(int i=0;i<c0;i++){
            nums[i]=0;
        }
        for(int i=c0;i<c1+c0;i++){
            nums[i]=1;
        }
        for(int i=c0+c1;i<c0+c2+c1;i++){
            nums[i]=2;
        }
        
    }
};