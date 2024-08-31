import concurrent.futures
import time


def is_safe(board, row, col):
    for i in range(col):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, len(board)), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_n_queens_util(board, col):
    if col >= len(board):
        return 1

    count = 0
    for i in range(len(board)):
        if is_safe(board, i, col):
            board[i][col] = 1
            count += solve_n_queens_util(board, col + 1)
            board[i][col] = 0

    return count

def solve_n_queens(n):
    board = [[0] * n for _ in range(n)]
    return solve_n_queens_util(board, 0)

def solve_n_queens_parallel(n):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = []
        for i in range(n):
            board = [[0] * n for _ in range(n)]
            board[i][0] = 1
            futures.append(executor.submit(solve_n_queens_util, board, 1))

        results = [f.result() for f in concurrent.futures.as_completed(futures)]
    return sum(results)

if __name__ == "__main__":
    N = 12  # Número de rainhas
    start_time = time.time()
    solutions = solve_n_queens_parallel(N)
    end_time = time.time()

    print(f"Total de soluções para {N} rainhas: {solutions}")
    print(f"Tempo de execução (paralelo): {end_time - start_time:.4f} segundos")