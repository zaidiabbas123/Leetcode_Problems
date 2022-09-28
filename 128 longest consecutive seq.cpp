class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        set<int> hashSet;
        if(nums.size()==1)return 1;
        if(nums.size()==0)return 0;
        int k=0;
        int max=1;
        int count=1;
        for(int n:nums){
            hashSet.insert(n);
        }
        set<int>::iterator itr;
        int crr=*hashSet.begin();
        for (itr = hashSet.begin();itr != hashSet.end(); itr++){
            if(hashSet.count(crr+1)){
                max+=1;
                crr+=1;
            }
            else{
                crr=*itr;
                max=1;
            }
            if(max>=count)count=max;
        }
        return count;
    }
};