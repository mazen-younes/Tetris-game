import pygame,sys
from game import Game
from colors import Colors
pygame.init()

title_font = pygame.font.Font(None,40)
game_over_font = pygame.font.Font(None,65)
score_surface = title_font.render("Score",True, Colors.yellow)
next_surface = title_font.render("Next",True, Colors.green)
game_over_surface = game_over_font.render("Game Over",True, Colors.red)


score_rect = pygame.Rect(365,55,170,60)
next_rect = pygame.Rect(365,215,170,200)



screen = pygame.display.set_mode((600,620))
pygame.display.set_caption(" Tetris ")

clock = pygame.time.Clock()
game = Game()
GAME_UPADATE = pygame.USEREVENT
pygame.time.set_timer(GAME_UPADATE,1000)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if game.game_over == True:
                game.game_over = False
                game.reset()
            if event.key == pygame.K_LEFT and game.game_over == False :
                game.move_left()
            if event.key == pygame.K_RIGHT and game.game_over == False :
                game.move_right()
            if event.key == pygame.K_DOWN and game.game_over == False :
                game.move_down() 
                game.update_score( 0 , 1)
            if event.key == pygame.K_SPACE and game.game_over == False :
                game.rotate()
        if event.type == GAME_UPADATE and game.game_over == False:
            game.move_down()

    score_value_surface = title_font.render(str(game.score),True , Colors.dark_blue)

    screen.fill(Colors.dark_blue)
    screen.blit(score_surface,(410,20,50,50))
    screen.blit(next_surface,(420,150,50,50))
    if game.game_over == True:
        screen.blit(game_over_surface,(340,500,50,50))

    pygame.draw.rect(screen,Colors.white,score_rect,0,10)
    screen.blit(score_value_surface , score_value_surface.get_rect(centerx = score_rect.centerx, centery = score_rect.centery))
    pygame.draw.rect(screen,Colors.white,next_rect,0,10)
    game.draw(screen)
    pygame.display.update()
    clock.tick(60)
