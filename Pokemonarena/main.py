import pandas as pd
from Pokemon import Pokemon


def generate_pokemons(pokemon_info, nr_of_pokemons):
    """
    Creates a specific number of pokemons from a given dataframe
    :param pokemon_info: pd.Dataframe
        containing needed info passed to Pokemon class
        has to contain columns : 'name',  'attack', 'defense', 'hp', 'sp_attack', 'sp_defense', 'speed'
    :param nr_of_pokemons: integer
        Number of Pokemons to be created
    :return: list<Pokemon>
        Generated Pokemons
    """
    # random sample of given dataframe
    pokemon_sample = pokemon_info.sample(nr_of_pokemons)
    pokemons = []

    # create pokemons
    for index, row in pokemon_sample.iterrows():
        generated_pokemon = Pokemon(row['name'], row['hp'], row['attack'], row['defense'], row['sp_attack'],
                                    row['sp_defense'], row['speed'])

        pokemons.append(generated_pokemon)

    return pokemons


def main():

    # load data
    pokemon_dataset = pd.read_csv("D:\Studium\Data_Mining\Programs\pokemon\Mining-Pokemon\pokemon.csv", sep=",")
    pokemon_mapping = pd.read_csv("D:\Studium\Data_Mining\Programs\pokemon\Mining-Pokemon\pokemon_mapping.csv", sep=";",
                                  encoding='latin-1')

    # change names to german
    pokemon_dataset['name'] = pokemon_mapping['Deutsch']

    # extract needed information to create a pokemon
    pokemon_info = pokemon_dataset[['name',  'attack', 'defense', 'hp', 'sp_attack', 'sp_defense', 'speed']]

    pokemons = generate_pokemons(pokemon_info, 10)





if __name__ == '__main__':

    main()