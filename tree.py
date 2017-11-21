import Queue
class Tree():
    def __init__(self, data, parent=None):
        self.child = []
        self.data = data
        self.parent = parent
    def add(self, parent, child):
        q = Queue.Queue()          
        q.put(self)  
        while (q.empty() == False):
            node = q.get()
            if(node.data == parent):
                child = Tree(child, node)
                node.child.append(child)
            else:
                for chi in node.child:
                    q.put(chi)
    def delete(self, key):
        q = Queue.Queue()          
        q.put(self) 
        latest_sub = None 
        while (q.empty() == False):
            node = q.get()
            if(node.data == key):
                latest_sub = len(node.child)
                while node.parent != None:
                    parent = node.parent
                    for chi in parent.child:                        
                        if chi.data != key:
                          latest_sub += 1
                    node = parent
                break
            else:
                for chi in node.child:
                    q.put(chi)
        print latest_sub

def solve(n , q , nodes, t):  
    temp = t 
    for i in range(q):
        query = nodes[i]
        t.delete(query)   
           
n = input()
t = Tree(1)
for i in range(0,n-1):
    a,b = map(int, raw_input().split())
    t.add(a,b)

q = input()
nodes = range(q)
for i in range(0,q):
    nodes[i] = input()

solve(n ,q, nodes, t)
