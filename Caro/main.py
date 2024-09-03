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

#loop until the user clicks the close button
done = False
status = None

while not done:
    # User do some operations
    for event in pygame.event.get():
        
        display_board()
        
        if event.type == pygame.QUIT:
            done = True
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            col = pos[0] // (width + margin)
            row = pos[1] // (height + margin)
            
            if grid[row][col] == 0:
                if XO == 'x':
                    grid[row][col] = XO
                    XO = 'o'
                else:
                    grid[row][col] = XO
                    XO = 'x'
                    
            display_board()
                    
            status = checkwin(grid)
            
            if status == 3:
                font = pygame.font.Font('FreeSansBold.ttf', 100)
                text = font.render('Draw', True, GREEN, BLUE)
                textRect = text.get_rect()
                textRect.center = window_size[0] / 2, window_size[1] / 2
                screen.blit(text, textRect)
                done = True
                
            if status == 1:
                screen.blit(player1win_img, ((1920 - 500) / 2, (990 - 500) / 2, 500, 500))
                done = True
                
            if status == 2:
                screen.blit(player2win_img, ((1920 - 500) / 2, (990 - 500) / 2, 500, 500))
                done = True                
                
    # if done == True:
    #     pygame.time.delay(100000000)
    #     font = pygame.font.Font('FreeSansBold.ttf', 100)
    #     text = font.render('New match', True, BLACK, WHITE)
    #     text.border
    #     text_rect = text.get_rect()
    #     text_rect.center = (window_size[0] / 2, window_size[1] / 2 + 400)
    #     screen.blit(text, text_rect)
    
    #     for event in pygame.event.get():
    #         if event.type == pygame.MOUSEBUTTONDOWN:
    #             y, x = pygame.mouse.get_pos()
    #             if x >= window_size[0] / 2 and x <= window_size[0] / 2 + text.get_width() and y >= window_size[1] / 2 + 400 and y <= window_size[1] / 2 + 400 + text.get_height():
    #                 done = False
    #                 for rows in grid:
    #                     for cells in rows:
    #                         cells = 0
            
                
        
    clock.tick(FPS)
    pygame.display.update()
    
pygame.time.delay(10000)
quit()
pygame.quit()
sys.exit()