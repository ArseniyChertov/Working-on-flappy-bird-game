import pygame, sys
import PIL
import random


class Game:
    counter = 0
    start_game = True
    def __init__(self):

        pygame.init()  # always init pygame(initialize modules)
        self.screen = pygame.display.set_mode((288, 512))  # pygame window with dimensions
        self.clock = pygame.time.Clock()
        self.game_start = False

        self.gravity = 0.27  # need to make bird move down
        self.birdmove = 0  # movement of bird

        self.back = pygame.image.load('pic/back.png')
        self.base = pygame.image.load('pic/base.png')
        self.birdmid = pygame.image.load('pic/birdmid.png')
        self.birdrec = self.birdmid.get_rect(center=(100, 288))  # Hit box for bird and pipes
        self.movement = 0  # movement of base of game
        # self.menu_surf = pygame.image.load('../graphics/ui/menu.png').convert_alpha()

        self.button = pygame.image.load('pic/button.png')
        self.greenp = pygame.image.load('pic/greenp.png')
        self.start = pygame.image.load('pic/start.png')
        self.piperec = self.greenp.get_rect(center=(150, 144))
        self.fliped = pygame.image.load('pic/fliped.png')
        self.pipe_list = []
        self.pipe_list2 = []
        self.SPAWNPIPE = pygame.USEREVENT
        pygame.time.set_timer(self.SPAWNPIPE, 2000)
        self.color = (255, 255, 0)
        self.s = 0
        self.x = 0
    def run(self):


        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.birdmove = 0
                        self.birdmove = -6
                if event.type == self.SPAWNPIPE:
                    self.height = random.randint(275, 370)
                    self.pipe_list.append(self.create_pipe(self.height))
                    self.pipe_list2.append(self.create_pipe2(self.height))



            self.birdmove += self.gravity
            self.birdrec.centery += self.birdmove

            self.screen.blit(self.back, (0, 0))
            self.screen.blit(self.birdmid, self.birdrec)

            self.pipe_list = self.movep(self.pipe_list)
            self.pipe_list2 = self.movep2(self.pipe_list2)

            self.draw_pipes(self.pipe_list)
            self.draw_pipes2(self.pipe_list2)

            self.movement -= 1
            self.center_y_bird = self.birdrec.centery - 15
            self.rect1 = pygame.Rect(80, self.center_y_bird, 35, 35)
            self.draw_floor()
            if self.movement <= -288:
                self.movement = 0

            self.display_score()


            # rect1 = pygame.draw.rect(screen, (255, 0, 0), (80, birdrec.centery - 15, 35, 35))

            pygame.display.update()
            self.clock.tick(120)

    def draw_floor(self):
        self.screen.blit(self.base, (self.movement, 400))  # original base
        self.screen.blit(self.base, (self.movement + 288, 400))  # added on base to the right of screen
        # clock.tick(200)

    def create_pipe(self, size):
        self.newp = self.greenp.get_rect(midtop=(300, size))  # draws pipe(325)
        return self.newp

    def create_pipe2(self, size):
        self.n_size = size - 500
        self.newp2 = self.fliped.get_rect(midtop=(300, self.n_size))  # draws pipe(-220)
        return self.newp2

    def movep(self, pipes):
        for pipe in pipes:
            pipe.centerx -= 1  # creates new list of new rectangles

            # rect2 = pygame.draw.rect(screen, (255, 0, 0), (pipe.centerx - 20, 350, 30, 100))
            center_x = pipe.centerx - 20
            self.rect2 = pygame.Rect(center_x, self.height, 30, 100)
            if self.rect1.x == self.rect2.x and self.rect1.y == self.rect2.y:
                pygame.quit()
            distance = (((self.rect1.x - self.rect2.x) ** 2) + ((self.rect1.y - self.rect2.y) ** 2)) ** 0.5

            if distance < (self.rect1.width + self.rect2.width) / 2.0:
                pygame.quit()
            if self.rect1.x == self.rect2.x:
                self.counter += 1

            #self.rect4 = pygame.Rect(self.movement, 400, 400, 200)
            self.rect4 = pygame.draw.rect(self.screen, (255, 0, 0), (0, 400, 400, 200))
            if self.rect1.x == self.rect4.x and self.rect1.y == self.rect4.y:
                pygame.quit()
            distance = (((self.rect1.x - self.rect4.x) ** 2) + ((self.rect1.y - self.rect4.y) ** 2)) ** 0.5

            if distance < (self.rect1.width + self.rect4.width) / 2.0:
                pygame.quit()
                # font = pygame.font.Font('freesansbold.ttf', 32)
                # text = font.render('Score is ' + str(score), True, (255, 0, 0), (0, 0, 0))
                # screen.blit(text, (50, 50))
        return pipes

    def movep2(self, pipes):
        for pipe in pipes:
            pipe.centerx -= 1

            # rect3 = pygame.draw.rect(screen, (255, 0, 0), (pipe.centerx - 20, 0, 120, 120))
            center_x = pipe.centerx - 20
            self.rect3 = pygame.Rect(center_x, 0, self.height - 100, 120)
            if self.rect1.x == self.rect3.x and self.rect1.y == self.rect3.y:
                pygame.quit()
            distance = (((self.rect1.x - self.rect3.x) ** 2) + ((self.rect1.y - self.rect3.y) ** 2)) ** 0.5

            if distance < (self.rect1.width + self.rect3.width) / 2.0:
                pygame.quit()

        return pipes

    def draw_pipes(self, pipes):
        for pipe in pipes:
            self.screen.blit(self.greenp, (pipe))

    def draw_pipes2(self, pipes):
        for pipe in pipes:
            self.screen.blit(self.fliped, (pipe))

    def display_score(self):
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render(str(self.counter), True, (255, 0, 0), (0, 0, 0))
        self.screen.blit(text, (265, 475))


if __name__ == '__main__':
    game = Game()
    game.run()
