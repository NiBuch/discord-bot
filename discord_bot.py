#!/usr/bin/python3

import configparser
import json
import random
import regex
import requests
from discord import Game
from discord.ext.commands import Bot

## Some initializations/loading/seeding
random.seed()

## Load configuration
config = configparser.ConfigParser()
config.read("config.ini")

BOT_PREFIX = tuple(config['DISCORD']['PREFIX'].split(","))
TOKEN = config['DISCORD']['TOKEN']


client = Bot(command_prefix=BOT_PREFIX)


######################
#### Bot Commands ####
######################

@client.command(name = "8ball",
                description = "Answer a yes/no question.",
                brief = "Answers ex machina.",
                aliases = ["eight_ball", "eightball", "8-ball"],
                pass_context = True)
async def eight_ball(context):
    ynm = ["absolutely", "always", "maybe", "never", "no", "possibly", "sometimes", "yes"]
    # '@#$' is a placeholder token for our yes/no/maybe
    answers = ["@#$, @#$, @#$!",
               "@#$, but not for the reasons you'd think.",
               "All I know is my gut says @#$.",
               "Definitely @#$.",
               "I think @#$, considering the facts.",
               "Signs point to @#$.",
               "That's a soft @#$."
              ]

    channel = context.channel
    await channel.send(context.author.mention + ": " + random.choice(answers).replace("@#$", random.choice(ynm)).capitalize())


@client.command(name = "dice",
                description = "Roll a dice.",
                brief = "Roll a dice.",
                aliases = ["d", "roll"],
                pass_context = True)
async def dice(context):


@client.command(name = "pokedex",
                description = "Look up information on a Pokemon.",
                brief = "Ask the Pokedex.",
                aliases = ["elm", "oak", "poke"],
                pass_context = True)
async def pokedex(context):
    uri = "https://pokeapi.co/api/v2/pokemon-species/"
    resp = requests.get(uri)

    data = resp.text
    data = data['flavor_text_entries']
    data = [x['flavor_text'] for x in data if x['language']['name'] == 'en']
    channel = context.channel
    await channel.send(context.author.mention + ": " + random.choice(data))

client.run(TOKEN)
