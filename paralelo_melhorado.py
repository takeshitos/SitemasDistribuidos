import concurrent.futures
import time

def is_safe(board, row, col, n):
    for i in range(col):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, n), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_n_queens_util(board, col, n):
    if col >= n:
        return 1

    count = 0
    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1
            count += solve_n_queens_util(board, col + 1, n)
            board[i][col] = 0

    return count

def solve_n_queens_parallel(n):
    with concurrent.futures.ProcessPoolExecutor() as executor:
        futures = []
        for i in range(n):
            board = [[0] * n for _ in range(n)]
            board[i][0] = 1
            futures.append(executor.submit(solve_n_queens_util, board, 1, n))

        results = [f.result() for f in concurrent.futures.as_completed(futures)]
    return sum(results)

if __name__ == "__main__":
    N = 2000
    start_time = time.time()
    solutions = solve_n_queens_parallel(N)
    end_time = time.time()

    print(f"Total de soluções para {N} rainhas: {solutions}")
    print(f"Tempo de execução (paralelo): {end_time - start_time:.4f} segundos")