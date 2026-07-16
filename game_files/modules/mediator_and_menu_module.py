from game_files.attack_mechanic.attack_mediator import AttackMediator
from game_files.healing_mechanic.healing_mediator import HealingMediator
from game_files.inventories.inventory_slot_mediator import InventoryAndActionSlotsMediator
from game_files.menus.player_attack_menu import PlayerAttackMenu
from game_files.menus.monster_attack_menu import MonsterAttackMenu
from game_files.menus.player_healing_menu import PlayerHealingMenu
from game_files.menus.players_action_menu import PlayersActionMenu
from game_files.menus.inventory_menu import InventoryMenu
from game_files.menus.item_pickup_menu import ItemPickUpMenu
from game_files.player_skill_system.skill_tree_menu import SkillTreeMenu


inventory_slot_mediator = InventoryAndActionSlotsMediator()
attack_mediator = AttackMediator()
healing_mediator = HealingMediator()

players_action_menu = PlayersActionMenu()
player_attack_menu = PlayerAttackMenu()
player_healing_menu = PlayerHealingMenu()

monster_attack_menu = MonsterAttackMenu()

inventory_menu = InventoryMenu()
item_pickup_menu = ItemPickUpMenu()
skill_tree_menu = SkillTreeMenu()