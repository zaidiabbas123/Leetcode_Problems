class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> vect;
        vector<int> temp;
        int l=nums.size();
        if(l<3)return{};
        else{
            vector<int>nums2(nums);
        set<vector<int> > set_of_vectors;
        sort(nums2.begin(),nums2.end());
        for(int i=0;i<nums2.size()-2;i++){
            int j=i+1;
            int k=l-1;
            while(j<k){
                if((nums2[j]+nums2[k])==(-nums2[i])){
                    if(set_of_vectors.insert({nums2[i],nums2[j],nums2[k]}).second){
                        vect.push_back({nums2[i],nums2[j],nums2[k]});
                    }
                    j++;
                    k--;
                    
                }
                else if((nums2[j]+nums2[k])<(-nums2[i])){
                    j++;
                }
                else{
                    k--;
                }
                
        }
        }
        }
        return vect;
    }
};