class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        map<int ,int> Map;
        for(int i=0;i<nums.size();i++){
            Map[nums[i]]++;
            
        }
        for(auto i:Map){
            if(i.second>=2){
                return i.first;
            }
        }return 0;
    }
};