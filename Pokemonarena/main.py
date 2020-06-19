import pandas as pd
from Pokemon import Pokemon
from Fight import Fight

# Main
def main():

    # Load the files
    pokemon_dataset = pd.read_csv("D:\Dokumente\Programmieren\VS Code\Mining-Pokemon\pokemon.csv", sep=",")
    pokemon_mapping = pd.read_csv("D:\Dokumente\Programmieren\VS Code\Mining-Pokemon\pokemon_mapping.csv", sep=";", encoding='latin-1')

    # Map the Pokemon names with german names
    pokemon_dataset['name'] = pokemon_mapping['Deutsch']

    # Get the importen informations of the data set
    pokemon_info = pokemon_dataset[['name',  'attack', 'defense', 'hp', 'sp_attack', 'sp_defense', 'speed']]

    # Create all pokemon
    pokemons = create_all_pokemon(pokemon_info)

    # Lets all Pokemons fight
    # fight(pokemons)

    # Check all Pokemons stats
    check_all_stats(pokemons)

    # Done
    print("Done!")



# Check all Pokemons stats
def check_all_stats(pokemons):

    # Max
    max_defense = 0
    max_specialDefense = 0
    max_attack = 0
    max_specialAttack = 0

    # Min
    min_defense = 1000
    min_specialDefense = 1000
    min_attack = 1000
    min_specialAttack = 1000

    # Average
    average_defense = 0
    average_specialDefense = 0
    average_attack = 0
    average_specialAttack = 0

    # Finde die min und max werte für die Stats
    for pokemon in pokemons:

        # Steck average
        average_defense += pokemon.defense
        average_specialDefense += pokemon.specialDefense
        average_attack += pokemon.attack
        average_specialAttack += pokemon.specialAttack

        # Max stats:
        # Maximale defense
        if max_defense < pokemon.defense: 
            max_defense = pokemon.defense
                
        # Maximale specialDefense
        if max_specialDefense < pokemon.specialDefense: 
            max_specialDefense = pokemon.specialDefense
                
        # Maximale attack
        if max_attack < pokemon.attack: 
            max_attack = pokemon.attack
                
        # Maximale specialAttack
        if max_specialAttack < pokemon.specialAttack: 
            max_specialAttack = pokemon.specialAttack
                        
        # Min stats: 
        # Minimale defense
        if min_defense > pokemon.defense: 
            min_defense = pokemon.defense
                
        # Minimale specialDefense
        if min_specialDefense > pokemon.specialDefense: 
            min_specialDefense = pokemon.specialDefense
                
        # Minimale attack
        if min_attack > pokemon.attack: 
            min_attack = pokemon.attack
                
        # Minimale specialAttack
        if min_specialAttack > pokemon.specialAttack: 
            min_specialAttack = pokemon.specialAttack

    # Calculate average
    average_defense = round(average_defense / len(pokemons))
    average_specialDefense = round(average_specialDefense / len(pokemons))
    average_attack = round(average_attack / len(pokemons))
    average_specialAttack = round(average_specialAttack / len(pokemons))

    # Show the results
    print("Max: Attack = " + str(max_attack) + " | Spezial Attack = " + str(max_specialAttack) + " | Deffense = " + str(max_defense) + " | Spezial Deffense = " + str(max_specialDefense))
    print("Min: Attack = " + str(min_attack) + " | Spezial Attack = " + str(min_specialAttack) + " | Deffense = " + str(min_defense) + " | Spezial Deffense = " + str(min_specialDefense))
    print("Avg: Attack = " + str(average_attack) + " | Spezial Attack = " + str(average_specialAttack) + " | Deffense = " + str(average_defense) + " | Spezial Deffense = " + str(average_specialDefense))


# Let all Pokemons fight
def fight(pokemons):

    # Lets all pokemons fight Pokemon 1
    for pokemon1 in pokemons:

        # Lets all pokemons fight Pokemon 2
        for pokemon2 in pokemons:
            
            # Create fight
            arena = Fight(pokemon1, pokemon2)

            # Show winner
            print(arena.fight_ml())



# Create all pokemons
def create_all_pokemon(pokemon_info):
    
    # Return: Holds all pokemons
    all_pokemons = []
    
    # create all pokemons from the list
    for index, row in pokemon_info.iterrows():
        # Create pokemon
        generated_pokemon = Pokemon(row['name'], row['hp'], row['attack'], row['defense'], row['sp_attack'],row['sp_defense'], row['speed'])
        # Add pokemon to the list
        all_pokemons.append(generated_pokemon)

    # Return all pokemons
    return all_pokemons



# Create pokemon
def generate_pokemons(pokemon_info, nr_of_pokemons):

    # random sample of given dataframe
    pokemon_sample = pokemon_info.sample(nr_of_pokemons)
    pokemons = []

    # create pokemons
    for index, row in pokemon_sample.iterrows():
        generated_pokemon = Pokemon(row['name'], row['hp'], row['attack'], row['defense'], row['sp_attack'],
                                    row['sp_defense'], row['speed'])

        pokemons.append(generated_pokemon)

    return pokemons



# Main
if __name__ == '__main__':
    # Start main
    main()