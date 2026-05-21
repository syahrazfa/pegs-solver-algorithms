import numpy as np
from typing import List, Tuple, Set, Optional
from collections import deque
import heapq

class PegsState:
    def __init__(self, board: np.ndarray, moves: List[Tuple[int, int, int, int]] = None):
        self.board = board.copy()
        self.moves = moves if moves else []
        
    def __hash__(self):
        return hash(self.board.tobytes())
    
    def __eq__(self, other):
        return np.array_equal(self.board, other.board)
    
    def __lt__(self, other):
        return len(self.moves) < len(other.moves)
    
    def is_goal(self) -> bool:
        return np.sum(self.board) == 1
    
    def peg_count(self) -> int:
        return int(np.sum(self.board))
    
    def get_valid_moves(self) -> List[Tuple[int, int, int, int]]:
        moves = []
        rows, cols = self.board.shape
        
        for i in range(rows):
            for j in range(cols):
                if self.board[i, j] == 1:
                    for di, dj in [(-2, 0), (2, 0), (0, -2), (0, 2)]:
                        ni, nj = i + di, j + dj
                        mi, mj = i + di // 2, j + dj // 2
                        
                        if (0 <= ni < rows and 0 <= nj < cols and 
                            0 <= mi < rows and 0 <= mj < cols and
                            self.board[ni, nj] == 0 and 
                            self.board[mi, mj] == 1):
                            moves.append((i, j, ni, nj))
        
        return moves
    
    def apply_move(self, move: Tuple[int, int, int, int]) -> 'PegsState':
        i, j, ni, nj = move
        mi, mj = i + (ni - i) // 2, j + (nj - j) // 2
        
        new_board = self.board.copy()
        new_board[i, j] = 0
        new_board[mi, mj] = 0
        new_board[ni, nj] = 1
        
        new_moves = self.moves + [move]
        return PegsState(new_board, new_moves)
    
    def heuristic(self) -> int:
        return self.peg_count() - 1
    
    def __str__(self):
        return str(self.board)


class PegsSolver:
    def __init__(self, initial_board: np.ndarray):
        self.initial_state = PegsState(initial_board)
        self.rows, self.cols = initial_board.shape
        
    def bfs(self, max_iterations: int = 100000) -> Optional[PegsState]:
        visited = set()
        queue = deque([self.initial_state])
        
        iterations = 0
        while queue and iterations < max_iterations:
            iterations += 1
            current = queue.popleft()
            
            if current.is_goal():
                return current
            
            if current in visited:
                continue
            visited.add(current)
            
            for move in current.get_valid_moves():
                new_state = current.apply_move(move)
                if new_state not in visited:
                    queue.append(new_state)
        
        return None
    
    def a_star(self, max_iterations: int = 100000) -> Optional[PegsState]:
        visited = set()
        heap = []
        
        f_score = self.initial_state.heuristic()
        heapq.heappush(heap, (f_score, 0, self.initial_state))
        
        iterations = 0
        while heap and iterations < max_iterations:
            iterations += 1
            f, g, current = heapq.heappop(heap)
            
            if current.is_goal():
                return current
            
            if current in visited:
                continue
            visited.add(current)
            
            for move in current.get_valid_moves():
                new_state = current.apply_move(move)
                if new_state not in visited:
                    g_new = g + 1
                    h_new = new_state.heuristic()
                    f_new = g_new + h_new
                    heapq.heappush(heap, (f_new, g_new, new_state))
        
        return None
    
    def print_solution(self, solution: PegsState) -> None:
        if not solution:
            print("No solution found")
            return
        
        print(f"Solution found in {len(solution.moves)} moves:")
        for i, move in enumerate(solution.moves, 1):
            from_row, from_col, to_row, to_col = move
            print(f"{i}. Move peg from ({from_row}, {from_col}) to ({to_row}, {to_col})")
        
        print("\nFinal board:")
        print(solution.board)
