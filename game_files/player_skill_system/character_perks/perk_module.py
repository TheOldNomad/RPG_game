from game_files.player_skill_system.character_perks.perk import Perk


incel_wrath = Perk(
    name = "Incel Wrath"
    description = "Behold the wrath of the man robbed of his divine sexual energy! 
    """Your damage increases by 5 points every level, but you fail all the checks when speaking with female characters"""
    effect = 5
)

berserker_curse = Perk(
    name = "Berserker Curse"
    description = "No one can stop you! Your chance of dealing a critical damage increases by 10%, 
    """and you gain extra 3 points for all close-range combat skills with every level, 
    but you fail all stealth checks and enemies spot you instantly"""
    effect = 3
)