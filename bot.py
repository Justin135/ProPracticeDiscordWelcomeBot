# bot.py
import os
import discord
import json
import time
from discord.ext.commands import Cog

with open(os.path.abspath(os.path.join(os.path.dirname("piSpam.py"), "secret.json"))) as f:
    data = json.load(f)

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)


@client.event
async def on_member_join(member):
    time.sleep(2)
    await client.get_channel(837575124101759006).send(f"Welcome to the ProPractice server, {member.mention}!")
    time.sleep(1)
    await client.get_channel(837575124101759006).send(f"{member.mention} To gain full access to the server, please change your nickname to your real name so the admins can recognize you.\n\n")
    time.sleep(1)
    await client.get_channel(837575124101759006).send(f"On PC: Simply right-click the server logo or click on the server name at the top left portion of the screen, and click \"Change Nickname\".")
    time.sleep(1)
    await client.get_channel(837575124101759006).send(f"On Mobile: While viewing the channels, click on the server name at the top of the screen and click \"Change Nickname\".")
    time.sleep(1)
    await client.get_channel(837575124101759006).send(f"After this, an admin will be able to recognize you and verify you!")
    time.sleep(1)
    await client.get_channel(837575124101759006).send(f"{member.mention} If you are having problems with changing your nickname, then you can simply type your name in this channel.")
    time.sleep(1)
    await client.get_channel(837575124101759006).send(f"{member.mention} Please be patient as it can take some time to verify each member!")
    


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord right now!')

client.run(data['token'])