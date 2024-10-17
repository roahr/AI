
# Minimax Algorithm with Alpha-Beta Pruning

## 1. Introduction

The **Minimax Algorithm** is used in game theory to simulate decision-making in a two-player game. The algorithm assumes that both players play optimally. The **maximizer** aims to maximize their score, while the **minimizer** aims to minimize the maximizer's score. 

**Alpha-Beta Pruning** is an optimization technique for the Minimax algorithm, allowing the algorithm to disregard branches of the tree that won't influence the final decision, thereby reducing the number of nodes evaluated and improving efficiency.

## 2. Algorithm Explanation

### 2.1 Minimax Algorithm

The Minimax algorithm explores all possible moves in a game tree and alternates between two players:
- **Maximizing Player**: Tries to select the highest possible value.
- **Minimizing Player**: Tries to select the lowest possible value.

The algorithm recursively explores all game outcomes, selecting the optimal value for the current player at each level of the tree.

### 2.2 Alpha-Beta Pruning

In a game tree search, **alpha** and **beta** are values used to determine when pruning can occur:
- **Alpha**: The best option (maximum) found so far for the maximizer.
- **Beta**: The best option (minimum) found so far for the minimizer.

When the minimizer's best move is worse than the maximizer's current option (`beta <= alpha`), the algorithm **prunes** that branch, avoiding unnecessary exploration.

## 3. Features of Alpha-Beta Pruning

1. **Pruning:** Alpha-beta pruning reduces the number of nodes explored in the search tree.
2. **Alpha (Maximizer's best choice):** The maximum lower bound for the maximizer.
3. **Beta (Minimizer's best choice):** The minimum upper bound for the minimizer.
4. **Efficiency:** Alpha-Beta pruning improves the search efficiency and reduces computational load by pruning branches that won't affect the outcome.

## 4. Example Output

### Test Case 1
- **Tree Depth**: 4
- **Leaf Node Values**: [4, 9, -2, -8, -10, 10, -4, -4, 3, 7, 3, 7, 7, 5, -2, -1]
- **Output:**
```
The optimal value is: 7
```
### Test Case 2
- **Tree Depth**: 3
- **Leaf Node Values**: [-9, -7, 8, 6, 6, -9, 9, -5]
- **Output:**
```
The optimal value is: 8
```

### Test Case 3
- **Tree Depth**: 4
- **Leaf Node Values**: [9, -4, 4, 0, -6, 1, -9, 9, 5, -5, -9, -7, -6, -9, -6, 10]
- **Output:**
```
The optimal value is: 5
```
