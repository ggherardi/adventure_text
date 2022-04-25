class Equipment:
    def __init__(self, head, body, left_arm, right_arm, hands, legs, feet, back, weapon_1, weapon_2):
        self.head = head
        self.body = body
        self.left_arm = left_arm
        self.right_arm = right_arm
        self.hands = hands
        self.legs = legs
        self.feet = feet
        self.back = back
        self.weapon_1 = weapon_1
        self.weapon_2 = weapon_2
        
    def __init__(self, json_equipment):
        pass #implement equipment init from json here

class Actor:
    def __init__(self, max_hp, current_hp, str, con, dex, wil, int, cha, equip):
        self.max_hp = max_hp
        self.current_hp = current_hp
        self.str = str
        self.con = con
        self.dex = dex
        self.wil = wil
        self.int = int
        self.cha = cha
        self.equip = equip