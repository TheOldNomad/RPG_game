import random

from game_files.entities.damage_dealing_entity import DamageDealingEntity
from game_files.items_and_inventories.inventory_slot_mediator import InventoryAndActionSlotsMediator
from game_files.items_and_inventories.player_inventory import ArmorSlots, Inventory, WeaponSlots


class Player(DamageDealingEntity):
    rpg_class: str

    def __init__(self, given_name: str, given_rpg_class: str):
        self.name = given_name
        self.rpg_class = given_rpg_class
        self.health_points = 60
        self.damage = random.randint(45, 90)
        self.health_regeneration = 30
        self.alive = True
        self.damage_stockphrases = ["Motherfucker", "Uuu suka", "You wanker", "Fuck, I'm bleeding"]
        self.death_stockphrases = ["Uuu suka", "I'm seeing stars...", "Bratan, this is fiasco", "I will meet Reagan.."]
        self.armor_slots = ArmorSlots()
        self.weapon_slots = WeaponSlots()
        self.inventory = Inventory()
        self.item_equipment_mechanic = InventoryAndActionSlotsMediator()
