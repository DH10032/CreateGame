import random
import json
import sys

class enemy():
    def __init__(self, name, level):
        self.level = name
        self.level = level

        if level == 1:
            self.Hp = 10
            self.attack = random.randint(1, 4)

        elif level == 2:
            self.Hp = 20
            self.attack = random.randint(1, 4) + random.randint(1, 4)

        elif level == 3:
            self.Hp = 30
            self.attack = random.randint(1, 6)
        
        elif level == 4:
            self.Hp = 40
            self.attack = random.randint(1, 6) + random.randint(1, 4)

        elif level == 5:
            self.Hp = 50
            self.attack = random.randint(1, 6) + random.randint(1, 6)

# def dataSave(data):
#     with open("log/history1.json", "w", encoding="utf-8") as f:
#             json.dump(data, f, ensure_ascii=False, indent="\t")

# def dataLoad(filename):
#     with open(filename, "r", encoding="utf-8") as f:
#         return json.load(f)
    
for i in range(sys.argv[1]):
    enemy(sys.argv[2])
    print()