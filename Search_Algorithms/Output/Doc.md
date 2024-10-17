# **Search Algorithms**

## **Introduction**
This repo contains 12 different search algorithms, each designed to explore and find paths in a weighted graph. The graph represents nodes as points and edges as connections with specific weights (costs). 

## **Graph Used**
The graph is represented as a set of nodes and edges, where each node has a specific position (X, Y) and each edge has a weight (cost). The graph is bidirectional, meaning paths can be traversed in both directions between nodes.

Here is a visual representation of the graph used:
![Graph]("Search_Algorithms/metaData/tree_visualization.png")

### **Metadata Used**

- **`node_positions.csv`**: Contains the node number and its respective coordinates on the graph.
  - Columns: `Node`, `X`, `Y`
  
- **`path_details.csv`**: Contains the paths between nodes and their associated weights.
  - Columns: `Source Node`, `Target Node`, `Weight`

---

## **Algorithms**

### **1. British Museum Search**
The British Museum Search performs an exhaustive, unstructured search. It explores all possible paths randomly without any specific direction or priority. This algorithm is generally inefficient but guarantees finding a solution if one exists.

**Output**
![Output]("BMS.png")

---

### **2. Depth First Search (DFS)**
Depth First Search explores as far down a path as possible before backtracking. It uses a stack (or recursion) to maintain the current path, making it suitable for deep but not necessarily optimal exploration. DFS does not guarantee the shortest path.

**Output**
![Output]("DFS.png")

---

### **3. Breadth First Search (BFS)**
Breadth First Search explores all neighbors at the present depth level before moving to nodes at the next depth level. It guarantees finding the shortest path in an unweighted graph, but in a weighted graph, BFS may still find suboptimal solutions unless combined with other strategies.

**Output**
![Output]("BFS.png")

---

### **4. Hill Climbing**
Hill Climbing is an informed search algorithm that always chooses the next step based on which neighbor is closest to the goal. It doesn't backtrack, which means it can get stuck in local optima, making it less reliable for complex search spaces.

**Output**
![Output]("HillClimbing.png")

---

### **5. Beam Search**
Beam Search is a variant of breadth-first search but limits the number of nodes stored at each level by selecting the best `k` nodes based on a heuristic. This reduces memory requirements but sacrifices completeness.

**Output**
![Output]("BeamSearch.png")

---

### **6. Oracle**
Oracle Search simulates having prior knowledge about the optimal path, making it an idealized version of a search algorithm. It's mainly theoretical but helps analyze other methods by providing a baseline for optimal performance.

**Output**
![Output]("Oracle.png")

---

### **7. Branch and Binde**
Branch and Binde performs a systematic search by exploring all possible branches, but it stops and eliminates branches that are not promising based on some evaluation. This algorithm guarantees an optimal solution but can be slow.

**Output**
![Output]("Branch_and_Bound.png")

---

### **8. Dead Horse**
The Dead Horse search is a brute force method that revisits nodes without much strategy, leading to redundant exploration of paths. It stops when no more progress can be made, essentially exhausting the search.

**Output**
![Output]("DH.png")

---

### **9. Branch and Bound + Cost + Estimate**
Branch and Bound + Cost + Estimate combines the traditional branch and bound approach with heuristic estimates to make decisions more efficient. It evaluates the total cost of reaching the goal, pruning suboptimal paths early.

**Output**
![Output]("BB_Cost_Est.png")

---

### **10. A* Algorithm**
A* is an informed search algorithm that uses both the actual cost from the start and an estimate (heuristic) of the remaining cost to the goal. It guarantees finding the optimal path, making it one of the most efficient and widely used search algorithms.

**Output**
![Output]("A_Star.png")

---

### **11. AO\*** Algorithm
AO* is used in graphs with multiple sub-goals. It evaluates and expands nodes by considering their direct neighbors and optimizes for an overall solution with minimal cost. It is ideal for hierarchical and decomposable problems.

**Output**
![Output](Search_Algorithms/Output/A_Star.png)

---

### **12. Best First Search**
Best First Search prioritizes the node that appears to be closest to the goal according to a heuristic. It does not always guarantee an optimal path but is efficient in scenarios where an approximate solution is acceptable.

**Output**
![Output]("BestFirstSearch.png")



