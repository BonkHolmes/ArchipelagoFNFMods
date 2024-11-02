from typing import Optional
from BaseClasses import MultiWorld
from .. import Helpers
from ..Locations import ManualLocation
from ..Items import ManualItem


# Use this if you want to override the default behavior of is_option_enabled
# Return True to enable the category, False to disable it, or None to use the default behavior
def before_is_category_enabled(multiworld: MultiWorld, player: int, category_name: str) -> Optional[bool]:
    if category_name == "Full Combos" or category_name == "Player's Choice":
        selection = Helpers.get_option_value(multiworld, player, "include_full_combos")
        if category_name == "Full Combos":
            if selection == 1:
                return True
            elif selection == 0:
                return False
        if category_name == "Player's Choice":
            if selection == 0:
                return True
            elif selection == 1:
                return False
    if category_name == "Optional":
        if Helpers.get_option_value(multiworld, player, "optional_songs") == 1:
            return True
        else:
            return False
    if category_name == "Little Man":
        if Helpers.get_option_value(multiworld, player, "Include_little") == 1:
            return True
        else:
            return False
    if category_name == "Doki Doki Takeover":
        if Helpers.get_option_value(multiworld, player, "Include_DDT") == 1:
            return True
        else:
            return False
    if category_name == "Hex":
        if Helpers.get_option_value(multiworld, player, "Include_Hex") == 1:
            return True
        else:
            return False
    if category_name == "Mad Virus Attack":
        if Helpers.get_option_value(multiworld, player, "Include_MVA") == 1:
            return True
        else:
            return False
    if category_name == "Shaggy":
        if Helpers.get_option_value(multiworld, player, "Include_Shaggy") == 1:
            return True
        else:
            return False
    if category_name == "Indie Cross":
        if Helpers.get_option_value(multiworld, player, "Include_IC") == 1:
            return True
        else:
            return False
    if category_name == "Impostor":
        if Helpers.get_option_value(multiworld, player, "Include_Impostor") == 1:
            return True
        else:
            return False
    if category_name == "Fnaf 2":
        if Helpers.get_option_value(multiworld, player, "Include_Fnaf2") == 1:
            return True
        else:
            return False
    if category_name == "Mario's Madness":
        if Helpers.get_option_value(multiworld, player, "Include_MM") == 1:
            return True
        else:
            return False
    if category_name == "Geese":
        if Helpers.get_option_value(multiworld, player, "Include_Geese") == 1:
            return True
        else:
            return False
    if category_name == "KOU":
        if Helpers.get_option_value(multiworld, player, "Include_Kou") == 1:
            return True
        else:
            return False
    if category_name == "YTP Invasion":
        if Helpers.get_option_value(multiworld, player, "Include_YTP") == 1:
            return True
        else:
            return False
    if category_name == "Fnaf1":
        if Helpers.get_option_value(multiworld, player, "Include_Fnaf1") == 1:
            return True
        else:
            return False
    if category_name == "Fnaf3":
        if Helpers.get_option_value(multiworld, player, "Include_Fnaf3") == 1:
            return True
        else:
            return False
    if category_name == "Dsides":
        if Helpers.get_option_value(multiworld, player, "Include_Dsides") == 1:
            return True
        else:
            return False
    if category_name == "Scott The Woz":
        if Helpers.get_option_value(multiworld, player, "Include_Scott") == 1:
            return True
        else:
            return False
    if category_name == "Progressive Mod" or category_name == "Weeksanity":
        selection = Helpers.get_option_value(multiworld, player, "experiments")
        if category_name == "Progressive Mod":
            if selection == 0:
                return True
            elif selection == 1:
                return False
        if category_name == "Weeksanity":
            if selection == 1:
                return True
            elif selection == 0:
                return False
    if category_name == "Split Paths":
        if Helpers.get_option_value(multiworld, player, "experiments") == 1:
            return True
        else:
            return False
    return None

# Use this if you want to override the default behavior of is_option_enabled
# Return True to enable the item, False to disable it, or None to use the default behavior
def before_is_item_enabled(multiworld: MultiWorld, player: int, item: ManualItem) -> Optional[bool]:
    return None

# Use this if you want to override the default behavior of is_option_enabled
# Return True to enable the location, False to disable it, or None to use the default behavior
def before_is_location_enabled(multiworld: MultiWorld, player: int, location: ManualLocation) -> Optional[bool]:
    return None
