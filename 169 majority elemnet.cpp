class Solution {
public:
    int majorityElement(vector<int>& nums) {
        map<int,int> Map;
        for(int i=0;i<nums.size();i++){
            Map[nums[i]]++;
            
        }
        for(auto i:Map){
            if(i.second>nums.size()/2){
                return i.first;
            }
        }return -9999;
    }
};