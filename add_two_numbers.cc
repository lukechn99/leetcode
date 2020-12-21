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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* ptr1 = l1;
        ListNode* ptr2 = l2;
        ListNode* sum = new ListNode();
        ListNode* sumptr = sum;
        int carry_over = 0;
        while (ptr1 != nullptr && ptr2 != nullptr) {
            int step_sum = ptr1->val + ptr2->val + carry_over;
            // take the ones place value
            int ones_place = step_sum % 10;
            // taking tens place value
            carry_over = step_sum / 10;
            ListNode* new_node = new ListNode(ones_place);
            sumptr->next = new_node;
            sumptr = sumptr->next;
            // increment pointers
            ptr1 = ptr1->next;
            ptr2 = ptr2->next;
        }
        // cleanup
        while (ptr1 != nullptr) {
            int step_sum = ptr1->val + carry_over;
            // take the ones place value
            int ones_place = step_sum % 10;
            // taking tens place value
            ListNode* new_node = new ListNode(ones_place);
            sumptr->next = new_node;
            sumptr = sumptr->next;
            ptr1 = ptr1->next;
            carry_over = step_sum / 10;
        }
        while (ptr2 != nullptr) {
            int step_sum = ptr2->val + carry_over;
            // take the ones place value
            int ones_place = step_sum % 10;
            // taking tens place value
            ListNode* new_node = new ListNode(ones_place);
            sumptr->next = new_node;
            sumptr = sumptr->next;
            ptr2 = ptr2->next;
            carry_over = step_sum / 10;
        }
        if (carry_over > 0) {
            ListNode* new_node = new ListNode(carry_over);
            sumptr->next = new_node;
            sumptr = sumptr->next;
        }
        return sum->next;
    }
};
