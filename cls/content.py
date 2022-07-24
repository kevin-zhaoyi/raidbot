class Content:
    def __init__(self, raid_type):
            
        self.type = raid_type

        if self.type == "kakul-sadon":
            self.MAX_DPS = 3
            self.MAX_SUP = 1
        else:
            self.MAX_DPS = 6
            self.MAX_SUP = 2
    
