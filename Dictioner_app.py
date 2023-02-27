import json
from difflib import get_close_matches

file ="Dictionery_app.json" 

def write_json(data, filename="Dictionery_app.json"):
    with open(filename, "w") as f:
        json.dump(data,f, indent=4)

data={
  "sea":"the expanse of salt water that covers most of the earth's surface and surrounds its land masses.",
  "bird":"a warm-blooded egg-laying vertebrate animal distinguished by the possession of feathers, wings, a beak, and typically by being able to fly.",
  "Car":"a four-wheeled road vehicle that is powered by an engine and is able to carry a small number of people.",
  "girl":"a female child.", "boy": "a male child or youth.", "refrigerator": " a large metal container which is kept cool, usually by electricity, so that food that is put in it stays fresh",
  "gog": "a domesticated carnivorous mammal that typically has a long snout, an acute sense of smell, non-retractable claws, and a barking, howling, or whining voice.",
  "apple":"the round fruit of a tree of the rose family, which typically has thin green or red skin and crisp flesh.",
  "teacher": "a person who teaches, especially in a school.", "house":"a building for human habitation, especially one that consists of a ground floor and one or more upper storeys.",
  "television": "a system for converting visual images (with sound) into electrical signals, transmitting them by radio or other means, and displaying them electronically on a screen.",
  "meat": "the flesh of an animal, typically a mammal or bird, as food (the flesh of domestic fowls is sometimes distinguished as poultry ",
  "desk": "a piece of furniture with a flat or sloping surface and typically with drawers, at which one can read, write, or do other work.",
  "milk": "an opaque white fluid rich in fat and protein, secreted by female mammals for the nourishment of their young.",
  "book":"1.a written or printed work consisting of pages glued or sewn together along one side and bound in covers.\n2.a bound set of blank sheets for writing in.",
  "cake" : "an item of soft sweet food made from a mixture of flour, fat, eggs, sugar, and other ingredients, baked and sometimes iced or decorated",
  "coffe": "a hot drink made from the roasted and ground seeds (coffee beans) of a tropical shrub.",
  "aeroplane": "a powered flying vehicle with fixed wings and a weight greater than that of the air it displaces.",
  "rugby": "a team game played with an oval ball that may be kicked, carried, and passed from hand to hand. Points are scored by grounding the ball behind the opponents' goal line (thereby scoring a try) or by kicking it between the two posts and over the crossbar of the opponents' goal.",
  "perfume": "a fragrant liquid typically made from essential oils extracted from flowers and spices, used to give a pleasant smell to one's body."
}
write_json(data)

data = json.loads(open("Dictionery_app.json").read())

def definition(name):

    name = name.lower()

    if name in data:
        return data[name]

    else:
        return "Wrong search!! Please try again."

def alternative(name):

    name = name.lower()

    alt = input("Do you want to find a close match? Enter Y for Yes and N for No: ")

    if alt == "Y" or alt == "y":

        try:
            print(get_close_matches(name, data.keys())[0])
            print(data[get_close_matches(name, data.keys())[0]])
        except:
            print("")

word = input('Enter the word you want to search: ')

if word.isnumeric():
    print('Your input is not a string, please try again and enter a word to search for.')

else:

    output = definition(word)
    if type(output) == list:
        for item in output:
            print(item)        
    else:
        print(output)

    alternative(word)
