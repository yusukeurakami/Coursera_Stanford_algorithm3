from heapq import heappush, heappop
import itertools

class MST_solver():
    def __init__(self):
        self.node_n = 0
        self.edges_n = 0
        self.adj_list = None

    def adj_list_maker(self):
        files = open('edges.txt')
        lines = files.readlines()
        data = [x.strip('\n').split(' ') for x in lines]
        self.node_n = int(data[0][0])
        self.edges_n = int(data[0][1])

        adj_list = [None] * self.node_n
        for i in range(self.node_n):
            node = Node(i+1)
            adj_list[i] = node
        
        for i, d in enumerate(data[1:]):
            adj_list[int(d[0])-1].neighber.append( [int(d[1]), int(d[2])] )
            adj_list[int(d[1])-1].neighber.append( [int(d[0]), int(d[2])] )
        self.adj_list = adj_list

    def MST(self,current_node):
        explored = []
        tree_cost = 0
        heap = Heap()

        explored.append(current_node)

        while(len(explored) != self.node_n):
            # print("current_node: ",current_node.id)
            neighber = current_node.neighber #neighber is list that elements like [dist_node, cost]
            for adj_node in neighber:
                heap.add_task(self.adj_list[adj_node[0]-1], adj_node[1])

            closest_node, cost = heap.pop_task()
            while(closest_node in explored):
                if len(heap.pq) == 0:
                    break
                closest_node, cost = heap.pop_task()
            # print(closest_node.id, cost)

            tree_cost += cost
            current_node = closest_node
            explored.append(current_node)
            
        return tree_cost

class Node():
    def __init__(self, id):
        self.id = id
        self.neighber = []

class Heap():
    def __init__(self):
        self.pq = []    
 
    def add_task(self, task, priority):
        entry = [priority, task]
        heappush(self.pq, entry)

    def pop_task(self):
        priority, task = heappop(self.pq)
        return task, priority

if __name__ == "__main__":
    mst = MST_solver()
    mst.adj_list_maker()
    # for i in range(mst.node_n):
    #     print(mst.adj_list[i].id, ": " ,mst.adj_list[i].neighber)
    print(mst.MST(mst.adj_list[0]))
    

