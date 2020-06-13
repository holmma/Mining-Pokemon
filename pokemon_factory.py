from Pokemonarena.Pokemon import Pokemon


class Pokemon_Factory:
    def __init__(self, pokemon_df, columns):
        self.pokemon_df = pokemon_df
        self.columns = columns

    def create_Pokemon(self, number):
        poke_dict = self.pokemon_df[self.pokemon_df['Id']
                                    == number][self.columns].to_dict('records')[0]
        return Pokemon(**poke_dict)

    def create_Pokemon_Samples(self, nr_of_pokemons):
        pokemon_sammples = self.pokemon_df.sample(nr_of_pokemons)['Id']
        pokemons = []
        for d, i in enumerate(pokemon_sammples):
            pokemons.append(self.create_Pokemon(i))
        return pokemons
