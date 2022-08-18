class Solution {
public:
    bool canJump(vector<int>& nums) {
        int jumps=0;
        int current=0;
        int farthest=0;
        for(int i=0;i<nums.size();i++){
            farthest=max(farthest,nums[i]+i);
            if(i==current){
                current=farthest;
                jumps++;
                if(current>=nums.size()-1){
                    return true;
                }
            }
            
        }
         return false;
    }
};