import pygame
pygame.init()

win = pygame.display.set_mode((500,480))
pygame.display.set_caption("The Howl")

walkRight = [pygame.image.load('HowlR.png'),pygame.image.load('HowlR.png') ,pygame.image.load('HowlR.png'),pygame.image.load('HowlR.png'),pygame.image.load('HowlR.png'),pygame.image.load('HowlR.png'),pygame.image.load('HowlR.png'),pygame.image.load('HowlR.png'),pygame.image.load('HowlR.png')]
walkLeft = [pygame.image.load('HowlL.png'),pygame.image.load('HowlL.png'),pygame.image.load('HowlL.png'),pygame.image.load('HowlL.png'),pygame.image.load('HowlL.png'),pygame.image.load('HowlL.png'),pygame.image.load('HowlL.png'),pygame.image.load('HowlL.png'),pygame.image.load('HowlL.png')]
bg = pygame.image.load('Background.jpg')

char = pygame.image.load('Howl.png')


clock = pygame.time.Clock()

bulletSound = pygame.mixer.Sound('bullet.wav')
hitSound = pygame.mixer.Sound('hit.wav')

music = pygame.mixer.music.load('song.mp3')
pygame.mixer.music.play(-1)

score = 0

class player(object):
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.left = False
        self.right = False
        self.walkCount = 0
        self.jumpCount = 10
        self.standing = True
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)

    def draw(self, win):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0

        if not(self.standing):
            if self.left:
                win.blit(walkLeft[self.walkCount//3], (self.x,self.y))
                self.walkCount += 1
            elif self.right:
                win.blit(walkRight[self.walkCount//3], (self.x,self.y))
                self.walkCount +=1
        else:
            if self.right:
                win.blit(walkRight[0], (self.x, self.y))
            else:
                win.blit(walkLeft[0], (self.x, self.y))
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)
        #pygame.draw.rect(win, (255,0,0), self.hitbox,2)

    def hit(self):
        self.isJump = False
        self.jumpCount = 10
        self.x = 100
        self.y = 410
        self.walkCount = 0
        font1 = pygame.font.SysFont('comicsans', 100)
        text = font1.render('-5', 1, (128,0,0))
        win.blit(text, (250 - (text.get_width()/2),200))
        pygame.display.update()
        i = 0
        while i < 200:
            pygame.time.delay(10)
            i += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    i = 201
                    pygame.quit()



class projectile(object):
    def __init__(self,x,y,radius,color,facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8 * facing

    def draw(self,win):
        pygame.draw.circle(win, self.color, (self.x,self.y), self.radius)


class enemy(object):
    walkRight = [pygame.image.load('EnemyR.png'), pygame.image.load('EnemyR.png'), pygame.image.load('EnemyR.png'), pygame.image.load('EnemyR.png'),pygame.image.load('EnemyR.png'), pygame.image.load('EnemyR.png'), pygame.image.load('EnemyR.png'), pygame.image.load('EnemyR.png'), pygame.image.load('EnemyR.png'), pygame.image.load('EnemyR.png'), pygame.image.load('EnemyR.png')]
    walkLeft = [pygame.image.load('EnemyL.png'), pygame.image.load('EnemyL.png'),pygame.image.load('EnemyL.png'), pygame.image.load('EnemyL.png'), pygame.image.load('EnemyL.png'),pygame.image.load('EnemyL.png'), pygame.image.load('EnemyL.png'), pygame.image.load('EnemyL.png'), pygame.image.load('EnemyL.png'),pygame.image.load('EnemyL.png'), pygame.image.load('EnemyL.png')]

    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.path = [self.x, self.end]
        self.walkCount = 0
        self.vel = 3
        self.hitbox = (self.x + 17, self.y + 2, 31, 57)
        self.health = 10
        self.visible = True

    def draw(self,win):
        self.move()
        if self.visible:
            if self.walkCount + 1 >= 33:
                self.walkCount = 0

            if self.vel > 0:
                win.blit(self.walkRight[self.walkCount //3], (self.x, self.y))
                self.walkCount += 1
            else:
                win.blit(self.walkLeft[self.walkCount //3], (self.x, self.y))
                self.walkCount += 1

            pygame.draw.rect(win, (255,0,0), (self.hitbox[0], self.hitbox[1] - 20, 50, 10))
            pygame.draw.rect(win, (0,128,0), (self.hitbox[0], self.hitbox[1] - 20, 50 - (5 * (10 - self.health)), 10))
            self.hitbox = (self.x + 17, self.y + 2, 31, 57)
            #pygame.draw.rect(win, (255,0,0), self.hitbox,2)

    def move(self):
        if self.vel > 0:
            if self.x + self.vel < self.path[1]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0
        else:
            if self.x - self.vel > self.path[0]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0

    def hit(self):
        if self.health > 0:
            self.health -= 1
        else:
            self.visible = False
        print('hit')

class enemy3(object):
    walkRight = [pygame.image.load('EnemyR.png'), pygame.image.load('EnemyR.png'), pygame.image.load('EnemyR.png'), pygame.image.load('EnemyR.png'),pygame.image.load('EnemyR.png'), pygame.image.load('EnemyR.png'), pygame.image.load('EnemyR.png'), pygame.image.load('EnemyR.png'), pygame.image.load('EnemyR.png'), pygame.image.load('EnemyR.png'), pygame.image.load('EnemyR.png')]
    walkLeft = [pygame.image.load('EnemyL.png'), pygame.image.load('EnemyL.png'),pygame.image.load('EnemyL.png'), pygame.image.load('EnemyL.png'), pygame.image.load('EnemyL.png'),pygame.image.load('EnemyL.png'), pygame.image.load('EnemyL.png'), pygame.image.load('EnemyL.png'), pygame.image.load('EnemyL.png'),pygame.image.load('EnemyL.png'), pygame.image.load('EnemyL.png')]

    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.path = [self.x, self.end]
        self.walkCount = 0
        self.vel = 3
        self.hitbox = (self.x + 17, self.y + 2, 31, 57)
        self.health = 10
        self.visible = True

    def draw(self,win):
        self.move()
        if self.visible:
            if self.walkCount + 1 >= 33:
                self.walkCount = 0

            if self.vel > 0:
                win.blit(self.walkRight[self.walkCount //3], (self.x, self.y))
                self.walkCount += 1
            else:
                win.blit(self.walkLeft[self.walkCount //3], (self.x, self.y))
                self.walkCount += 1

            pygame.draw.rect(win, (255,0,0), (self.hitbox[0], self.hitbox[1] - 20, 50, 10))
            pygame.draw.rect(win, (0,128,0), (self.hitbox[0], self.hitbox[1] - 20, 50 - (5 * (10 - self.health)), 10))
            self.hitbox = (self.x + 17, self.y + 2, 31, 57)
            #pygame.draw.rect(win, (255,0,0), self.hitbox,2)

    def move(self):
        if self.vel > 0:
            if self.x + self.vel < self.path[1]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0
        else:
            if self.x - self.vel > self.path[0]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0

    def hit(self):
        if self.health > 0:
            self.health -= 1
        else:
            self.visible = False
        print('hit')

class enemy1(object):
    walkRight = [pygame.image.load('Enemy1R.png'), pygame.image.load('Enemy1R.png'), pygame.image.load('Enemy1R.png'), pygame.image.load('Enemy1R.png'),pygame.image.load('Enemy1R.png'), pygame.image.load('Enemy1R.png'), pygame.image.load('Enemy1R.png'), pygame.image.load('Enemy1R.png'), pygame.image.load('Enemy1R.png'), pygame.image.load('Enemy1R.png'), pygame.image.load('Enemy1R.png')]
    walkLeft = [pygame.image.load('Enemy1L.png'), pygame.image.load('Enemy1L.png'),pygame.image.load('Enemy1L.png'), pygame.image.load('Enemy1L.png'), pygame.image.load('Enemy1L.png'),pygame.image.load('Enemy1L.png'), pygame.image.load('Enemy1L.png'), pygame.image.load('Enemy1L.png'), pygame.image.load('Enemy1L.png'),pygame.image.load('Enemy1L.png'), pygame.image.load('Enemy1L.png')]

    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.path = [self.x, self.end]
        self.walkCount = 0
        self.vel = 3
        self.hitbox = (self.x + 17, self.y + 2, 31, 57)
        self.health = 10
        self.visible = True

    def draw(self,win):
        self.move()
        if self.visible:
            if self.walkCount + 1 >= 33:
                self.walkCount = 0

            if self.vel > 0:
                win.blit(self.walkRight[self.walkCount //3], (self.x, self.y))
                self.walkCount += 1
            else:
                win.blit(self.walkLeft[self.walkCount //3], (self.x, self.y))
                self.walkCount += 1

            pygame.draw.rect(win, (255,0,0), (self.hitbox[0], self.hitbox[1] - 20, 50, 10))
            pygame.draw.rect(win, (0,128,0), (self.hitbox[0], self.hitbox[1] - 20, 50 - (5 * (10 - self.health)), 10))
            self.hitbox = (self.x + 17, self.y + 2, 31, 57)


    def move(self):
        if self.vel > 0:
            if self.x + self.vel < self.path[1]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0
        else:
            if self.x - self.vel > self.path[0]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0

    def hit(self):
        if self.health > 0:
            self.health -= 1
        else:
            self.visible = False
        print('hit')

class enemy2(object):
    walkRight = [pygame.image.load('Enemy1R.png'), pygame.image.load('Enemy1R.png'), pygame.image.load('Enemy1R.png'), pygame.image.load('Enemy1R.png'),pygame.image.load('Enemy1R.png'), pygame.image.load('Enemy1R.png'), pygame.image.load('Enemy1R.png'), pygame.image.load('Enemy1R.png'), pygame.image.load('Enemy1R.png'), pygame.image.load('Enemy1R.png'), pygame.image.load('Enemy1R.png')]
    walkLeft = [pygame.image.load('Enemy1L.png'), pygame.image.load('Enemy1L.png'),pygame.image.load('Enemy1L.png'), pygame.image.load('Enemy1L.png'), pygame.image.load('Enemy1L.png'),pygame.image.load('Enemy1L.png'), pygame.image.load('Enemy1L.png'), pygame.image.load('Enemy1L.png'), pygame.image.load('Enemy1L.png'),pygame.image.load('Enemy1L.png'), pygame.image.load('Enemy1L.png')]

    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.path = [self.x, self.end]
        self.walkCount = 0
        self.vel = 3
        self.hitbox = (self.x + 17, self.y + 2, 31, 57)
        self.health = 10
        self.visible = True

    def draw(self,win):
        self.move()
        if self.visible:
            if self.walkCount + 1 >= 33:
                self.walkCount = 0

            if self.vel > 0:
                win.blit(self.walkRight[self.walkCount //3], (self.x, self.y))
                self.walkCount += 1
            else:
                win.blit(self.walkLeft[self.walkCount //3], (self.x, self.y))
                self.walkCount += 1

            pygame.draw.rect(win, (255,0,0), (self.hitbox[0], self.hitbox[1] - 20, 50, 10))
            pygame.draw.rect(win, (0,128,0), (self.hitbox[0], self.hitbox[1] - 20, 50 - (5 * (10 - self.health)), 10))
            self.hitbox = (self.x + 17, self.y + 2, 31, 57)
            #pygame.draw.rect(win, (255,0,0), self.hitbox,2)

    def move(self):
        if self.vel > 0:
            if self.x + self.vel < self.path[1]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0
        else:
            if self.x - self.vel > self.path[0]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0

    def hit(self):
        if self.health > 0:
            self.health -= 1
        else:
            self.visible = False
        print('hit')

def redrawGameWindow():
    win.blit(bg, (0,0))
    text = font.render('Score: ' + str(score), 1, (0, 0, 128))
    win.blit(text, (350, 10))
    dog.draw(win)
    goblin.draw(win)
    for bullet in bullets:
        bullet.draw(win)
    beast.draw(win)
    for bullet in bullets:
        bullet.draw(win)
    goblin1.draw(win)
    for bullet in bullets:
        bullet.draw(win)
    beast1.draw(win)
    for bullet in bullets:
        bullet.draw(win)

    pygame.display.update()


#mainloop
font = pygame.font.SysFont('comicsans', 30, True)
dog = player(200, 410, 64,64)
goblin = enemy(1, 410, 64, 64, 100)
beast  = enemy1(250,300,64,64,300)
beast1  = enemy3(300,410,64,64,450)
goblin1  = enemy2(400,300,64,64,500)
shootLoop = 0
bullets = []
run = True
while run:
    clock.tick(27)

    if goblin.visible == True:
        if dog.hitbox[1] < goblin.hitbox[1] + goblin.hitbox[3] and dog.hitbox[1] + dog.hitbox[3] > goblin.hitbox[1]:
            if dog.hitbox[0] + dog.hitbox[2] > goblin.hitbox[0] and dog.hitbox[0] < goblin.hitbox[0] + goblin.hitbox[2]:
                dog.hit()
                score -= 5

    if shootLoop > 0:
        shootLoop += 1
    if shootLoop > 3:
        shootLoop = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for bullet in bullets:
        if bullet.y - bullet.radius < goblin.hitbox[1] + goblin.hitbox[3] and bullet.y + bullet.radius > goblin.hitbox[1]:
            if bullet.x + bullet.radius > goblin.hitbox[0] and bullet.x - bullet.radius < goblin.hitbox[0] + goblin.hitbox[2]:
                hitSound.play()
                goblin.hit()
                score += 1
                bullets.pop(bullets.index(bullet))

    if goblin1.visible == True:
        if dog.hitbox[1] < goblin1.hitbox[1] + goblin1.hitbox[3] and dog.hitbox[1] + dog.hitbox[3] > goblin1.hitbox[1]:
            if dog.hitbox[0] + dog.hitbox[2] > goblin1.hitbox[0] and dog.hitbox[0] < goblin1.hitbox[0] + goblin1.hitbox[2]:
                dog.hit()
                score -= 5

    if shootLoop > 0:
        shootLoop += 1
    if shootLoop > 3:
        shootLoop = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for bullet in bullets:
        if bullet.y - bullet.radius < goblin1.hitbox[1] + goblin1.hitbox[3] and bullet.y + bullet.radius > goblin1.hitbox[1]:
            if bullet.x + bullet.radius > goblin1.hitbox[0] and bullet.x - bullet.radius < goblin1.hitbox[0] + goblin1.hitbox[2]:
                hitSound.play()
                goblin1.hit()
                score += 1
                bullets.pop(bullets.index(bullet))


    if beast.visible == True:
        if dog.hitbox[1] < beast.hitbox[1] + beast.hitbox[3] and dog.hitbox[1] + dog.hitbox[3] > beast.hitbox[1]:
            if dog.hitbox[0] + dog.hitbox[2] > beast.hitbox[0] and dog.hitbox[0] < beast.hitbox[0] + beast.hitbox[2]:
                dog.hit()
                score -= 5

    if shootLoop > 0:
        shootLoop += 1
    if shootLoop > 3:
        shootLoop = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for bullet in bullets:
        if bullet.y - bullet.radius < beast.hitbox[1] + beast.hitbox[3] and bullet.y + bullet.radius > beast.hitbox[1]:
            if bullet.x + bullet.radius > beast.hitbox[0] and bullet.x - bullet.radius < beast.hitbox[0] + beast.hitbox[2]:
                hitSound.play()
                beast.hit()
                score += 1
                bullets.pop(bullets.index(bullet))

        if bullet.x < 500 and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))

    if beast1.visible == True:
        if dog.hitbox[1] < beast1.hitbox[1] + beast1.hitbox[3] and dog.hitbox[1] + dog.hitbox[3] > beast1.hitbox[1]:
            if dog.hitbox[0] + dog.hitbox[2] > beast1.hitbox[0] and dog.hitbox[0] < beast1.hitbox[0] + beast1.hitbox[2]:
                dog.hit()
                score -= 5

    if shootLoop > 0:
        shootLoop += 1
    if shootLoop > 3:
        shootLoop = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for bullet in bullets:
        if bullet.y - bullet.radius < beast1.hitbox[1] + beast1.hitbox[3] and bullet.y + bullet.radius > beast1.hitbox[1]:
            if bullet.x + bullet.radius > beast1.hitbox[0] and bullet.x - bullet.radius < beast1.hitbox[0] + beast1.hitbox[2]:
                hitSound.play()
                beast1.hit()
                score += 1
                bullets.pop(bullets.index(bullet))

        if bullet.x < 500 and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE] and shootLoop == 0:
        bulletSound.play()
        if dog.left:
            facing = -1
        else:
            facing = 1

        if len(bullets) < 5:
            bullets.append(projectile(round(dog.x + dog.width //2), round(dog.y + dog.height//2), 6, (178,34,34), facing))

        shootLoop = 1

    if keys[pygame.K_LEFT] and dog.x > dog.vel:
        dog.x -= dog.vel
        dog.left = True
        dog.right = False
        dog.standing = False
    elif keys[pygame.K_RIGHT] and dog.x < 500 - dog.width - dog.vel:
        dog.x += dog.vel
        dog.right = True
        dog.left = False
        dog.standing = False
    else:
        dog.standing = True
        dog.walkCount = 0

    if not(dog.isJump):
        if keys[pygame.K_UP]:
            dog.isJump = True
            dog.right = False
            dog.left = False
            dog.walkCount = 0
    else:
        if dog.jumpCount >= -10:
            neg = 1
            if dog.jumpCount < 0:
                neg = -1
            dog.y -= (dog.jumpCount ** 2) * 0.5 * neg
            dog.jumpCount -= 1
        else:
            dog.isJump = False
            dog.jumpCount = 10

    redrawGameWindow()

pygame.quit()
