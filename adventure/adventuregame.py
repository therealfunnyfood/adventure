import pygame
e = 1
pygame.init()
display = pygame.display.set_mode((400,400))
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans Ms', 30)
clock = pygame.time.Clock()
key_sprite = pygame.image.load("adventure/Key.png")

class game:
        def __init__(self):
            self.reset = 1
            self.inst = 0
            self.instk = 0
            self.rid = False
            self.keysleft = 4
            self.showclock = False
            self.change = 1
Game = game()
while Game.reset == 1:
    game()
    while Game.change == 1:
        

        class player:
            def __init__(self, x, y, csnum):
                self.x = x
                self.y = y
                self.up = False
                self.down = False
                self.left = False
                self.right = False
                self.csnum = csnum
                self.csnumo = 0
                self.ox = x
                self.oy = y
                self.gr = False
                self.gl = False
                self.gd = False
                self.gu = False
            
            def move(self, x, y):
                self.ox = x
                self.oy = y

                vX = 0
                vY = 0

                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_d:
                            self.right = True
                        if event.key == pygame.K_a:
                            self.left = True
                        if event.key == pygame.K_w:
                            self.up = True
                        if event.key == pygame.K_s:
                            self.down = True
                        if event.key == pygame.K_l:
                            quit()
                    if event.type == pygame.KEYUP:
                        if event.key == pygame.K_d:
                            self.right = False
                        if event.key == pygame.K_a:
                            self.left = False
                        if event.key == pygame.K_w:
                            self.up = False
                        if event.key == pygame.K_s:
                            self.down = False
                        
                
                if self.left == True:
                    vX -= 6
                if self.right == True:
                    vX += 6
                if self.up == True:
                    vY -= 6
                if self.down == True:
                    vY += 6

                self.x += vX
                self.y += vY
            
            def draw(self, display):
                pygame.draw.rect(display, (0, 255, 255), (self.x, self.y, 10, 10))
            
            def main(self):
                self.move(self.x, self.y)
                self.draw(display)

        class wall:
            def __init__(self, x, y, length, width):
                self.x = x 
                self.y = y
                self.length = length
                self.width = width

            
            def draw(self, display):
                pygame.draw.rect(display, (255, 255, 0),(self.x, self.y, self.width, self.length))
            
            def main(self):
                self.draw(display)

        class Key:
            def __init__(self, x, y, snum):
                self.x = x 
                self.y = y
                self.snum = snum
            
            def draw(self, display):
                if self.snum == Player.csnum:
                    display.blit(pygame.transform.scale(key_sprite, (25, 25)), (self.x, self.y))
                else:
                    pass
            def main(self):
                self.draw(display)

        class door:
            def __init__(self, x, y, snum):
                self.x = x
                self.y = y
                self.snum = snum
                self.unlocked = False
                print("aaaa")
            
            def draw(self, display):
                if self.snum == Player.csnum:
                    pygame.draw.rect(display, (77, 55, 5),(self.x, self.y, 50, 50))
            def main(self):
                self.draw(display)
        if Game.inst == 0:
            Player = player(187.5, 325, 5)
            Walls = [wall(150, 150, 100, 100),wall(0, 300, 100, 150), wall(250, 300, 100, 150), wall(0, 0, 100, 150), wall(250, 0, 100, 150), wall(0, 250, 50, 50), wall(0, 100, 50, 50), wall(350, 100, 50, 50), wall(350, 250, 50, 50)]
            Keys = [Key(275, 75, 3),Key(275,175, 6),Key(75, 275, 7),Key(225, 175, 9)]
            Door = door(200, 175, 4)
            print("aaa")
            Game.inst += 1
        if Player.csnum == 1:
            Walls = [wall(0, 0, 75, 400), wall(0, 0, 400, 75), wall(75, 300, 100, 175), wall(350, 225, 50, 175), wall(350, 75, 50, 100), wall(125, 125, 100, 100)]
            Keys = [Key(287.5, 87.5, 3),Key(275,175, 6),Key(75, 275, 7),Key(225, 175, 9)]
            if Player.gl == True:
                Player = player(375, Player.oy, 1)
                Player.gl == False
            elif Player.gu == True:
                Player = player(Player.ox, 375, 1)
                Player.gu = False
            elif Player.gr == True:
                Player = player(5, Player.oy, 1)
                Player.gr = False
            elif Player.gd == True:
                Player = player(Player.ox, 5, 1)
                Player.gd = False

        if Player.csnum == 2:
            Walls = [wall(0, 0, 75, 400), wall(0, 75, 100, 150), wall(225, 0, 175, 150), wall(250, 75, 300, 150)]
            Keys = [Key(287.5, 87.5, 3),Key(275,175, 6),Key(75, 275, 7),Key(225, 175, 9)]
            if Player.gl == True:
                Player = player(375, Player.oy, 2)
                Player.gl == False
            elif Player.gu == True:
                Player = player(Player.ox, 375, 2)
                Player.gu = False
            elif Player.gr == True:
                Player = player(5, Player.oy, 2)
                Player.gr = False
            elif Player.gd == True:
                Player = player(Player.ox, 5, 2)
                Player.gd = False
        if Player.csnum == 3:
            Walls = [wall(0, 0, 250, 250), wall(0, 250, 150, 50), wall(275, 0, 75, 125), wall(325, 75, 325, 75), wall(150, 300, 100, 250)]
            Keys = [Key(287.5, 87.5, 3),Key(275,175, 6),Key(75, 275, 7),Key(225, 175, 9)]
            if Player.gl == True:
                Player = player(375, Player.oy, 3)
                Player.gl == False
            elif Player.gu == True:
                Player = player(Player.ox, 375, 3)
                Player.gu = False
            elif Player.gr == True:
                Player = player(5, Player.oy, 3)
                Player.gr = False
            elif Player.gd == True:
                Player = player(Player.ox, 5, 3)
                Player.gd = False
        if Player.csnum == 4:
            Walls = [wall(0, 0, 400, 75), wall(0, 0, 50, 250), wall(0, 350, 50, 250), wall(150, 100, 50, 200), wall(150, 250, 50, 200), wall(350, 0, 400, 50), wall(175, 175, 50, 25), wall(250, 175, 50, 25)]
            Doors = [door(200, 175, 4)]
            Keys = [Key(287.5, 87.5, 3),Key(275,175, 6),Key(75, 275, 7),Key(225, 175, 9)]
            if Player.gl == True:
                Player = player(375, Player.oy, 4)
                Player.gl == False
            elif Player.gu == True:
                Player = player(Player.ox, 375, 4)
                Player.gu = False
            elif Player.gr == True:
                Player = player(5, Player.oy, 4)
                Player.gr = False
            elif Player.gd == True:
                Player = player(Player.ox, 5, 4)
                Player.gd = False
        if Player.csnum == 5:
            Walls = [wall(0, 0, 100, 150), wall(250, 0, 100, 150), wall(350, 100, 50, 50), wall(0, 100, 200, 50), wall(0, 300, 100, 150), wall(150, 375, 25, 100), wall(350, 250, 50, 50), wall(250, 300, 100, 150), wall(150, 150, 100, 100)]
            Keys = [Key(287.5, 87.5, 3),Key(275,175, 6),Key(75, 275, 7),Key(225, 175, 9)]
            if Player.gl == True:
                Player = player(375, Player.oy, 5)
                Player.gl == False
            elif Player.gu == True:
                Player = player(Player.ox, 375, 5)
                Player.gu = False
            elif Player.gr == True:
                Player = player(5, Player.oy, 5)
                Player.gr = False
            elif Player.gd == True:
                Player = player(Player.ox, 5, 5)
                Player.gd = False
        if Player.csnum == 6:
            Walls = [wall(0, 0, 150, 50), wall(0, 250, 50, 50), wall(0, 300, 100, 400), wall(0, 150, 100, 250), wall(325, 100, 200, 75), wall(100, 125, 150, 50), wall(200, 125, 150, 50)]
            Keys = [Key(287.5, 87.5, 3),Key(275,175, 6),Key(75, 275, 7),Key(225, 175, 9)]
            if Player.gl == True:
                Player = player(375, Player.oy, 6)
                Player.gl == False
            elif Player.gu == True:
                Player = player(Player.ox, 375, 6)
                Player.gu = False
            elif Player.gr == True:
                Player = player(5, Player.oy, 6)
                Player.gr = False
            elif Player.gd == True:
                Player = player(Player.ox, 5, 6)
                Player.gd = False
        if Player.csnum == 7:
            Walls = [wall(0, 0, 50, 250), wall(0, 0, 400, 75), wall(75, 325, 75, 325), wall(75, 200, 75, 100), wall(125, 100, 50, 275), wall(225, 150, 125, 75), wall(350, 0, 150, 50), wall(350, 225, 100, 50), wall(300, 150, 25, 100)]
            Keys = [Key(287.5, 87.5, 3),Key(275,175, 6),Key(75, 275, 7),Key(225, 175, 9)]
            if Player.gl == True:
                Player = player(375, Player.oy, 7)
                Player.gl == False
            elif Player.gu == True:
                Player = player(Player.ox, 375, 7)
                Player.gu = False
            elif Player.gr == True:
                Player = player(5, Player.oy, 7)
                Player.gr = False
            elif Player.gd == True:
                Player = player(Player.ox, 5, 7)
                Player.gd = False
        if Player.csnum == 8:
            Walls = [wall(0, 0, 75, 400), wall(0, 325, 75, 400), wall(100, 100, 75, 200), wall(100, 225, 75, 200), wall(0, 75, 100, 50), wall(0, 225, 100, 50), wall(350, 75, 100, 50), wall(350, 225, 100, 50)]
            Keys = [Key(287.5, 87.5, 3),Key(275,175, 6),Key(75, 275, 7),Key(225, 175, 9)]
            if Player.gl == True:
                Player = player(375, Player.oy, 8)
                Player.gl == False
            elif Player.gu == True:
                Player = player(Player.ox, 375, 8)
                Player.gu = False
            elif Player.gr == True:
                Player = player(5, Player.oy, 8)
                Player.gr = False
            elif Player.gd == True:
                Player = player(Player.ox, 5, 8)
                Player.gd = False
        if Player.csnum == 9:
            Walls = [wall(0, 0, 50, 400), wall(0, 0, 175, 100), wall(300, 50, 200, 100), wall(0, 250, 150, 400), wall(0, 225, 25, 200), wall(150, 100, 50, 100), wall(150, 100, 125, 50)]
            Keys = [Key(287.5, 87.5, 3),Key(275,175, 6),Key(75, 275, 7),Key(225, 175, 9)]
            if Player.gl == True:
                Player = player(375, Player.oy, 9)
                Player.gl == False
            elif Player.gu == True:
                Player = player(Player.ox, 375, 9)
                Player.gu = False
            elif Player.gr == True:
                Player = player(5, Player.oy, 9)
                Player.gr = False
            elif Player.gd == True:
                Player = player(Player.ox, 5, 9)
                Player.gd = False
            
        def main():
            while True:
                
                rid = False
                display.fill((107, 107, 107))
                print(Game.keysleft)
                Player.main()
                Door.main()

                for wall in Walls:
                    wall.main()
                for Key in Keys:
                    Key.main()

                for Key in Keys:
                    if Player.x > Key.x and Player.x < Key.x + 25 and Player.y > Key.y and Player.y < Key.y + 25:
                        Keys.remove(Key)
                        rid = True
                    if rid == True:
                        Game.keysleft -= 1
                        rid = False
                        
                if Game.keysleft == 0:
                    Door.unlocked == True
                if Door.unlocked == True and Player.csnum == Door.snum and Player.x > Door.x and Player.x < Door.x + 50 and Player.y > Door.y and Player.y < Door.y + 50:
                    textsurface = myfont.render("You Won!", False, (0,255,255))
                    display.blit(textsurface, (50,250))
                    print("weewoo")

                for wall in Walls:
                    if Player.x > wall.x and Player.x < wall.x + wall.width and Player.y > wall.y and Player.y < wall.y + wall.length:
                        textsurface = myfont.render("You Died", False, (0,255,255))
                        pygame.time.wait(3000)
                        Game.reset = 0
                        Game.change = 0
                        return False
                
                if Player.x >= 400:
                    Player.csnumo = Player.csnum
                    Player.oy = Player.y
                    Player.csnum += 1
                    Player.gr = True
                    return False
                if Player.x <= 0:
                    Player.csnumo = Player.csnum
                    Player.oy = Player.y
                    Player.csnum -= 1
                    Player.gl = True
                    return False
                if Player.y >= 400:
                    Player.csnumo = Player.csnum
                    Player.ox = Player.x
                    Player.csnum += 3
                    Player.gd = True
                    return False
                if Player.y <= 0:
                    Player.csnumo = Player.csnum
                    Player.ox = Player.x
                    Player.csnum -= 3
                    Player.gu = True
                    return False
            
                clock.tick(24)
                pygame.display.update()

        main()
