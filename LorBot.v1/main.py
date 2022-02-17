import discord
import os

#music
from discord.ext import commands

from youtube_dl import YoutubeDL

#/music

import requests
import json
import random
from replit import db
from discord.ext import commands

from numpy.random import randint
from keep_alive import keep_alive

client = discord.Client()

key_words = ["miłego", "miły", "miłym", "czułe"]


@client.event
async def on_ready():
    print('Bot is ready.')


@client.event
async def on_message(message):
    msg = message.content
    if message.author == client:
        return

    if message.content.startswith('-toxic'):
        juser = message.author.id
        zmienna = randint(0, 100)
        s = str(zmienna)
        txt = "`Poziom toksyczności wynosi: " + s + "%`"
        await message.channel.send(txt)

    if message.content.startswith('-simp'):
        juser = message.author.id
        if juser == 621044725230600232:
            zmienna = randint(70, 100)
            s = str(zmienna)
            txt = "`Poziom simpu wynosi: " + s + "%`"
            await message.channel.send(txt)
        else:
            zmienna = randint(0, 100)
            s = str(zmienna)
            txt = "`Poziom simpu wynosi: " + s + "%`"
            await message.channel.send(txt)

    if message.content.startswith('-dick'):
        juser = message.author.id
        if juser == 621044725230600232 or juser == 311945690026606592:
            zmienna = randint(16, 30)
            s = str(zmienna)
            txt = "`Twój kutas ma: " + s + "cm` <:21:831963794867224586>"
            await message.channel.send(txt)
        elif juser == 668507275937316875:
            txt = "`Marysia ty to lepiej cipke pokaż`"
            await message.channel.send(txt)
        else:
            emotka = "<:21:831963794867224586>"
            zmienna = randint(4, 30)
            s = str(zmienna)
            txt = ""
            if zmienna > 15:
                txt = "`Twój kutas ma: " + s + "cm`" + emotka
                await message.channel.send(txt)
            else:
                txt = "`Twój kutas ma: " + s + "cm`"
                await message.channel.send(txt)

    if message.content.startswith('-iq'):
        zmienna = randint(0, 200)
        s = str(zmienna)
        txt = "`Masz: " + s + "iq`"
        await message.channel.send(txt)

    if message.content.startswith('-pussy'):
        zmienna = randint(0, 200)
        s = str(zmienna)
        txt = "`Chętnie zobaczymy :)`"
        await message.channel.send(txt)

    if message.content.startswith('-tilt'):
        zmienna = randint(0, 10)
        s = str(zmienna)

        if (zmienna == 10):
            txt = "`Poziom Szymon ~ Daj sobie spokój na dziś`"
            await message.channel.send(txt)
        elif (zmienna == 9):
            txt = "`Poziom Kacper ~ Dobra ff to nie ma sensu`"
            await message.channel.send(txt)
        elif (zmienna == 8):
            txt = "`Poziom Bartek ~ Wkurwiony jak sam diabeł`"
            await message.channel.send(txt)
        else:
            txt = "`Dziś można grać `"
            await message.channel.send(txt)

    if message.content.startswith('-list tilt'):
        txt1 = "`1.Poziom Szymon ~ Daj sobie spokój na dziś \n2.Poziom Kacper ~ Dobra ff to nie ma sens \n3.Poziom Bartek ~ Wkurwiony jak sam diabeł`"

        await message.channel.send(txt1)

    if message.content.startswith('-thotrate'):
        zmienna = randint(0, 100)
        s = str(zmienna)
        txt = "`thotrate: " + s + "%`"
        await message.channel.send(txt)

    if message.content.startswith('-lorid'):
        zmienna = str(message.author.id)

        txt = "`" + zmienna + "`"
        await message.channel.send(txt)

    if message.content.startswith('-smile'):
        aaa = "Twoja stara to dupa blada"
        embedVar = discord.Embed(title="LorBot",
                                 description=aaa,
                                 color=0x00ff00)
        #embedVar.add_field(name="Field1", value="hi", inline=False)
        #embedVar.add_field(name="Field2", value="hi2", inline=False)
        await message.channel.send(embed=embedVar)

    if message.content.startswith('-test'):
        f = open("mileslowka.txt", "r")
        Lines = f.readlines()
        count = 0
        thislist = []
        for line in Lines:
            count += 1
            thislist.append(line)

        zmienna = randint(0, len(thislist))
        txt = thislist[zmienna]
        await message.channel.send(txt)

    if message.content.startswith('-addtxt'):
        encouraging_mess = msg.split("-addtxt ", 1)[1]
        file_object = open('mileslowka.txt', 'a')
        file_object.write(encouraging_mess + "\n")
        file_object.close()
        await message.channel.send("New message added.")

    if any(word in msg for word in key_words):

        f = open("mileslowka.txt", "r")
        Lines = f.readlines()
        count = 0
        thislist = []
        for line in Lines:
            count += 1
            thislist.append(line)
        user = message.author.mention
        zmienna = randint(0, len(thislist))
        txt = thislist[zmienna]
        embedVar = discord.Embed(title="LorBot",
                                 description=user + txt,
                                 color=0x00ff00)
        await message.channel.send(embed=embedVar)

    if message.content.startswith('-komendy'):
        f2 = open("komendy.txt", "r")
        txtkomenda = f2.readlines()

        count = 0
        ciagznakow = ""
        for line in txtkomenda:
            count += 1
            ciagznakow += line
        embedVar = discord.Embed(title="LorBot - Komendy",
                                 description=ciagznakow,
                                 color=0x00ff00)
        #embedVar.add_field(name="Field2", value="hi2", inline=False)
        await message.channel.send(embed=embedVar)

    if message.content.startswith('-hug'):

        await message.channel.send("https://tenor.com/bpJ0h.gif")

    if message.content.startswith('-sad'):
        await message.channel.send("https://tenor.com/Ulb6.gif")

    if message.content.startswith('-jednorozec'):
        await message.channel.send(
            "https://cdn.discordapp.com/attachments/754459079107412079/854681869827178506/unknown.png"
        )

    if message.content.startswith('-rabbit'):
        await message.channel.send(
            "https://cdn.discordapp.com/attachments/754459079107412079/854432534862626856/unknown.png"
        )

    if message.content.startswith('-qń'):
        await message.channel.send(
            "https://cdn.discordapp.com/attachments/754459079107412079/854850444849315852/received_322974979328752.jpeg"
        )
    if message.content.startswith('-60'):
        await message.channel.send(
            "https://cdn.discordapp.com/attachments/788148287391793192/892511106541686784/received_373078791175589.jpeg"
        )

    if message.content.startswith('-rozlam'):
        text = 'popatrz na to tak\nkto ma ich zintować jak nie ty \npotrzebują Cię \n"Ja idę na bota" ~ Łukasz Grochowiak 2021\nROZŁAM W EKIPIE 2\n"Ja pierdole debilu jebany czemu zbanowałeś zeda" ~ Mateusz Górczak 2021\nROZŁAM W EKIPIE 3\n" Wy macie takie jazdy na bani" ~ Adam Lorek 2021\nROZŁAM W EKIPIE 4\n"Nie trzeba umieć grać jungle żeby zgankować" ~ Kacper Dropek 2021\nROZŁAM W EKIPIE 5"'
        await message.channel.send(text)


621044725230600232
keep_alive()
client.run(os.getenv('TOKEN'))
