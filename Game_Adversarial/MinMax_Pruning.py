import math
import random

def minimax(depth, nodeIndex, isMaximizingPlayer, values, maxDepth):
    if depth == maxDepth:
        print(f"Leaf node reached at depth {depth}, returning value: {values[nodeIndex]}")
        return values[nodeIndex]

    if isMaximizingPlayer:
        best = -math.inf
        print(f"\nMaximizer at depth {depth}")
        print("====================================================================================")

        for i in range(2):
            value = minimax(depth + 1, nodeIndex * 2 + i, False, values, maxDepth)
            print(f"Maximizer at depth {depth}, comparing value: {value} with best: {best}")
            best = max(best, value)

        print(f"Maximizer at depth {depth}, selected best: {best}")
        print("====================================================================================")
        return best
    else:
        best = math.inf
        print(f"\nMinimizer at depth {depth}")
        print("====================================================================================")

        for i in range(2):
            value = minimax(depth + 1, nodeIndex * 2 + i, True, values, maxDepth)
            print(f"Minimizer at depth {depth}, comparing value: {value} with best: {best}")
            best = min(best, value)

        print(f"Minimizer at depth {depth}, selected best: {best}")
        return best

def main():
    # Get user input for maximum depth
    maxDepth = int(input("Enter the maximum depth of the game tree: "))
    
    # Generate random leaf node values
    num_leaf_nodes = 2 ** maxDepth
    values = [random.randint(-10, 10) for _ in range(num_leaf_nodes)]
    
    print(f"Generated leaf node values: {values}\n")

    optimalValue = minimax(0, 0, True, values, maxDepth)

    print("====================================================================================")
    print("The optimal value is:", optimalValue)
    print("====================================================================================")

if __name__ == "__main__":
    main()
