import numpy as np
from pegs_solver import PegsState, PegsSolver

def test_linear_board():
    """Test simple linear board that is solvable in 1 move"""
    board = np.array([[1, 1, 0]])
    print("=== Linear Board (3 pegs) ===")
    print("Board:", board)
    
    solver = PegsSolver(board)
    solution = solver.bfs(max_iterations=1000)
    if solution:
        print("✓ BFS Solution found in", len(solution.moves), "moves")
        solver.print_solution(solution)
    else:
        print("✗ No solution found")
    print()

def test_4_peg_linear():
    """Test 4 pegs in a line - this should be solvable"""
    board = np.array([[1, 1, 1, 1, 0]])
    print("=== 5-Peg Linear Board ===")
    print("Board:", board)
    
    state = PegsState(board)
    print("Valid moves:", state.get_valid_moves())
    
    solver = PegsSolver(board)
    solution = solver.bfs(max_iterations=5000)
    if solution:
        print("✓ BFS Solution found in", len(solution.moves), "moves")
        solver.print_solution(solution)
    else:
        print("✗ No solution found")
    print()

def test_simple_cross():
    """Test small cross configuration"""
    board = np.zeros((5, 5), dtype=int)
    positions = [
        (1, 1), (1, 2), (1, 3),
        (2, 1), (2, 2), (2, 3),
        (3, 1), (3, 2), (3, 3)
    ]
    for pos in positions:
        board[pos] = 1
    board[2, 2] = 0
    
    print("=== Simple Cross (9 pegs) ===")
    print(board)
    print("Peg count:", np.sum(board))
    
    solver = PegsSolver(board)
    solution = solver.bfs(max_iterations=50000)
    if solution:
        print("✓ BFS Solution found in", len(solution.moves), "moves")
        solver.print_solution(solution)
    else:
        print("✗ No solution found")
    print()

def test_astar_on_linear():
    """Test A* on simple linear board"""
    board = np.array([[1, 1, 1, 1, 0]])
    print("=== A* on 5-Peg Linear ===")
    print("Board:", board)
    
    solver = PegsSolver(board)
    solution = solver.a_star(max_iterations=5000)
    if solution:
        print("✓ A* Solution found in", len(solution.moves), "moves")
        solver.print_solution(solution)
    else:
        print("✗ No solution found")
    print()

def main():
    test_linear_board()
    test_4_peg_linear()
    test_simple_cross()
    test_astar_on_linear()

if __name__ == "__main__":
    main()
