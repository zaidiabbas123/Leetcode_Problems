/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode *detectCycle(ListNode *head) {
        map<ListNode*,int> Map;
        ListNode*p=head;
        int i=0;
        while(p){
            if(Map.find(p)!=Map.end())
            {
                return p;
            }
            else{
                Map[p]=i;
            }
            i+=1;
            p=p->next;
        }
        return NULL;
    }
};