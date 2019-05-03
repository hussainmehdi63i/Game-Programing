import pygame
pygame.init()


win = pygame.display.set_mode((500,480))
pygame.display.set_caption("First Game")

walkRight = [pygame.image.load('HowlR.png'),pygame.image.load('HowlR.png') ,pygame.image.load('HowlR.png'),pygame.image.load('HowlR.png'),pygame.image.load('HowlR.png'),pygame.image.load('HowlR.png'),pygame.image.load('HowlR.png'),pygame.image.load('HowlR.png'),pygame.image.load('HowlR.png')]
walkLeft = [pygame.image.load('HowlL.png'),pygame.image.load('HowlL.png'),pygame.image.load('HowlL.png'),pygame.image.load('HowlL.png'),pygame.image.load('HowlL.png'),pygame.image.load('HowlL.png'),pygame.image.load('HowlL.png'),pygame.image.load('HowlL.png'),pygame.image.load('HowlL.png')]
bg = pygame.image.load('Background.jpg')

char = pygame.image.load('Howl.png')


clock = pygame.time.Clock()

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
        self.hitbox = (self.x + 20, self.y + 11, 35, 52)

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
        pygame.draw.rect(win, (255,0,0), self.hitbox,2)



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
    walkRight = [pygame.image.load('EnemyR.png'), pygame.image.load('EnemyR.png'), pygame.image.load('EnemyR.png'), pygame.image.load('EnemyR.png'), pygame.image.load('EnemyR.png'), pygame.image.load('EnemyR.png'), pygame.image.load('EnemyR.png'), pygame.image.load('EnemyR.png'),pygame.image.load('EnemyR.png'), pygame.image.load('EnemyR.png'), pygame.image.load('EnemyR.png')]
    walkLeft = [pygame.image.load('EnemyL.png'),pygame.image.load('EnemyL.png'), pygame.image.load('EnemyL.png'),pygame.image.load('EnemyL.png'), pygame.image.load('EnemyL.png'), pygame.image.load('EnemyL.png'), pygame.image.load('EnemyL.png'), pygame.image.load('EnemyL.png'),pygame.image.load('EnemyL.png'),pygame.image.load('EnemyL.png'), pygame.image.load('EnemyL.png')]

    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.path = [self.x, self.end]
        self.walkCount = 0
        self.vel = 3
        self.hitbox = (self.x + 20, self.y + 12, 31, 57)

    def draw(self,win):
        self.move()
        if self.walkCount + 1 >= 33:
            self.walkCount = 0

        if self.vel > 0:
            win.blit(self.walkRight[self.walkCount //3], (self.x, self.y))
            self.walkCount += 1
        else:
            win.blit(self.walkLeft[self.walkCount //3], (self.x, self.y))
            self.walkCount += 1
        self.hitbox = (self.x + 20, self.y + 12, 31, 57)
        pygame.draw.rect(win, (255,0,0), self.hitbox,2)

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
        print('hit')



def redrawGameWindow():
    win.blit(bg, (0,0))
    dog.draw(win)
    beast.draw(win)
    for bullet in bullets:
        bullet.draw(win)

    pygame.display.update()


#mainloop
dog = player(200, 410, 64,64)
beast = enemy(100, 410, 64, 64, 450)
shootLoop = 0
bullets = []
run = True
while run:
    clock.tick(27)

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
                goblin.hit()
                bullets.pop(bullets.index(bullet))

        if bullet.x < 500 and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE] and shootLoop == 0:
        if dog.left:
            facing = -1
        else:
            facing = 1

        if len(bullets) < 5:
            bullets.append(projectile(round(dog.x + dog.width //2), round(dog.y + dog.height//2), 6, (0,0,0), facing))

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
