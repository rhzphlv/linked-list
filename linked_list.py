class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class SinglyList():
    def __init__(self):
        self.head=None
        self.tail=None
        
    def add_val(self,val):
        if self.head == None:
            self.head=val
        else:
            self.tail.next=val
        self.tail=val
    
    def new_head(self,val):
        val.next=self.head
        self.head=val
        
    def change_index_value(self,index,val):
        i=0
        current=self.head
        while current:
            if index==i:
                current.value=val
                break
            current=current.next
            i+=1
            
    def remove_val(self,val):
        prev,current=self.head,self.head
        if current.value==val:
            self.head=current.next
            current=None
            return 
        while current!=None:
            if current.value==val:
                prev.next=current.next
                current=None
                return
            prev=current
            current=current.next
        return f"{val} not found!"
    
    def remove_by_index(self,index):
        current,prev=self.head,self.head
        i=0
        while current:
            if index==i:
                prev.next=current.next
                current=None
                return
            prev=current
            current=current.next
            i+=1
            
    def length(self):
        i=0
        current=self.head
        while current:
            i+=1
            current=current.next
        return i
    
    def get_index(self,num):
        i=0
        current=self.head
        while current!= None:
            if current.value == num:return i
            i+=1
            current=current.next
        return f"{num} not found!"
    
    def reverse(self,current=None,prev=None):
        if current==None:
            current=self.head
        if current.next==None:
            self.tail=self.head
            current.next=prev
            self.head=current
        else:
            next=current.next
            current.next=prev
            self.reverse(next,current)
    
    def add_after_value(self,node,val):
        current=self.head
        while current:
            if current.value==val:
                temp=current.next
                current.next=node
                node.next=temp
                temp=None
                return
            current=current.next
        return f"{val} not found!" 
    
    
    def __str__(self):
        linked_list=""
        current=self.head
        while current:
            linked_list+=str(current.value)+"->"
            current=current.next
        return linked_list[:-2]
