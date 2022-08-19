class Solution {
public:
    bool isPossible(vector<int>& nums) {
        int n=nums.size();
        map<int,int> Map1,Map2;
        for(int i=0;i<n;i++){
            Map1[nums[i]]++;
        }
        
       for(auto i:nums){
           if(Map1[i]==0)
               continue;
            Map1[i]--;
            if(Map2[i-1]>0){
                Map2[i-1]--;
                Map2[i]++;
            }
            else if(Map1[i+1]!=0 && Map1[i+2]!=0){
                Map1[i+1]--;
                Map1[i+2]--;
                Map2[i+2]++;
            }
            else
                return false;
        }
        return true;
       }
};