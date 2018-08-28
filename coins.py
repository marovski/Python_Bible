import random
#Super Class Coin
class Coin:
    def __init__(self, rare =False, clean = True, heads = True, **kwargs):

        for key,value in kwargs.items():
            setattr(self,key,value)

        self.rare=rare
        self.is_clean=clean
        self.heads=heads

        if self.rare:
            self.value=self.original_value*1.25
        else:
            self.value=self.original_value

        if self.is_clean:
            self.colour = self.clean_colour
        else:
            self.colour = self.rusty_colour
    

    def rust(self):
        self.colour=self.rusty_colour

    def clean(self):
        self.colour=self.clean_colour
        
    def flip(self):
        self.heads=random.choice([True, False])

   
        
    def __str__(self):
        if self.original_value>=1.00:
            return "£{}Coin".format(int(self.original_value))
        else:
            return "{}p Coin".format(int(self.original_value*100))

    def __del__(self):
        print("Coin Spent!")
        

#Objects of the Class Coin
class One_Pence(Coin):
    def __init__(self):
        data = {"original_value":0.01,
                "clean_colour":"bronze",
                "rusty_colour":"brownish",
                "num_edges" : 1,
                "diameter": 20.3,
                "thickness": 1.52,
                "mass":3.56,
            }
        super().__init__(**data)

class Two_Pence(Coin):
    def __init__(self):
        data = {"original_value":0.02,
                "clean_colour":"bronze",
                "rusty_colour":"brownish",
                "num_edges" : 1,
                "diameter": 25.9,
                "thickness": 1.85,
                "mass":7.12,
            }

        super().__init__(**data)

class Five_Pence(Coin):
    def __init__(self):
        data = {"original_value":0.05,
                "clean_colour":"silver",
                "rusty_colour": None,
                "num_edges" : 1,
                "diameter": 18.0,
                "thickness": 1.77,
                "mass":3.25,
            }
        super().__init__(**data)

    def rust(self):
        self.colour = self.rusty_colour

    def clean(self):
        self.colour = self.clean_colour
        
class One_Pound(Coin):
        
    def __init__(self):
        data = {"original_value":1.00,
                "clean_colour":"Gold",
                "rusty_colour":"greenish",
                "num_edges" : 1,
                "diameter": 22.5,
                "thickness": 3.15,
                "mass":9.5,
            }
        
        super().__init__(**data)

        


coins = [One_Pound(),Five_Pence(),One_Pence(),Two_Pence()]

for coin in coins:
    arguments=[coin, coin.colour, coin.value, coin.diameter, coin.thickness,coin.num_edges, coin.mass]

    string="{} - Colour: {}, Value: {}, Diameter(mm): {}, Thickness(mm): {}, Edges: {}, Weigth: {}".format(*arguments)

    print(string)

