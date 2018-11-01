# NOTE
# THIS REQUIRES PYTHON v3.6 

# Python 3.7 introduces breaking changes with async calls which destroys
# the discord package. Trust me, it's a bad day.

import random
import discord
import os
from discord.ext import commands
from discord.ext.commands import Bot
from discord import game

BOT_PREFIX=("?", "!")

# Token Management:
# Best practices include not including the token in the code itself
# As this allows you to store and share your code.

# If you don't care, uncomment the line below,
# comment out the os.environ call and 
# populate the TOKEN variable in code with your token.
#TOKEN = "TOKEN HERE"

# OR set an environment variable called DISCORD_TOKEN (Better)
# This is something you set on your computer, on mac/linux
# via `export DISCORD_TOKEN=token`
# And use the definition below.
TOKEN = os.environ['DISCORD_TOKEN']

client = commands.Bot(command_prefix=BOT_PREFIX)

chat_responses = {
    "fireball":"hot",
    "THUNDERWAVE":"whoosh",
    "MULTIPLE WORD SPELL":"Fuck this shit"
    }


spell_responses = [
        '1',
        '2',
        '3',
        '4',
        '5',
        '6',   
    ]

@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name="studying in the library"))
    print("Logged in as " + client.user.name)

@client.event
async def on_message(message):
    #Don't talk to yourself
    if message.author == client.user:
        return

    # Thanks Juan for cleaner code!
    message_responses = [response for key, response in chat_responses.items() if key.upper() in message.content.upper()]
    response_string = str(' and '.join(message_responses))
    if message_responses:
        await client.send_message(message.channel, content=response_string)

    await client.process_commands(message)


@client.command(name="spell_choice", description="Chooses the appropriate spell for the occasion", aliases=["choose_spell", "spell", "which_spell"], pass_context=True)
async def spell_choice(context):
    await client.send_message(context.message.channel, content=random.choice(spell_responses))

# Actually do the thing
client.run(TOKEN)