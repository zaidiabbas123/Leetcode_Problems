/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* deleteDuplicates(ListNode* head) {
        if(!head)return head;
        ListNode* pseudo=new ListNode(0);
        pseudo->next=head;
        ListNode*itr=pseudo;
        while(itr->next&&itr->next->next){
            if(itr->next->val==itr->next->next->val){
                int var=itr->next->val;
                while(itr->next->val==val&& itr->next!=NULL){
                    itr->next=itr->next->next;
                }
            }
            else{
                itr=itr->next;
            }
        }
        return pseudo->next;
    }
};