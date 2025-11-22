import random
import json
import sys

filename = "log/history1.json"
lst = []
Loop = True

class player():
    def __init__(self, name):
        self.name = name
        self.level = 1
        self.Hp = 0
        self.Max_Hp = 0
        
        self.stat = {"근력":0, "민첩":0, "체력":0, "지능":0, "지혜":0, "매력":0}
        self.attack = 1
        self.defense = 0
        self.dodge = 0
        self.skill = []
        
        self.backgoundstory = ""
        self.inven = ["일반 카타나"]

    def make_player(self):
        for n in self.stat:
            self.stat[n] = random.randint(5, 20)
        self.attack = 5 + self.stat["민첩"]/2     # 무기 데미지를 5로 넣음 나중에 수정할 것
        self.dodge = self.stat["민첩"]/2
        self.defense = self.stat["체력"]/2
        self.Hp = self.Max_Hp = (self.stat["체력"]/2)*8

    def Data(self):
        data = {"이름" : self.name,
                "level" : self.level,
                "HpMax" : self.Max_Hp,
                "Hp" : self.Hp,
                "stat" : self.stat,
                "공격력" : self.attack,
                "방어력" : self.defense,
                "회피" : self.dodge,
                "skill" : self.skill,
                "배경이야기" : self.backgoundstory,
                "inven" : self.inven 
                }
        return data
    
class NPC():
    def __init__(self, level, name):
        self.name = name
        self.level = level
        self.Hp = 0
        self.Max_Hp = 0
        
        self.attack = 1
        self.dodge = 0
        self.skill = []
        
        self.inven = []

    def make_NPC(self):
        self.attack = 5*self.level
        self.dodge = 2*self.level
        self.Hp = 10*self.level

    def Data(self):
        data = {"이름" : self.name,
                "level" : self.level,
                "HpMax" : self.Max_Hp,
                "Hp" : self.Hp,
                "공격력" : self.attack,
                "회피" : self.dodge,
                "skill" : self.skill,
                "inven" : self.inven 
                }
        return data

def dataSave(data):
    with open("log/history1.json", "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent="\t")

def dataLoad(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)

i = 1
while Loop:
    # print(sys.argv[i])
    if sys.argv[i] == "P":
        P = player(sys.argv[i+1])
        P.make_player()
        lst.append(P.Data())
        i = i+2

    elif sys.argv[i] == "N":
        N = NPC(int(sys.argv[i+1]), (sys.argv[i+2]))
        N.make_NPC()
        lst.append(N.Data())
        i = i+3

    elif sys.argv[i] == "EOF":
        dataSave(lst)
        Loop = False
    