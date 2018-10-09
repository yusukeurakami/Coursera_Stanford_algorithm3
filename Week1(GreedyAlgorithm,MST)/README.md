# 1.Greedy Search Algorithm

```
This file describes a set of jobs with positive and integral weights and lengths. It has the format

[number_of_jobs]

[job_1_weight] [job_1_length]

[job_2_weight] [job_2_length]

...

For example, the third line of the file is "74 59", indicating that the second job has weight 74 and length 59.

You should NOT assume that edge weights or lengths are distinct.

Your task in this problem is to run the greedy algorithm that schedules jobs in decreasing order of the difference (weight - length). Recall from lecture that this algorithm is not always optimal. IMPORTANT: if two jobs have equal difference (weight - length), you should schedule the job with higher weight first. Beware: if you break ties in a different way, you are likely to get the wrong answer. You should report the sum of weighted completion times of the resulting schedule --- a positive integer --- in the box below.

```

## Approach
My first approach is to use the priority queue to sort the jobs in the decreasing value of cost 1.(weight - length) and 2.(weight/length).
However, I could not come up with the idea of how to sort the jobs according to the weight value when the cost is same.

Instead of the priority queue I ended up using the Python sorted() build-in function as follow.

``` python
def sort_diff(self):
    self.sorted_data = sorted(self.raw, key=lambda x: (x[0] - x[1], x[0]) , reverse=True)

def sort_frac(self):
    self.sorted_data = sorted(self.raw, key=lambda x: (float(x[0]) / x[1], x[0]) , reverse=True)
```

``` key=lambda x: operation(x)``` is the typical way to sort the element inside the array according to key value "operation(x)".
In this case, operation(x) has given by the tuple, so if the first element in the tuples are same, it will determine the order by the second element in the tuples.

Other then that, it is pretty straight forward.

# 2.Minimal Spanning Trees

```
This file describes an undirected graph with integer edge costs. It has the format

[number_of_nodes] [number_of_edges]

[one_node_of_edge_1] [other_node_of_edge_1] [edge_1_cost]

[one_node_of_edge_2] [other_node_of_edge_2] [edge_2_cost]

...

For example, the third line of the file is "2 3 -8874", indicating that there is an edge connecting vertex #2 and vertex #3 that has cost -8874.

You should NOT assume that edge costs are positive, nor should you assume that they are distinct.

Your task is to run Prim's minimum spanning tree algorithm on this graph. You should report the overall cost of a minimum spanning tree --- an integer, which may or may not be negative --- in the box below.

```

## Approach
I decided to use heap structure because it need to choose the minimal distanced neighbor for every iteration.
In the lecture, it describe that we have to update the key value every time I add the new node in "explored" list, but this is even simpler way exist.

```python
    while(len(explored) != self.node_n):
        # print("current_node: ",current_node.id)
        neighber = current_node.neighber
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
```

As you see in my code, I just add all the neighbor node into the heap no matter it is already in the heap.
So, how can I avoid visiting the same node twice? I just iteratively popped the new node until I got the node that has not been explored yet. Since a heap is keeping all of the possible minimum distanced neighbor, the first unexplored node that I pop-out from the heap is the next node I should visit.

Tricky part was the part when I make the adjacency list from the txt input. First time, I read the file in the way as if all the edges are directed edge (i.e. I only stored the a->b but not b->a). In order to make the complete adjacent list, I should've store the edges from the both ends.

```python
        for i, d in enumerate(data[1:]):
            adj_list[int(d[0])-1].neighber.append( [int(d[1]), int(d[2])] )         
            adj_list[int(d[1])-1].neighber.append( [int(d[0]), int(d[2])] )
            
```
