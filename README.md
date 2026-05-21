# Pegs Puzzle Solver

A peg solitaire solver implementing both BFS and A* algorithms.

## Requirements

```
pip install -r requirements.txt
```

## Usage

```bash
python main.py
```

## Board Format

The solver uses a numpy array where:
- `1` represents a peg
- `0` represents an empty hole

## Algorithms

### BFS (Breadth-First Search)
- Explores all states level by level
- Guarantees shortest path (minimum moves)
- Memory intensive for large state spaces

### A* (A-Star)
- Uses heuristic function (peg count - 1)
- More efficient than BFS for finding solutions
- May not find optimal solution

## Examples

### Simple Linear Board (3 pegs)
```
[[1 1 0]]
```
Solution: Move left peg to right position (1 move)

### Small Cross Board (10 pegs)
```
[[0 0 0 0 0]
 [0 1 1 1 0]
 [1 1 0 1 1]
 [0 1 1 1 0]
 [0 0 0 0 0]]
```

## Custom Boards

You can create custom boards by modifying the `create_cross_board()` function in `main.py`:

```python
board = np.array([
    [0, 1, 0],
    [1, 1, 1],
    [0, 1, 0]
])
```
