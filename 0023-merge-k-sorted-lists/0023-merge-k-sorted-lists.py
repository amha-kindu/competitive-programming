# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeList(self, list1, list2):
        if not list1:
            return list2
        if not list2:
            return list1
        if list1.val < list2.val:
            list1.next = self.mergeList(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeList(list1, list2.next)
            return list2
        
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return
        if len(lists) == 1:
            return lists[0]
        
        last  = lists.pop()
        last2 = lists.pop()
        
        lists.append( self.mergeList(last, last2) )
        
        return self.mergeKLists(lists)
        