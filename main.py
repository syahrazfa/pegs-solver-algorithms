import numpy as np
from pegs_solver import PegsSolver

def create_cross_board():
    board = np.zeros((5, 5), dtype=int)
    
    positions = [
        (1, 1), (1, 2), (1, 3),
        (2, 0), (2, 1), (2, 2), (2, 3), (2, 4),
        (3, 1), (3, 2), (3, 3)
    ]
    
    for pos in positions:
        board[pos] = 1
    
    board[2, 2] = 0
    
    return board

def main():
    board = create_cross_board()
    
    print("Initial board:")
    print(board)
    print(f"Initial peg count: {np.sum(board)}\n")
    
    solver = PegsSolver(board)
    
    print("Solving with BFS...")
    bfs_solution = solver.bfs(max_iterations=1000000)
    if bfs_solution:
        print(f"BFS solution found!")
        solver.print_solution(bfs_solution)
    else:
        print("BFS: No solution found")
    print()
    
    print("Solving with A*...")
    astar_solution = solver.a_star(max_iterations=1000000)
    if astar_solution:
        print(f"A* solution found!")
        solver.print_solution(astar_solution)
    else:
        print("A*: No solution found")

if __name__ == "__main__":
    main()
