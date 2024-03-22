if csnum == 1:
    Walls = [wall(0, 0, 75, 400), wall(0, 0, 400, 75), wall(75, 300, 100, 175), wall(350, 225, 50, 175), wall(350, 75, 50, 100), wall(125, 125, 100, 100)]
    if Player.gl == True:
        Player = player(375, Player.oy)
        Player.gl == False
    elif Player.gu == True:
        Player = player(Player.ox, 375)
        Player.gu = False
    elif Player.gr == True:
        Player = player(5, Player.oy)
        Player.gr = False
    elif Player.gd == True:
        Player = player(Player.ox, 5)
        Player.gd = False

if csnum == 2:
    Walls = [wall(0, 0, 75, 400), wall(0, 75, 100, 150), wall(225, 0, 175, 150), wall(250, 75, 300, 150)]
    if Player.gl == True:
        Player = player(375, Player.oy)
        Player.gl == False
    elif Player.gu == True:
        Player = player(Player.ox, 375)
        Player.gu = False
    elif Player.gr == True:
        Player = player(5, Player.oy)
        Player.gr = False
    elif Player.gd == True:
        Player = player(Player.ox, 5)
        Player.gd = False
if csnum == 3:
    Walls = [wall(0, 0, 250, 250), wall(0, 250, 150, 50), wall(275, 0, 75, 125), wall(325, 75, 325, 75), wall(150, 300, 100, 250)]
    Keys = [key(287.5, 87.5, 3)]
    if Player.gl == True:
        Player = player(375, Player.oy)
        Player.gl == False
    elif Player.gu == True:
        Player = player(Player.ox, 375)
        Player.gu = False
    elif Player.gr == True:
        Player = player(5, Player.oy)
        Player.gr = False
    elif Player.gd == True:
        Player = player(Player.ox, 5)
        Player.gd = False
if csnum == 4:
    Walls = [wall(0, 0, 400, 75), wall(0, 0, 50, 250), wall(0, 350, 50, 250), wall(150, 100, 50, 200), wall(150, 250, 50, 200), wall(350, 0, 400, 50), wall(175, 175, 50, 25), wall(250, 175, 50, 25)]
    Doors = [door(200, 175, 4)]
    if Player.gl == True:
        Player = player(375, Player.oy)
        Player.gl == False
    elif Player.gu == True:
        Player = player(Player.ox, 375)
        Player.gu = False
    elif Player.gr == True:
        Player = player(5, Player.oy)
        Player.gr = False
    elif Player.gd == True:
        Player = player(Player.ox, 5)
        Player.gd = False
if csnum == 5:
    Walls = [wall(0, 0, 100, 150), wall(250, 0, 100, 150), wall(350, 100, 50, 50), wall(0, 100, 200, 50), wall(0, 300, 100, 150), wall(150, 375, 25, 100), wall(350, 250, 50, 50), wall(250, 300, 100, 150), wall(150, 150, 100, 100)]
    if Player.gl == True:
        Player = player(375, Player.oy)
        Player.gl == False
    elif Player.gu == True:
        Player = player(Player.ox, 375)
        Player.gu = False
    elif Player.gr == True:
        Player = player(5, Player.oy)
        Player.gr = False
    elif Player.gd == True:
        Player = player(Player.ox, 5)
        Player.gd = False
if csnum == 6:
    Walls = [wall(0, 0, 150, 50), wall(0, 250, 50, 50), wall(0, 300, 100, 400), wall(0, 150, 100, 250), wall(325, 100, 200, 75), wall(100, 125, 150, 50), wall(200, 125, 150, 50)]
    Keys = [key(275,175, 6)]
    if Player.gl == True:
        Player = player(375, Player.oy)
        Player.gl == False
    elif Player.gu == True:
        Player = player(Player.ox, 375)
        Player.gu = False
    elif Player.gr == True:
        Player = player(5, Player.oy)
        Player.gr = False
    elif Player.gd == True:
        Player = player(Player.ox, 5)
        Player.gd = False
if csnum == 7:
    Walls = [wall(0, 0, 50, 250), wall(0, 0, 400, 75), wall(75, 325, 75, 325), wall(75, 200, 75, 100), wall(125, 100, 50, 275), wall(225, 150, 125, 75), wall(350, 0, 150, 50), wall(350, 225, 100, 50), wall(300, 150, 25, 100)]
    Keys = [key(75, 275, 7)]
    if Player.gl == True:
        Player = player(375, Player.oy)
        Player.gl == False
    elif Player.gu == True:
        Player = player(Player.ox, 375)
        Player.gu = False
    elif Player.gr == True:
        Player = player(5, Player.oy)
        Player.gr = False
    elif Player.gd == True:
        Player = player(Player.ox, 5)
        Player.gd = False
if csnum == 8:
    Walls = [wall(0, 0, 75, 400), wall(0, 325, 75, 400), wall(100, 100, 75, 200), wall(100, 225, 75, 200), wall(0, 75, 100, 50), wall(0, 225, 100, 50), wall(350, 75, 100, 50), wall(350, 225, 100, 50)]
    if Player.gl == True:
        Player = player(375, Player.oy)
        Player.gl == False
    elif Player.gu == True:
        Player = player(Player.ox, 375)
        Player.gu = False
    elif Player.gr == True:
        Player = player(5, Player.oy)
        Player.gr = False
    elif Player.gd == True:
        Player = player(Player.ox, 5)
        Player.gd = False
if csnum == 9:
    Walls = [wall(0, 0, 50, 400), wall(0, 0, 175, 100), wall(300, 50, 200, 100), wall(0, 250, 150, 400), wall(0, 225, 25, 200), wall(150, 100, 50, 100), wall(150, 100, 125, 50)]
    if Player.gl == True:
        Player = player(375, Player.oy)
        Player.gl == False
    elif Player.gu == True:
        Player = player(Player.ox, 375)
        Player.gu = False
    elif Player.gr == True:
        Player = player(5, Player.oy)
        Player.gr = False
    elif Player.gd == True:
        Player = player(Player.ox, 5)
        Player.gd = False