class Patient:
    def __init__(self, p_id = None, p_type = None, prev = None, next =None):
        self.p_id = p_id
        self.p_type = p_type
        self.prev = prev
        self.next = next

class Hospital:
    def __init__(self):
        # dummy nodes for convinince
        self.head = Patient()
        self.tail = Patient()

        self.head.next = self.tail
        self.tail.prev = self.head

        # dictionay for saving records, 
        # {id: Node}
        self.di = {}

# required features
# --------------------------------------------------
    def visit(self, p_id, p_type):
        np = Patient(p_id, p_type)
        emg = np.p_type == 'Emergency'

        if emg:
            self.addFront(np)
        else:
            self.addBack(np)
    
    # ------------------------
    def cancel(self, p_id):
        print(self.delete(p_id))

    # ------------------------
    def treated(self, k):
        try:
            cur = self.head.next
            for _ in range(k):
                if cur == self.tail:
                    print("No more patient to treat...")
                    break
                nxtNode = cur.next
                print(self.delete(cur.p_id))
                cur = nxtNode

        except(Exception) as err:
            print("error treating patient", err)

    # ------------------------
    def details(self, p_id):
        print(self.di[p_id])



# utility functions
# ---------------------------------------------------
    def addFront(self, node):
        try:
            self.di[node.p_id] = node
            
            node.next = self.head.next
            self.head.next.prev = node
            node.prev = self.head
            self.head.next = node

        except(Exception) as err:
            print(f"error adding node {node.p_id} at back", err)

        print(f"sucessfuly added {node.p_id} in front")



    def addBack(self, node):
        try:
            self.di[node.p_id] = node

            node.next = self.tail
            self.tail.prev.next = node
            node.prev = self.tail.prev
            self.tail.prev = node

        except(Exception) as err:
            print(f"error adding node {node.p_id} at back", err)

        print(f"sucessfuly added {node.p_id} in Back")


    def delete(self, p_id):
        node = self.di[p_id]
        try:
            del self.di[p_id]
            node.prev.next =  node.next      
            node.next.prev =  node.prev   
            node.prev = None   
            node.next = None 
                
        except(Exception) as err:
            print("error deleting node...", err)
        print(f"node {p_id} has been deleted sucessfully")
        return node

