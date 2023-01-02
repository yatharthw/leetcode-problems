// naive method 
// count the number of nodes and then traverse till n-count nodes and delete the required element
struct ListNode* removeNthFromEnd(struct ListNode* head, int n){
    // counting the number of nodes
    int count = 1;
    struct ListNode *ptr = head;
    while (ptr->next != NULL) {
        count ++;
        ptr = ptr->next;
    }
    count = count - n;
    ptr = head;
    if (count <= 0)
        return head->next;
    while (count-- > 1) {
        ptr = ptr->next;
    }
    ptr->next = ptr->next->next;
    return head;
}
