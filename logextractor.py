log = open("20160312110436-HELIOS_base_1-vs-YuShan2015_2.rcg" , "rt")
lines = list()
for l in log:
    if l.find("show") != -1: # or l.find("playmode") != -1: or l.find("(team 1") != -1:    
        lines.append(l)

class player:
    def __init__(self,name,unum,Type,x, y, vx, vy, kick, dash,catch):
        self.name = name
        self.unum = unum
        self.Type = Type
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.kick = kick
        self.dash = dash
        self.catch = catch

class ball:
    def __init__(self,x, y, vx, vy):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
class cycle:
    def __init__(self,show,ball,lplayer,rplayer):
        self.show = show
        self.ball = ball
        self.lplayer = lplayer
        self.rplayer = rplayer
# data = lines[1].split(" ")
# for i in range(len(data)):
#     print(i , data[i])
# # for k in range(0,712,33):
# #     i = 712 - k
# #     data.pop(i)
# #     data.pop(i)
# #     data.pop(i)
# for i in range(len(data)):
#     print(i , data[i])
cycles = list()
for l in lines:
    # print(l)
    isfocus = False
    if l.find("(f") != -1:
        isfocus = True
    data = l.split(" ")
    if isfocus:
        # for k in range(0,712,33):
        #     i = 712 - k
        #     data.pop(i)
        #     data.pop(i)
        #     data.pop(i)
        # data.pop(26)
        # data.pop(26)
        # data.pop(26)
        for _ in range(data.count("(f")):
            i = data.index("(f")
            data.pop(i)
            data.pop(i)
            data.pop(i)
    print(data)
    for i in range(len(data)):
        print(i , data[i])
    data.pop(0)
    show = int(data[0]) #which cycle
    data.pop(0)
    data.pop(0)
    b = ball(float(data[0]),float(data[1]),float(data[2]),float(data[3][:-1]))
    data.pop(0)
    data.pop(0)
    data.pop(0)
    data.pop(0)
    lplayer = list()
    for i in range(0,11):
        print(data)
        name = "l"
        data.pop(0)
        print(data[0])
        unum = int(data[0][:-1])
        data.pop(0)
        Type = int(data[0])
        data.pop(0)
        data.pop(0)
        x = float(data[0])
        data.pop(0)
        y = float(data[0])
        data.pop(0)
        vx = float(data[0])
        data.pop(0)
        vy = float(data[0])
        data.pop(0)
        for _ in range(11):
            data.pop(0)
        kick = int(data[0])
        data.pop(0)
        dash = int(data[0])
        data.pop(0)
        data.pop(0)
        catch = int(data[0])
        data.pop(0)
        for _ in range(7):
            data.pop(0)
        lplayer.append(player(name, unum, Type, x, y, vx, vy, kick, dash, catch))
    rplayer = list()
    for i in range(11):
        print(data)
        name = "r"
        data.pop(0)
        print(data[0])
        unum = int(data[0][:-1])
        data.pop(0)
        Type = int(data[0])
        data.pop(0)
        data.pop(0)
        x = float(data[0])
        data.pop(0)
        y = float(data[0])
        data.pop(0)
        vx = float(data[0])
        data.pop(0)
        vy = float(data[0])
        data.pop(0)
        for _ in range(11):
            data.pop(0)
        kick = int(data[0])
        data.pop(0)
        dash = int(data[0])
        data.pop(0)
        data.pop(0)
        catch = int(data[0])
        data.pop(0)
        for _ in range(7):
            data.pop(0)
        rplayer.append(player(name, unum, Type, x, y, vx, vy, kick, dash, catch))
    cycles.append(cycle(show, ball, lplayer, rplayer))
print(cycles)
    