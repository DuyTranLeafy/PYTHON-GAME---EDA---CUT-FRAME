import pygame, sys, random
from pygame.locals import *
import Select_Map
import Start_Main
import Select_Car

####################################
#PHẦN 1: ĐỊNH NGHĨA CÁC THAM SỐ ##
#####################################
###KÍCH THƯỚC KHUNG MÀN HÌNH GAME
WINDOWWIDTH = 400
WINDOWHEIGHT = 600
###KHỞI TẠO THƯ VIỆN ĐỂ DÙNG
pygame.init()
##TỐC ĐỘ KHUNG HÌNH CỦA VIDEO
FPS = 60 # Famres Per Second
fpsClock = pygame.time.Clock() #Lặp theo nhịp clock (tham số FPS) 
####################################
#####PHẦN 2: NỀN GAME ##############
#####################################
#TỐC ĐỘ CUỘN NỀN
BGSPEED = 3.0 # tốc độ cuộn nền
# LAYER (SURFACE) NỀN
DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('09 TRAN VAN BAO DUY')
# LỚP HÌNH NỀN = CUỘN NỀN
X_MARGIN = 80
CARWIDTH = 40
CARHEIGHT = 60
CARSPEED = 4

class Background():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.speed = BGSPEED
        self.img = pygame.image.load(Select_Map.Map)
        self.width = self.img.get_width()
        self.height = self.img.get_height()

    def draw(self):
        DISPLAYSURF.blit(self.img, (int(self.x), int(self.y)))
        DISPLAYSURF.blit(self.img, (int(self.x), int(self.y - self.height)))

    def update(self):
        self.y += self.speed

        if self.y > self.height:
            self.y -= self.height


class Car():
    def __init__(self):
        self.width = CARWIDTH
        self.height = CARHEIGHT
        self.x = (WINDOWWIDTH - self.width) / 2
        self.y = (WINDOWHEIGHT - self.height) / 2
        self.speed = CARSPEED
        self.surface = pygame.Surface((self.width, self.height))
        self.surface.fill((255, 255, 255))


    def draw(self):
        DISPLAYSURF.blit(pygame.image.load(Select_Car.Car), (int(self.x), int(self.y)))


    def update(self, moveLeft, moveRight, moveUp, moveDown):
        if moveLeft == True:
            self.x -= self.speed
        if moveRight == True:
            self.x += self.speed
        if moveUp == True:
            self.y -= self.speed
        if moveDown == True:
            self.y += self.spee
        if self.x < X_MARGIN:
            self.x = X_MARGIN
        if self.x + self.width > WINDOWWIDTH - X_MARGIN:
            self.x = WINDOWWIDTH - X_MARGIN - self.width
        if self.y < 0:
            self.y = 0
        if self.y + self.height > WINDOWHEIGHT:
            self.y = WINDOWHEIGHT - self.height
LANEWIDTH = 60
DISTANCE = 200
OBSTACLESSPEED = 2
CHANGESPEED = 0.001
OBSTACLESIMG = pygame.image.load('img/obstaclesBD09.png')
class Obstacles():
    pygame.init()
    def __init__(self):
        self.width = CARWIDTH
        self.height = CARHEIGHT
        self.distance = DISTANCE
        self.speed = OBSTACLESSPEED
        self.changeSpeed = CHANGESPEED
        self.ls = []
        for i in range(5):
            y = -CARHEIGHT-i*self.distance
            lane = random.randint(0, 3)
            self.ls.append([lane, y])
    def draw(self):
        for i in range(5):
            x = int(X_MARGIN + self.ls[i][0]*LANEWIDTH + (LANEWIDTH-self.width)/2)
            y = int(self.ls[i][1])
            DISPLAYSURF.blit(OBSTACLESIMG, (x, y))
    def update(self):
        for i in range(5):
            self.ls[i][1] += self.speed
        self.speed += self.changeSpeed
        if self.ls[0][1] > WINDOWHEIGHT:
            self.ls.pop(0)
            y = self.ls[3][1] - self.distance
            lane = random.randint(0, 3)
            self.ls.append([lane, y])

