import random
import json

class player():
    def _init_():
        player.name = "다몬"
        player.level = 1
        
        player.stat={"근력":0, "민첩":0, "체력":0, "지능":0, "지혜":0, "매력":0}
        player.attack = 1
        player.defense = 0
        player.dodge = 0
        
        player.backgoundstory = ""
        player.inven = []
        player.story = ""

    def make_player():
        for (n, val) in player.stat:
            player.stat[n] = random.random(1, 20)
        return

    def saveJson():
        data = {"이름" : player.name,
                "level" : player.level,
                "stat" : player.stat,
                "공격력" : player.attack,
                "방어력" : player.defense,
                "회피" : player.dodge,
                "배경이야기" : player.backgoundstory,
                "inven" : player.inven,
                "story" : ""
                }
        with open("log/history1.json", "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent="\t")
    
class NPC():
    def make_NPC():
        return