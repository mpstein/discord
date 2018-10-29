import random
import discord
import aiohttp
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
    "FIREBALL":"hot",
    "THUNDERWAVE":"whoosh"
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

    input = message.content.upper()
    if input in chat_responses:
        #Fix this so it searches for substring match, not full
        await client.send_message(message.channel, content=chat_responses[input])
        client.process_commands(message)

    await client.process_commands(message)
 

@client.command(name="spell_choice", description="Chooses the appropriate spell for the occasion", aliases=["choose_spell", "spell", "which_spell"], pass_context=True)
async def spell_choice(context):
    await client.send_message(context.message.channel, content=random.choice(spell_responses))
client.run(TOKEN)