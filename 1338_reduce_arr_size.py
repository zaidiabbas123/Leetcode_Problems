class Solution {
public:
    int minSetSize(vector<int>& arr) {
       map<int,int> Map;
       
        int count=0;
        int half=arr.size()/2;
       for(int i=0;i<arr.size();i++){
           Map[arr[i]]++;
           
       }
       int n=arr.size();
       multimap<int ,int,greater<int>>mm;
        for(auto it:Map){
            mm.insert({it.second,it.first});
        }
        int sum=n;
        
        for( auto it=mm.begin();it!=mm.end();it++){
            sum-=it->first;
            count++;
            if(sum<=n/2){
                return count;
            }
        }
        return count;
    }
};