from cls.content import Content
class Raid:
    def __init__(self, raid_type, difficulty, time):
        print(raid_type)
        content = Content(raid_type)
        self.content = content.type
        self.difficulty = difficulty
        self.time = time
        self.MAX_DPS = content.MAX_DPS
        self.MAX_SUP = content.MAX_SUP
        self.dps = []
        self.sup = []

    def __str__(self):
        dpsfull = ""
        supfull = ""
        FULL = "**FULL**"
        if len(self.dps) == self.MAX_DPS:
            dpsfull = FULL
        if len(self.sup) == self.MAX_SUP:
            supfull = FULL
        return f"{self.content} {self.difficulty} raid at {self.time}\n\ndps:{self.dps} {dpsfull}\nsup:{self.sup} {supfull}"

    def apply(self, discord_id, ign, subclass):
        # enforce unique user in raids
        already_enrolled = 0
        for i in self.sup + self.dps:
            if i[0] == discord_id:
                already_enrolled = 1
                break

        
        if already_enrolled:
            return -2 # Already enrolled.
        else:
            if is_sup(subclass):
                if len(self.sup) < self.MAX_SUP:
                    self.sup.append((discord_id, ign, subclass))
                else:
                    return -1 # Error raid full
            else:
                if len(self.dps < self.MAX_DPS):
                    self.dps.append((discord_id, ign, subclass))
                else:
                    return -1 # Error raid full

        return 0

supports = ["bard", "paladin", "artist"]

def is_sup(subclass):
    if subclass in supports:
        return True
    return False
    
