# Object classes from AP that represent different types of options that you can create
from Options import FreeText, NumericOption, Toggle, DefaultOnToggle, Choice, TextChoice, Range, NamedRange, OptionList

# These helper methods allow you to determine if an option has been set, or what its value is, for any player in the multiworld
from ..Helpers import is_option_enabled, get_option_value



####################################################################
# NOTE: At the time that options are created, Manual has no concept of the multiworld or its own world.
#       Options are defined before the world is even created.
#
# Example of creating your own option:
#
#   class MakeThePlayerOP(Toggle):
#       """Should the player be overpowered? Probably not, but you can choose for this to do... something!"""
#       display_name = "Make me OP"
#
#   options["make_op"] = MakeThePlayerOP
#
#
# Then, to see if the option is set, you can call is_option_enabled or get_option_value.
#####################################################################


# To add an option, use the before_options_defined hook below and something like this:
#   options["total_characters_to_win_with"] = TotalCharactersToWinWith
#
class include_full_combos(Choice):
    """
    Full Combos are considered checks, (Replaces Player's Choice)
    """
    display_name = "Include Full Combos?"
    option_false = 0
    option_true = 1
    default = 0
    
class optional_songs(Choice):
    """
    Songs after the Victory Token will be added to the locations pool.
    """
    display_name = "Include Optional Songs?"
    option_false = 0
    option_true = 1
    default = 0

class Include_little(Choice):
  """Choose to have the Little man mod be included (Placeholder)"""
  display_name = "Include Little Man?"
  option_false = 0
  option_true = 1
  default = 0

class Include_DDT(Choice):
    """Choose to have the Doki Doki Takeover Mod be included (Placeholder)"""
    display_name = "Include Doki Doki Takeover?"
    option_false = 0
    option_true = 1
    default = 0

class Include_MVA(Choice):
    """Choose the have the Mad Virus Attack Mod be included (Placeholder)"""
    display_name = "Include Mad Virus Attack?"
    option_false = 0
    option_true = 1
    default = 0

class Include_Impostor(Choice):
    """Choose to have the Impostor Mod be included (Placeholder)"""
    display_name = "Include Impostor?"
    option_false = 0
    option_true = 1
    default = 0

class Include_Shaggy(Choice):
    """Choose to have the Shaggy Mod be included (Placeholder)"""
    display_name = "Include Shaggy?"
    option_false = 0
    option_true = 1
    default = 0

class Include_Fnaf2(Choice):
    """Choose to have the Fnaf 2 Mod be included (Placeholder)"""
    display_name = "Include Fnaf2?"
    option_false = 0
    option_true = 1
    default = 0

class Include_Kou(Choice):
    """Choose to have the Kou Mod be included (Placeholder)"""
    display_name = "Include Kou?"
    option_false = 0
    option_true = 1
    default = 0

class Include_MM(Choice):
    """Choose to have the Mario's Madness Mod be included (Placeholder)"""
    display_name = "Include Mario's Madness?"
    option_false = 0
    option_true = 1
    default = 0

class Include_Hex(Choice):
    """Choose to have the Hex Mod be included (Placeholder)"""
    display_name = "Include Hex?"
    option_false = 0
    option_true = 1
    default = 0

class Include_IC(Choice):
    """Choose to have the Indie Cross Mod be included (Placeholder)"""
    display_name = "Include Indie Cross?"
    option_false = 0
    option_true = 1
    default = 0

class Include_Geese(Choice):
    """Choose to have the UniqueGeese Mod be included (Placeholder)"""
    display_name = "Include UniqueGeese?"
    option_false = 0
    option_true = 1
    default = 0
    
class Include_YTP(Choice):
    """(FLASHING LIGHTS WARNING) Do you want YTP Invasion to be added? (Placeholder, rework in the works, just taking longer than expected)"""
    display_name = "Include YTP Invasion?"
    option_false = 0
    option_true = 1
    default = 0
    
class Include_Fnaf1(Choice):
    """Do you want the Fnaf1 mod to be added? (Placeholder, rework in the works, just taking longer than expected)"""
    display_name = "Include Fnaf1?"
    option_false = 0
    option_true = 1
    default = 0
    
class Include_Dsides(Choice):
    """Do you want the DSides remix mod to be added? (Placeholder, rework in the works, just taking longer than expected)"""
    display_name = "Include Dsides?"
    option_false = 0
    option_true = 1
    default = 0
    
class Include_Scott(Choice):
    """Do you want the Scott the Woz mod to be added? (Placeholder, rework in the works, just taking longer than expected)"""
    display_name = "Include Scott?"
    option_false = 0
    option_true = 1
    default = 0

class Include_Fnaf3(Choice):
    """Do you want the Fnaf3 mod to be added? (Placeholder, rework in the works, just taking longer than expected)"""
    display_name = "Include Fnaf3?"
    option_false = 0
    option_true = 1
    default = 0
class experiments(Choice):
    """Should WIPs be added to logic, (warning it may be flawed)."""
    display_name = "Experiments"
    option_false = 0
    option_true = 1
    default = 0
class afterdark(Choice):
    """Only activate this if you are in the AP AD server"""
    display_name = "Afterdark?"
    option_false = 0
    option_true = 1
    default = 0

# This is called before any manual options are defined, in case you want to define your own with a clean slate or let Manual define over them
def before_options_defined(options: dict) -> dict:
    options["include_full_combos"] = include_full_combos
    options["optional_songs"] = optional_songs
    options["Include_little"] = Include_little
    options["Include_DDT"] = Include_DDT
    options["Include_Fnaf2"] = Include_Fnaf2
    options["Include_Geese"] = Include_Geese
    options["Include_Fnaf1"] = Include_Fnaf1
    options["Include_IC"] = Include_IC
    options["Include_Impostor"] = Include_Impostor
    options["Include_Fnaf3"] = Include_Kou
    options["Include_YTP"] = Include_YTP
    options["Include_Dsides"] = Include_Dsides
    options["Include_Shaggy"] = Include_Shaggy
    options["Include_Scott"] = Include_Scott
    options["experiments"] = experiments
    return options

# This is called after any manual options are defined, in case you want to see what options are defined or want to modify the defined options
def after_options_defined(options: dict) -> dict:
    return options