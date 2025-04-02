'''
Created on Apr 1, 2025

@author: bigcv
'''
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
class Solution: 
    def insert(self,head,data):
            p = Node(data)           
            if head==None:
                head=p
            elif head.next==None:
                head.next=p
            else:
                start=head
                while(start.next!=None):
                    start=start.next
                start.next=p
            return head  
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def removeDuplicates(self, head):
        s = set()
        cur = head
        if cur is not None:
            s.add(cur.data)
            while cur.next:
                if cur.next.data in s:
                    cur.next = cur.next.next
                else:
                    s.add(cur.next.data)
                    cur = cur.next
        return head
                

mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data) 
mylist.display(head);
print("\n")   
head=mylist.removeDuplicates(head)
mylist.display(head); 