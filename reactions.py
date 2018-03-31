# Hier werden alle User Reaction Commands gehandled.

import discord
import requests
import asyncio
import random
import io
import sys
import keys
from pxldrn import adv

client = discord.Client()
messageid = None
messageuserid = None
mods = open("config/mods.txt", "r", encoding='utf-8')

@client.event
async def on_ready():
    print('Eingeloggt als')
    print(client.user.name)
    print(client.user.id)
    print('------------------------')

@client.event
async def on_message(message):
    # Zufälliges "falsches" Zitat
    if message.content.lower().startswith('p.zitat'):
        await client.send_message(message.channel, adv.zitate())

    # Zitat hinzufügen
    if message.content.lower().startswith('p.schreiben'):
        zitat = message.content[12:]
        await client.send_message(message.channel, adv.schreiben(zitat))

    # Coinflip
    if message.content.lower().startswith('p.coin'):
        await client.add_reaction(message, adv.coin())

    # Ab hier muss umgebaut werden
    if message.content.lower().startswith('p.ja'):
        choice = random.randint(1, 4)
        if choice == 1:
            response = requests.get('https://media.giphy.com/media/A3dD2XWfJ7tV6/giphy.gif', stream=True)
            await  client.send_file(message.channel, io.BytesIO(response.raw.read()), filename="ja.gif")
        if choice == 2:
            response = requests.get('https://media.giphy.com/media/XMBJ0l20sNWEM/giphy.gif', stream=True)
            await  client.send_file(message.channel, io.BytesIO(response.raw.read()), filename="ja.gif")
        if choice == 3:
            response = requests.get('https://media.giphy.com/media/BlVVi6LGpZZ7O/giphy.gif', stream=True)
            await  client.send_file(message.channel, io.BytesIO(response.raw.read()), filename="ja.gif")
        if choice == 4:
            response = requests.get('https://media.giphy.com/media/dZWJ0MdlA6W9W/giphy.gif', stream=True)
            await  client.send_file(message.channel, io.BytesIO(response.raw.read()), filename="ja.gif")

    if message.content.lower().startswith('p.nein'):
        response = requests.get('https://media.giphy.com/media/eXQPwwE8DFTZS/200w_d.gif', stream=True)
        await  client.send_file(message.channel, io.BytesIO(response.raw.read()), filename="nein.gif")

    if message.content.lower().startswith('p.tableflip'):
        response = requests.get('https://media.giphy.com/media/uKT0MWezNGewE/giphy.gif', stream=True)
        await  client.send_file(message.channel, io.BytesIO(response.raw.read()), filename="pixie.gif")

    if 'porg' in message.content.lower():
        response = requests.get('https://media.giphy.com/media/3ohhwqOVlEbBxEbss0/giphy.gif', stream=True)
        await client.send_file(message.channel, io.BytesIO(response.raw.read()), filename="porg.gif")

    if message.content.lower().startswith('p.halt') and message.author.id == keys.pmcid:
        await client.logout()
        await asyncio.sleep(1)
        sys.exit(1)


client.run(keys.token)
