# Mathematical Models for Pegs Puzzle Solver

## Overview

This document describes the mathematical foundations and models used to solve the pegs puzzle using vector space theory and search algorithms.

## State Space Representation

### Vector Space Model

The pegs puzzle can be represented as a vector space where each board configuration is a vector in a high-dimensional space.

#### Definition

Let $S$ be the set of all possible board configurations. A board configuration $s \in S$ can be represented as:

$$s = (s_1, s_2, \ldots, s_n)$$

where $s_i \in \{0, 1\}$ represents the state of position $i$:
- $s_i = 1$: Peg present at position $i$
- $s_i = 0$: Empty hole at position $i$

For a standard $7 \times 7$ English peg solitaire board with 33 valid positions:

$$n = 33$$

### Vector Operations

#### Addition

The state transition can be modeled as vector addition:

$$s' = s + \Delta_m$$

where $\Delta_m$ is the transition vector representing move $m$:

$$\Delta_m = (-e_i) + (-e_j) + (e_k)$$

where:
- $e_i$: Unit vector at starting position
- $e_j$: Unit vector at jumped peg position  
- $e_k$: Unit vector at landing position

Example: For a move from position $(r_1, c_1)$ to $(r_2, c_2)$ over $(r_m, c_m)$:

$$\Delta_m = -\delta_{r_1,c_1} - \delta_{r_m,c_m} + \delta_{r_2,c_2}$$

where $\delta_{i,j}$ is the Kronecker delta function.

## Search Space as Graph

### Graph Theory Model

The state space forms a directed graph $G = (V, E)$ where:
- $V$: Set of all valid board configurations (vertices)
- $E$: Set of valid moves (edges)

### Properties

1. **Finite State Space**: $|V| = 2^{33} \approx 8.59 \times 10^9$ possible configurations
2. **Directed Edges**: Moves are reversible but with different transition vectors
3. **Acyclic Paths**: Shortest path from initial to goal state
4. **Branching Factor**: Varies by position (typically 2-4 moves per peg)

## Heuristic Function (A* Algorithm)

### Mathematical Definition

The heuristic function $h(s)$ estimates the cost to reach the goal from state $s$:

$$h(s) = \text{peg\_count}(s) - 1$$

### Admissibility Proof

For any state $s$, let $k$ be the minimum number of pegs to remove to reach the goal:

$$k \geq \text{peg\_count}(s) - 1$$

Since each move removes exactly one peg:

$$h(s) \leq h^*(s)$$

where $h^*(s)$ is the true minimum cost. Thus, the heuristic is admissible.

### Cost Function

For A*, the total cost function is:

$$f(s) = g(s) + h(s)$$

where:
- $g(s)$: Actual cost from initial state to $s$ (number of moves made)
- $h(s)$: Heuristic estimate from $s$ to goal
- $f(s)$: Estimated total cost

## BFS Mathematical Foundation

### Breadth-First Search Properties

BFS explores the state space level by level, guaranteeing the shortest path.

#### Time Complexity

$$O(b^d)$$

where:
- $b$: Average branching factor
- $d$: Depth of solution (number of moves)

#### Space Complexity

$$O(b^d)$$

For peg solitaire:
- Average branching factor: $\bar{b} \approx 3$
- Typical solution depth: $d \approx 15$
- Total states explored: $O(3^{15}) \approx 1.4 \times 10^7$

### Completeness

BFS is complete for finite state spaces. It will find a solution if one exists.

### Optimality

BFS is optimal - it finds the solution with minimum number of moves.

## A* Mathematical Foundation

### A* Properties

A* uses heuristic guidance to search more efficiently.

#### Time Complexity

$$O(b^d) \text{ in worst case, } O(b^{\epsilon d}) \text{ with good heuristic}$$

where $\epsilon < 1$ depends on heuristic quality.

#### Space Complexity

$$O(b^d)$$

### Optimality with Admissible Heuristic

Theorem: If $h(s)$ is admissible, A* is optimal.

Proof:
- Let $s^*$ be the optimal solution with cost $C^* = g(s^*)$
- At any point, A* expands the state with minimum $f(s) = g(s) + h(s)$
- Since $h(s) \leq h^*(s)$, $f(s) \leq g(s) + h^*(s) \leq C^*$
- Thus, A* never expands states with $f(s) > C^*$
- Therefore, A* always finds $s^*$

## State Representation as Matrix

### Matrix Formulation

The board can be represented as a matrix $B \in \{0, 1\}^{m \times n}$:

$$B = \begin{bmatrix}
b_{1,1} & b_{1,2} & \cdots & b_{1,n} \\
b_{2,1} & b_{2,2} & \cdots & b_{2,n} \\
\vdots & \vdots & \ddots & \vdots \\
b_{m,1} & b_{m,2} & \cdots & b_{m,n}
\end{bmatrix}$$

where $b_{i,j} = 1$ if position $(i,j)$ has a peg, $0$ otherwise.

### Move Operator

A move can be represented as a matrix operation:

$$B' = B + M_{r_1,c_1 \rightarrow r_2,c_2}$$

where the move matrix $M$ has:
- $M_{r_1,c_1} = -1$ (source position)
- $M_{r_m,c_m} = -1$ (jumped position)
- $M_{r_2,c_2} = +1$ (destination position)
- All other entries: 0

## Invariants and Parity

### Peg Parity

The peg solitaire puzzle has mathematical invariants that determine solvability.

#### Definition

Define the parity of a position as:

$$P(i,j) = \begin{cases}
1 & \text{if } i+j \text{ is even} \\
0 & \text{if } i+j \text{ is odd}
\end{cases}$$

#### Parity Invariant

Let $P_{\text{even}}$ be the number of pegs on even positions and $P_{\text{odd}}$ on odd positions.

For a solvable configuration:

$$|P_{\text{even}} - P_{\text{odd}}| \leq 1$$

### Proof of Invariant

Each move affects three positions with same parity sum:
- Starting position: one parity
- Jumped position: same parity (distance 1)
- Landing position: same parity (distance 2)

Thus, the difference $P_{\text{even}} - P_{\text{odd}}$ changes by $\pm 1$ or $0$.

## Complexity Analysis

### Theoretical Bounds

#### Upper Bound on Solution Length

For $n$ initial pegs, maximum moves:

$$\text{max\_moves} = n - 1$$

since each move removes exactly one peg.

#### State Space Size

For a board with $k$ valid positions:

$$|S| = 2^k$$

For English peg solitaire ($k=33$):

$$|S| = 2^{33} \approx 8.59 \times 10^9$$

#### Reachable States

Empirically, only a fraction of states are reachable:

$$|S_{\text{reachable}}| \approx 2.3 \times 10^7$$

## Algorithm Comparison

### Mathematical Comparison

| Property | BFS | A* |
|----------|-----|-----|
| Time Complexity | $O(b^d)$ | $O(b^d)$ worst case |
| Space Complexity | $O(b^d)$ | $O(b^d)$ |
| Optimality | Optimal | Optimal (with admissible heuristic) |
| Pruning | None | Heuristic-guided |
| Best Case | Solution at shallow depth | Heuristic close to actual cost |

### Practical Performance

For typical peg solitaire puzzles:
- BFS: Explores more states but guarantees shortest solution
- A*: Explores fewer states due to heuristic guidance

## Conclusion

The pegs puzzle solver combines:
1. **Vector space theory** for state representation
2. **Graph theory** for search space modeling
3. **Heuristic search** for efficient problem solving
4. **Mathematical invariants** for solvability analysis

The mathematical framework provides both theoretical guarantees (optimality, completeness) and practical efficiency (heuristic guidance, state space reduction).
