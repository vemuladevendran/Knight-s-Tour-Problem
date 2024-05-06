import pygame
import sys

def initialize_chessboard(N):
    return [[-1 for _ in range(N)] for _ in range(N)]

def is_safe(x, y, board):
    return (0 <= x < len(board)) and (0 <= y < len(board)) and (board[x][y] == -1)

def print_board(board):
    for row in board:
        print(' '.join(f'{val:02d}' for val in row))

def solve_knights_tour_chessboard_util(N, board, current_x, current_y, move_x, move_y, position, screen, colors):
    if position == N**2:
        return True
    for i in range(8):
        new_x = current_x + move_x[i]
        new_y = current_y + move_y[i]
        if is_safe(new_x, new_y, board):
            board[new_x][new_y] = position
            draw_board(board, screen, colors)
            pygame.display.flip()
            pygame.time.wait(50)
            if solve_knights_tour_chessboard_util(N, board, new_x, new_y, move_x, move_y, position + 1, screen, colors):
                return True
            board[new_x][new_y] = -1  # Backtrack
    return False

def draw_board(board, screen, colors):
    blockSize = 50  
    for x in range(len(board)):
        for y in range(len(board)):
            rect = pygame.Rect(x*blockSize, y*blockSize, blockSize, blockSize)
            pygame.draw.rect(screen, colors[(x+y) % 2], rect)
            if board[x][y] != -1:
                font = pygame.font.Font(None, 40)
                text = font.render(str(board[x][y]), True, (255, 0, 0))
                screen.blit(text, (x*blockSize + 15, y*blockSize + 10))

def solve_knights_tour_chessboard(N):
    pygame.init()
    blockSize = 50  
    screen = pygame.display.set_mode((N*blockSize, N*blockSize))
    colors = [(255, 255, 255), (0, 0, 0)]  
    
    board = initialize_chessboard(N)
    move_x = [2, 1, -1, -2, -2, -1, 1, 2]
    move_y = [1, 2, 2, 1, -1, -2, -2, -1]
    board[0][0] = 0
    
    if not solve_knights_tour_chessboard_util(N, board, 0, 0, move_x, move_y, 1, screen, colors):
        print("Solution does not exist")
    else:
        print_board(board)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

if __name__ == "__main__":
    N = 8
    solve_knights_tour_chessboard(N)
