class game:
    def __init__(self,id,line):
        self.id = int(id)
        self.line = line
        maxes = {}
        for res in line.split(":")[1].split(";"):
            for cv in res.split(","):
                lr = cv.split(" ")
                maxes[lr[2]] = max(int(lr[1]),maxes.get(lr[2],0))
        self.maxes = maxes
        

    def __repr__(self):
        return f'"{self.maxes}"'

games = []
with open("input_d2.txt","r") as data:
    for line in data.read().split("\n"):
        print(line)
        games.append(game(line.split(":")[0][5:],line))

accu = 0
for game in games:
    m = game.maxes
    accu = accu + (m.get("blue") * m.get("red") * m.get("green"))
    #if (m.get("blue") <= 14) and (m.get("red") <= 12) and (m.get("green") <= 13):
        #accu = accu + game.id

print(accu)