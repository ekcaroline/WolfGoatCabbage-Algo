# Wolf Goat Cabbage Problem Solver

## Description
This repository contains Python code to solve the classic problem of the Wolf Goat Cabbage puzzle using search algorithms.

## Problem Description
In the Wolf Goat Cabbage problem, a farmer must transport a wolf, a goat, and a cabbage across a river using a boat. However, the boat can only carry the farmer and one item at a time. Additionally, if the farmer leaves the wolf and the goat alone together, the wolf will eat the goat; likewise, if the goat and the cabbage are left alone together, the goat will eat the cabbage. The goal is to move all items from one side of the river to the other without any of the items being eaten.

## Implementation
The `WolfGoatCabbage` class in `search.py` provides functionality to define the problem, its initial state, goal state, actions, and how the state changes with each action. The class inherits from the `Problem` class provided in the `search` module.

### `__init__(self, initial, goal)`
- Initializes the problem with the initial state and goal state.

### `goal_test(self, state)`
- Returns `True` if the state is a goal state.

### `result(self, state, action)`
- Returns the state resulting from executing a given action in a given state.

### `actions(self, state)`
- Determines possible actions that can be taken from a given state.

## Running the Code
The main script in the repository demonstrates how to use the `WolfGoatCabbage` class to find solutions using depth-first and breadth-first graph search algorithms.

To run the code:
This will print the solutions obtained from both depth-first and breadth-first graph search algorithms.

## Example
```python
if __name__ == '__main__':
    wgc = WolfGoatCabbage()
    solution = depth_first_graph_search(wgc).solution()
    print(solution)
    solution = breadth_first_graph_search(wgc).solution()
    print(solution)
