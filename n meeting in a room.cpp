//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends
class Solution
{
    public:
    //Function to find the maximum number of meetings that can
    //be performed in a meeting room.
    int maxMeetings(int start[], int end[], int n)
    {
        int count=0;
        int a;
        int startv[n];
        vector<pair<int,int>> vect;
        for(int i=0;i<n;i++){
            pair<int,int>p;
            p.first=end[i];
            p.second=i;
            vect.push_back(p);
        }
        sort(vect.begin(),vect.end());
        for(int i=0;i<n;i++){
            end[i]=vect[i].first;
            a=vect[i].second;
            startv[i]=start[a];
        }
        int end_limit=0;
        for(int i=0;i<n;i++){
            if(startv[i]>end_limit){
                count++;
                end_limit=end[i];
            }
        }
        // Your code here
        return count;
    }
};

//{ Driver Code Starts.
int main() {
    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;
        int start[n], end[n];
        for (int i = 0; i < n; i++) cin >> start[i];

        for (int i = 0; i < n; i++) cin >> end[i];

        Solution ob;
        int ans = ob.maxMeetings(start, end, n);
        cout << ans << endl;
    }
    return 0;
}
// } Driver Code Ends