import pygame
import sys

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

XO = 'x'
FPS = 120

# Height and Width of board

width = 28
height = 28

# This sets the distance between each cell

margin = 2
rownum = 33
colnum = 64

# Create a 2 dimensional array. 

grid = []
for row in range(rownum):
    grid.append([])
    for column in range(colnum):
        grid[row].append(0)
        
# Set the height and width of the screen
window_size = [1920, 990]
screen = pygame.display.set_mode(window_size)

x_img = pygame.transform.smoothscale(pygame.image.load("icon_X.png").convert(), (28, 28))
o_img = pygame.transform.smoothscale(pygame.image.load("icon_O.png").convert(), (28, 28))
player1win_img = pygame.transform.smoothscale(pygame.image.load("player1win.png").convert(), (500, 500))
player2win_img = pygame.transform.smoothscale(pygame.image.load("player2win.png").convert(), (500, 500))
restart_btn = pygame.transform.smoothscale(pygame.image.load("Restart.jpeg").convert(), (300, 200))

clock = pygame.time.Clock()

def checkwin(board):
    #Tạo mảng indices là mảng sau khi lọc ra các hàng chứa kí tự 'x'  từ mảng board
    indices = [i for i, x in enumerate(board) if 'x' in x] 
    for index in indices:
        #Tạo mảng xrow Lọc ra các ô chứa kí tự 'x'
        xrowindices = [i for i, x in enumerate(board[index]) if x == 'x']
        
        #Kiểm tra điều kiện chiến thắng
        for xs in xrowindices:
            if xs <= len(board[0]) - 5:
                if board[index][xs] == board[index][xs + 1] == board[index][xs + 2] == board[index][xs + 3] == board[index][xs + 4]:
                    return 1
            if index <= len(board) - 5:
                if board[index][xs] == board[index + 1][xs] == board[index + 2][xs] == board[index + 3][xs] == board[index + 4][xs]:
                    return 1
                if xs <= len(board[0]) - 5:
                    if board[index][xs] == board[index + 1][xs + 1] == board[index + 2][xs + 2] == board[index + 3][xs + 3] == board[index + 4][xs + 4]:
                        return 1
                    if board[index][xs] == board[index + 1][xs - 1] == board[index + 2][xs - 2] == board[index + 3][xs - 3] == board[index + 4][xs - 4]:
                        return 1
    
    indices =  [i for i, x in enumerate(board) if 'o' in x]
    for index in indices:
        #Tạo mảng xrow Lọc ra các ô chứa kí tự 'o'
        xrowindices = [i for i, x in enumerate(board[index]) if x == 'o']
        
        #Kiểm tra điều kiện chiến thắng
        for xs in xrowindices:
            if xs <= len(board[0]) - 5:
                if board[index][xs] == board[index][xs + 1] == board[index][xs + 2] == board[index][xs + 3] == board[index][xs + 4]:
                    return 2
            if index <= len(board) - 5:
                if board[index][xs] == board[index + 1][xs] == board[index + 2][xs] == board[index + 3][xs] == board[index + 4][xs]:
                    return 2
                if xs <= len(board[0]) - 5:
                    if board[index][xs] == board[index + 1][xs + 1] == board[index + 2][xs + 2] == board[index + 3][xs + 3] == board[index + 4][xs + 4]:
                        return 2
                    if board[index][xs] == board[index + 1][xs - 1] == board[index + 2][xs - 2] == board[index + 3][xs - 3] == board[index + 4][xs - 4]:
                        return 2
                        
    count = 0
    for rows in board:
        for cells in rows:
            if cells == 'x' or cells == 'o':
                count += 1
            if count == rownum * colnum:
                return 3
            
    return 0

def display_board():
    for row in range(rownum):
            for column in range(colnum):
                pygame.draw.rect(screen, WHITE, [(margin + width) * column + margin, (margin + height) * row + margin, width, height])
                
                if grid[row][column] == 'x':
                    screen.blit(x_img, ((width + margin) * column + 2, (height + margin) * row + 2))
                if grid[row][column] == 'o':
                    screen.blit(o_img, ((width + margin) * column + 2, (height + margin) * row + 2))
                    
def reset():
    global XO, status, game_over
    for i in range(rownum):
        for j in range(colnum):
            grid[i][j] = 0
    XO = 'x'
    status = 0
    game_over = False

# loop until the user clicks the close button
done = False
status = 0
game_over = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        
        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            pos = pygame.mouse.get_pos()
            col = pos[0] // (width + margin)
            row = pos[1] // (height + margin)
            
            if 0 <= row < rownum and 0 <= col < colnum and grid[row][col] == 0:
                grid[row][col] = XO
                XO = 'o' if XO == 'x' else 'x'
                status = checkwin(grid)
                if status != 0:
                    game_over = True

        if event.type == pygame.MOUSEBUTTONDOWN and game_over:
            x, y = pygame.mouse.get_pos()
            restart_rect = pygame.Rect((1920 - 300) // 2, 700, 300, 200)
            if restart_rect.collidepoint(x, y):
                reset()

    screen.fill(BLACK)
    display_board()

    if status == 3:
        font = pygame.font.Font('FreeSansBold.ttf', 100)
        text = font.render('Draw', True, GREEN, BLUE)
        textRect = text.get_rect()
        textRect.center = window_size[0] // 2, window_size[1] // 2
        screen.blit(text, textRect)
    
    if status == 1:
        screen.blit(player1win_img, ((1920 - 500) // 2, (990 - 500) // 2 - 100))
    
    if status == 2:
        screen.blit(player2win_img, ((1920 - 500) // 2, (990 - 500) // 2 - 100))

    if game_over:
        screen.blit(restart_btn, ((1920 - 300) // 2, 700))

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()