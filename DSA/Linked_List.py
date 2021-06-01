class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def print_linked_list(self):
        curr_node = self.head
        while curr_node:
            print(curr_node.data)
            curr_node = curr_node.next
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head #so we can traverse the whole of the linked list
        while last_node.next: #while the node does not point to end of linked list (None)
            last_node = last_node.next
        last_node.next = new_node
    def insert_after_node(self,prev,data):
        if not prev: #prev could be None or does not exist
            print("Previous Node does not exist")
            return
        new_node = Node(data)
        new_node.next = prev.next
        prev.next = new_node
    def prepend(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    def delete_node(self,key): #key to check if head has this value or if other node has it
        curr = self.head
        if curr and curr.data == key:
            self.head = curr.next
            curr = None #essentially deleting it
            return 

        previous = None
        #curr is now the node to be deleted
        while curr and curr.data != key: #could break if node's key is None (does not exist) or if we have found node with the key
            previous = curr
            curr = curr.next
        #curr should now hold the node to be deleted
        if curr is None:
            return 
        previous.next = curr.next #like (want to be deleted b) a->b->c where a.next is b but should then point to c which is just curr.next
        curr = None
    def delete_node_pos(self,pos):
        if self.head: #if linked list is not empty
            curr = self.head
            if pos == 0: #if we want to delete head of the array
                self.head = curr.next
                curr = None
                return
            prev = None
            count = 0
            while curr and count!=pos:
                prev = curr
                curr = curr.next
                count+=1
            if curr is None: #indeterminate loop above may stop if we have traversed the whole of the linked list
                return 
            #condition above ensures that loop will have terminated because we have found the element at the desired position
            prev.next = curr.next
            curr = None
    def len_iteratively(self):
        curr = self.head
        count=0
        while curr:
            curr = curr.next
            count+=1
        return count 
    def len_recursively(self,node):
        if node is None:
            return 0
        else:
            return 1+self.len_recursively(node.next)
    def swap_nodes(self, key_1, key_2):
        if key_1==key_2:
            return 
        prev_1 = None
        curr_1 = self.head
        while curr_1 and curr_1.data != key_1:
            prev_1 = curr_1
            curr_1 = curr_1.next
        prev_2 = None
        curr_2 = self.head
        while curr_2 and curr_2.data != key_2:
            prev_2 = curr_2
            curr_2 = curr_2.next
        if not curr_1 or not curr_2: # if all of the nodes do not have both of the keys then swapping cannot happen
            return 
        if prev_1:
            prev_1.next = curr_2
        else: #if prev_1 is None then curr_1 has to be the head of linked list
            self.head = curr_2
        if prev_2:
            prev_2.next = curr_1
        else:#if prev_2 is None then curr_2 has to be the head of linked list
            self.head = curr_1
        curr_1.next,curr_2.next = curr_2.next,curr_1.next #after swapping the previous nodes and the actual nodes we have to swap nodes' nexts
    def reverse_iteratively(self):
        prev = None
        curr = self.head
        while curr:
            next_node = curr.next #temporary
            curr.next = prev #pointers or the arrows flip here 
            prev = curr
            curr = next_node
        #prev is the last node in the list 
        self.head = prev
        #Below is a visualisation that really helped me (got confused with how curr.next = prev actually refers to the pointer and not the value)
        '''
        A->b->c->d
        A<-b->c->d
        A<-b<-c->d
        A<-b<-c<-d	
        '''
    def reverse_recursively(self):
        def _reverse_recursively(curr,prev): #a helper method
            if not curr: #base case for the recursion to occur
                return prev #is triggered when we reach end of linked list and have to return the last node (prev)
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
            return _reverse_recursively(curr,prev)
        #below call will always return prev (last node of llist or the head of the reversed llist)
        self.head = _reverse_recursively(curr=self.head,prev=None)
    def remove_duplicates(self):
        curr = self.head
        prev = None
        dupl_values = dict()

        while curr:
            if curr.data in dupl_values:
                prev.next = curr.next
                curr = None
            else: #element not a key in our reference dict
                dupl_values[curr.data] = 1
                prev = curr
            curr = prev.next #helps go to next node even if we have just removed a duplicate node 
    def print_nth_from_last(self,n,method):
        if method==1:
            total_len = self.len_iteratively()
            curr = self.head
            while curr:
                if total_len == n:
                    print(curr.data)
                    return curr.data
                total_len -=1
                curr = curr.next
            if curr is None: #empty linked list or total_len never equal to n 
                return 
        elif method==2:
            p = self.head
            q = self.head 

            if n>0:
                count = 0
                while q:
                    count+=1
                    if count>=n:
                        break
                    q = q.next
                if not q:
                    print(n," is greater than the number of nodes in list hence I cannot print",n,"nodes from the end of the list")
                    return
                while p and q.next: #picture a list of size 6 and so q would be at 3rd node whereas p at head (when q gets to end, p should be at the desired node)
                    p = p.next
                    q = q.next 
                return p.data 
            else:
                return None   
#Driver code
# linked = LinkedList()
# linked.append('Shakeel')
# linked.append('Majeed')
# linked.prepend(2021)
# linked.insert_after_node(linked.head.next,"India")
# linked.delete_node('Majeed')
# linked.print_linked_list()
# linked.delete_node_pos(0)
# linked.print_linked_list()
# linked.swap_nodes("Shakeel","India")
# linked.print_linked_list()
# print('------')
# linked.reverse_iteratively()
# linked.print_linked_list()
# print('------')
# linked.reverse_recursively()
# linked.print_linked_list()
# print('------')
# print(linked.len_iteratively())
# print(linked.len_recursively(linked.head))


