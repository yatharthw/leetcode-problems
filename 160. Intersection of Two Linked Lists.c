/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode *getIntersectionNode(struct ListNode *headA, struct ListNode *headB) {
    struct ListNode *p1 = headA, *p2 = headB;
    int count1 = 1, count2 = 1, i = 0;
    while (p1->next != NULL)
    {
        p1 = p1->next;
        count1++;
    }
    while (p2->next != NULL)
    {
        p2 = p2->next;
        count2++;
    }
    p1 = headA;
    p2 = headB;
    if (count1 > count2)
    {
        for (i = 0; i < (count1 - count2); i++)
            p1 = p1->next;
    }
    else if (count1 < count2)
    {
        for (i = 0; i < (count2 - count1); i++)
            p2 = p2->next;
    }
    while (p1 != NULL)
    {
        if (p1 == p2)
            return p1;
        p1 = p1->next;
        p2 = p2->next;
    }
    return NULL;
}
