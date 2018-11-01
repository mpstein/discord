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
    "MULTIPLE WORD SPELL":"Fuck this shit",
    "multiple asdf asdf":"FUck this shit again",
    "ACID_SPLASH":"A classic first day on the job spell that can melt the face and fur of one target, or two if they're standing close enough. Fail that Dex save and they take 1d6 acid damage.",
    "AID":"If you're feel squishy, this one will give some extra meat to go with your potatoes. 5 hit points added to current and max for 8 hours, that's like one Kobold dagger stab so, yay?",
    "ALARM":"WeeeeOOOOOOOHH WEeeeeeeeOOOOOOOOHH I'm just fuckin with you, but seriously you can rest easy knowing the sound of a hand bell will wake you if anything you don't want to get in tries that shit. But after 8 hours you're back to the old string and cans trick.",
    "ALTER SELF":"For 2nd level this spell is pretty tasty. Up to an hour you can change how you look, yeah sure cool, OR you can get some damn gills and fins and be a merperson. You can also grow claws, fangs or gotdamn spines and get 1d6 damage for those unarmed strikes with a +1 for attack and damage rolls because shit is magic.",
    "ANIMAL FRIENDSHIP":"Be friends with beasts, like it says, but only the really dumb ones with 4 or less Intelligence. The critter has to succeed on a Wisdom save or be charmed by you. You get that thing for 24 hours as long as you don't hurt it or cuddle tooo hard.",
    "ANIMAL_MESSENGER":"Passing love notes has never been easier when Tiny beasts can do it for you. Up to 25 words will be delivered in your voice to the target you describe and only them. They have 24 hours to deliver or your next spell is free. Land animals can travel up to 25 miles in that time and flyers 50 miles, which is slow ass flying.",
    "ANIMAL_SHAPES":"Make your friends mutha fuckin druids for a day! Large or smaller, up to CR 4, shift that shit while keeping your Intelligence Wisdom and Charisma, if you have any. Also this is any number of willing creatures so if a local lord is being a dick to villages, maybe they should all become Wooly Mammoths and stomp some dick.",
    "ANIMATE_DEAD":"Assemble a minor army of skeletons with up to 4 bitches under your control. Raise them from the dead and then command them to do cool shit like take a steaming skeleton dumb on some guys chest...wait...do skeleton's poop? Dang. Okay have them guard a particular corridor. Sooooo exciting. Remember you have up to 24 hours before they don't consider you the boss anymore.",
    "ANIMATE_OBJECTS":"Okay this is cool but to really understand it you're going to have to see a whole table of stats. Basically you can bring to life up to 10 objects to work and fight for you. Medium counts as 2, Large 4, and Huge 8 so don't think you'll have a squad of buildlings backing you up. Whatever you do, for the next minute you can have that construct destruct.",
    "ANTILIFE_SHELL":"10 foot barrier of pure STAY THE FUCK OUT. Anything except undead and robits can't go in but they can still cast spells at you and make attacks through it. But if you're up against a group of thugs with clubs, this is a great spot to waggle your butt without fear of stabbing.",
    "ANTIMAGIC_FIELD":"Vanquish the summoned, turn off magic items and even trick fools into wasting their spell slots because this 10 foot dome is as devoid of magic as Dan's bedroom.",
    "ANTIPATHY_SYMPATHY":"Bring all the boys to the yard or dust off your shoulder with both ends of the magnet for up to 10 days. Really, the idea of everyone leaving you alone sounds pretty fantastic. No bartenders asking you to throw out the unruly gamblers. No pickpockets trying to take your collection of ears. No stupid cleric bumping into you and just ASKING for your axe in his face. Oh sorry, in this scenario you're a barbarian.",
    "ARCANE_EYE":"Invisible floating eye that can travel anywhere, cept thru walls or into the Nine Hells, and see anything, cept thru clothes or that spot you missed shaving apparently.",
    "ARCANE_GATE":"Fancy door"
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