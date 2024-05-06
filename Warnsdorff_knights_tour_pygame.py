import pygame
import sys
import time

def initialize_chessboard(N):
    return [[-1 for i in range(N)] for j in range(N)]

def print_board(board):
    for row in board:
        for val in row:
            print(f"{val:02d}", end=' ')
        print()

def is_safe(x, y, N, visited):
    return (0 <= x < N) and (0 <= y < N) and not visited[x][y]

def count_valid_moves(x, y, N, visited):
    count = 0
    for dx, dy in [(2, 1), (1, 2), (-1, 2), (-2, 1),
                   (-2, -1), (-1, -2), (1, -2), (2, -1)]:
        new_x, new_y = x + dx, y + dy
        if is_safe(new_x, new_y, N, visited):
            count += 1
    return count

def get_next_move(x, y, N, visited):
    min_count = float('inf')
    next_move = (-1, -1)
    moves = [(2, 1), (1, 2), (-1, 2), (-2, 1),
             (-2, -1), (-1, -2), (1, -2), (2, -1)]
    for dx, dy in moves:
        new_x, new_y = x + dx, y + dy
        if is_safe(new_x, new_y, N, visited):
            num_moves = count_valid_moves(new_x, new_y, N, visited)
            if num_moves < min_count:
                min_count = num_moves
                next_move = (new_x, new_y)
    return next_move

def draw_board(screen, N, cell_size, board, path, knight_img):
    for x in range(N):
        for y in range(N):
            rect = (y * cell_size, x * cell_size, cell_size, cell_size)
            if (x + y) % 2 == 0:
                bg_color = (255, 255, 255)  # White square
                text_color = (0, 0, 0)  # Black text on white background
            else:
                bg_color = (0, 0, 0)  # Black square
                text_color = (255, 255, 255)  # White text on black background
            
            pygame.draw.rect(screen, bg_color, rect)
            if (x, y) in path:
                screen.blit(knight_img, (y * cell_size, x * cell_size))
            if board[x][y] >= 0:
                font = pygame.font.SysFont(None, 20)
                text = font.render(str(board[x][y]), True, text_color)
                text_rect = text.get_rect(center=(y * cell_size + cell_size // 2, x * cell_size + cell_size // 2))
                screen.blit(text, text_rect)

def solve_knights_tour_chessboard(N, screen, knight_img):
    board = initialize_chessboard(N)
    visited = [[False for _ in range(N)] for _ in range(N)]
    x, y = 0, 0
    path = [(x, y)]
    visited[x][y] = True
    move_number = 0
    running = True
    while running:
        for event in pygame.event.get():
            if event.type is pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
        screen.fill((60, 70, 90))
        draw_board(screen, N, cell_size, board, path, knight_img)
        pygame.display.flip()
        time.sleep(0.5)  # Pause for visualization
        
        if move_number < N * N - 1:
            next_x, next_y = get_next_move(x, y, N, visited)
            if next_x == -1 or next_y == -1:
                print("No solution found!")
                running = False
            else:
                x, y = next_x, next_y
                path.append((x, y))
                visited[x][y] = True
                board[x][y] = move_number + 1
                move_number += 1
        else:
            print("Tour complete!")
            running = False

if __name__ == "__main__":
    N = 8
    pygame.init()
    cell_size = 80
    screen = pygame.display.set_mode((N * cell_size, N * cell_size))
    pygame.display.set_caption("Warnsdorff's Algorithm Knight's Tour")
    knight_img = pygame.image.load("knight.png").convert_alpha()  # Load knight image
    knight_img = pygame.transform.scale(knight_img, (cell_size, cell_size))  # Resize knight image
    solve_knights_tour_chessboard(N, screen, knight_img)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
