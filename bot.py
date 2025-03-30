# This example requires the 'message_content' intent.

import discord
from dotenv import load_dotenv
import os
import logging
from hf import chat_completion

load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")


intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


# In our case, the on_ready() event is called
# when the bot has finished logging in and setting things up
@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")


# the on_message() event is called when the bot has received a message.
@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return
    else:
        # response = chat_completion(message.content)
        response = chat_completion(message.content)
        await message.channel.send(response)


client.run(DISCORD_TOKEN, log_level=logging.DEBUG)
