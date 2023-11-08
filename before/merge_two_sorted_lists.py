from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# def solution(
#     list1: Optional[ListNode], list2: Optional[ListNode]
# ) -> Optional[ListNode]:
#     if not list1:
#         return list2
#     if not list2:
#         return list1

#     # order the lists
#     list1, list2 = (
#         list1,
#         list2 if list1.val <= list2.val else list2,
#         list1,
#     )

#     # save the head so that we can return the final list
#     head = list1

#     # we will use list1 as the 'main' list, since its head is less than list2
#     # we take a look at the head of list2,
#     #   either attach it right after the list1 current node,
#     #   or compare it to the next list1 node

#     # we will iterate and compare on list1 and list2,
#     #   which refer to the current nodes in the respective lists

#     while list2.next:
#         # compare list1 and list2
#         if list1.val < list2.val:
#             list1 = list1.next # we move on
#         else:
#             # insert list2 into list1
#             temp = list2
#             list2 = list2.next
#             temp.next = list1.next
#             list1.next = temp

#     # last list2 node left
#     if list1.val < list2.val:
#         # insert list2 after
#         list2.next = list1.next
#         list1.next = list2
#     else:
#         # insert list2 before

#         pass

#     return head

def solution(
    list1: Optional[ListNode], list2: Optional[ListNode]
) -> Optional[ListNode]:
    if not list1:
        return list2
    if not list2:
        return list1

    cur = None
    head = cur

    while True:
        if list1.val < list2.val:
            cur.next = list1
            list1 = list1.next
        else:
            cur.next = list2
            list2 = list2.next

        if not list1.next:
            if list2.next:
                cur.next = list2
            break
        if not list2.next:
            if list1.next:
                cur.next = list1
            break
    return head.next
