# Lib
import discord
from aioconsole import ainput

client = discord.Client()

# Logging
import logging

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

# On ready notification
@client.event
async def on_ready():
    print("Ready to lock-on\n")
    
# The only function
@client.event
async def on_message(message):
    if (message.content.startswith('Welcome home, EchoBot.')):
        TargetChannel = message.channel
        while True:
            response = await ainput("> ")
            await TargetChannel.send(response)
    
# Run
client.run("Your token here")
