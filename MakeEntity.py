import random
import json

class player():
    def __init__(self):
        self.name = "다몬"
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
        self.story = ""

    def make_player(self):
        for n in self.stat:
            # print(n)
            self.stat[n] = random.randint(5, 20)
        self.attack = 5 + self.stat["민첩"]/2     # 무기 데미지를 5로 넣음 나중에 수정할 것
        self.dodge = self.stat["민첩"]/2
        self.Hp = self.Max_Hp = (self.stat["체력"]/2)*8
        # return self.stat

    def saveJson(self):
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
                "inven" : self.inven,
                "story" : self.story
                }
        with open("log/history1.json", "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent="\t")
    
class NPC():
    def make_NPC():
        return