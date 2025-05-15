'''
This is the test script for the pokemon.py. Will use simple tests such as testing damage, fainting, healing, healing more than needed, and attacking.
'''
from pokemon import Pokemon

def test_taking_damage():
    charmander = Pokemon("Charmander", 100) # creating a pokemon
    charmander.take_damage(99) # taking 50 damage
    assert charmander.hp == 1 # hp should be at 1 after taking 99 damage

def test_faining():
    bulbasaur = Pokemon("Bulbasaur", 100) # another pkmn, (I'm not being very creative here)
    bulbasaur.take_damage(100) # taking 100 damage
    assert bulbasaur.hp == 0 # hp will hit 0...
    assert bulbasaur.fainted == True # ...so he should be knocked out

def test_healing():
    squirtle = Pokemon("Squirtle", 100) # I'm just going through the starters, lol
    squirtle.take_damage(50) # taking 50 damage
    squirtle.heal(20) # healing 20 (used a potion!)
    assert squirtle.hp == 70 # taking 50 damage and healing 20 shoudl be at 70

def test_healing_over():
    squirtle = Pokemon("Squirtle", 100)
    squirtle.heal(20) # Should have hp of 100 instead of going over to 120
    assert squirtle.hp == 100

def test_attack():
    absol = Pokemon("Absol", 100) # why absol? because I think he's cool :p
    attack = absol.attack("Night Slash", 85)
    assert attack == "Absol used Night Slash. It caused 85 damage!"