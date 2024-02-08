# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ## Recursive Solusion

        if list1 == None: 
            return list2
        if list2 == None: 
            return list1 

        if list1.val < list2.val: 
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else: 
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2

        ## Normal Solusion
        '''
        temp_list = ListNode()
        temp_tail = temp_list 

        while list1 and list2: 
            if list1.val > list2.val: 
                temp_tail.next = list2
                list2 = list2.next
            else: 
                temp_tail.next = list1
                list1 = list1.next

            temp_tail = temp_tail.next #update the temp tail as well

        if list1: # if it is not null 
            temp_tail.next = list1
        if list2: # if it is not null 
            temp_tail.next = list2

        return temp_list.next
        '''

        