class Score():
    def __init__(self):
        self.score = 0

    def draw(self):
        font = pygame.font.SysFont('consolas', 30)
        scoreSuface = font.render('Score: ' + str(int(self.score)), True, (0, 0, 0))
        DISPLAYSURF.blit(scoreSuface, (10, 10))

    def update(self):
        self.score += 0.02

    def rectCollision(self, rect1, rect2):
        if rect1[0] <= rect2[0] + rect2[2] and rect2[0] <= rect1[0] + rect1[2] and rect1[1] <= rect2[1] + rect2[3] and \
                rect2[1] <= rect1[1] + rect1[3]:
            return True
        return False

    def isGameover(self, car, obstacles):
        carRect = [car.x, car.y, car.width, car.height]
        for i in range(5):
            x = int(X_MARGIN + obstacles.ls[i][0] * LANEWIDTH + (LANEWIDTH - obstacles.width) / 2)
            y = int(obstacles.ls[i][1])
            obstaclesRect = [x, y, obstacles.width, obstacles.height]
            if self.rectCollision(carRect, obstaclesRect):
                return True
        return False

    def gameOver(self, bg, car, obstacles, score):
        pygame.mixer.music.pause()
        pygame.mixer.init()
        pygame.mixer.music.load("audio/over.mp3")
        # Thêm tham số loops để chạy lặp lại vô hạn
        pygame.mixer.music.play()
        font = pygame.font.SysFont('consolas', 60)
        headingSuface = font.render('GAMEOVER', True, (255, 0, 0))
        headingSize = headingSuface.get_size()
        font = pygame.font.SysFont('consolas', 20)
        commentSuface = font.render('Press "space" to replay', True, (0, 0, 0))
        commentQuit = font.render('Press "Q" to quit', True, (0, 0, 0))
        commentSize = commentSuface.get_size()
        commentSizeQuit = commentQuit.get_size()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYUP:
                    if event.key == K_SPACE:
                        pygame.mixer.init()
                        pygame.mixer.music.load("audio/racing.mp3")
                        # Thêm tham số loops để chạy lặp lại vô hạn
                        pygame.mixer.music.play(loops=-1)
                        return
                    elif event.key == K_q:  # Thêm điều kiện cho phím Q
                        background = Start_Main.PacmanStartMenu()
                        background.run_start_menu()
                        return
                        
                
            bg.draw()
            car.draw()
            obstacles.draw()
            score.draw()
            DISPLAYSURF.blit(headingSuface, (int((WINDOWWIDTH - headingSize[0]) / 2), 100))
            DISPLAYSURF.blit(commentSuface, (int((WINDOWWIDTH - commentSize[0]) / 2), 400))
            DISPLAYSURF.blit(commentQuit, (int((WINDOWWIDTH - commentSizeQuit[0]) / 2), 420))
            pygame.display.update()
            fpsClock.tick(FPS)

    def gameStart(self, bg):
        bg.__init__()
        font = pygame.font.SysFont('consolas', 60)
        headingSuface = font.render('RACING', True, (255, 0, 0))
        headingSize = headingSuface.get_size()
        font = pygame.font.SysFont('consolas', 20)
        commentSuface = font.render('Press "space" to play', True, (0, 0, 0))
        commentSize = commentSuface.get_size()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYUP:
                    if event.key == K_SPACE:
                        return
                    
            bg.draw()
            DISPLAYSURF.blit(headingSuface, (int((WINDOWWIDTH - headingSize[0]) / 2), 100))
            DISPLAYSURF.blit(commentSuface, (int((WINDOWWIDTH - commentSize[0]) / 2), 400))
            pygame.display.update()
            fpsClock.tick(FPS)

    def gamePlay(self, bg, car, obstacles, score):
        pygame.init()
        car.__init__()
        obstacles.__init__()
        bg.__init__()
        score.__init__()
        moveLeft = False
        moveRight = False
        moveUp = False
        moveDown = False
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_LEFT:
                        moveLeft = True
                    if event.key == K_RIGHT:
                        moveRight = True
                    if event.key == K_UP:
                        moveUp = True
                    if event.key == K_DOWN:
                        moveDown = True
                if event.type == KEYUP:
                    if event.key == K_LEFT:
                        moveLeft = False
                    if event.key == K_RIGHT:
                        moveRight = False
                    if event.key == K_UP:
                        moveUp = False
                    if event.key == K_DOWN:
                        moveDown = False
            if self.isGameover(car, obstacles):
                return
            bg.draw()
            bg.update()
            car.draw()
            car.update(moveLeft, moveRight, moveUp, moveDown)
            obstacles.draw()
            obstacles.update()
            self.draw()
            self.update()
            pygame.display.update()
            fpsClock.tick(FPS)


class GameRunner:
    def __init__(self):
        pygame.mixer.init()
        pygame.mixer.music.load("audio/racing.mp3")
        # Thêm tham số loops để chạy lặp lại vô hạn
        pygame.mixer.music.play(loops=-1)
        pygame.init()
        self.window_width = 400
        self.window_height = 600
        self.display_surface = pygame.display.set_mode((self.window_width, self.window_height))
        pygame.display.set_caption('Your Game Title')
        bg = Background()
        car = Car()
        obstacles = Obstacles()
        score = Score()
        score.gameStart(bg)
        while True:
            score.gamePlay(bg, car, obstacles, score)
            score.gameOver(bg, car, obstacles, score)
            
        # CỬA SỔ START
        self.root = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        background = pygame.image.load(
            'img/start_main.png')
        background = pygame.transform.scale(background, (self.WIDTH, self.HEIGHT))
        self.root.blit(background, (0, 0))

    def run_game(self):
        main()






