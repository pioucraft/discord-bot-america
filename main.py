import discord
from discord import FFmpegPCMAudio
from discord.ext import commands
from discord import app_commands
import os
import youtube_dl
import json

#set the client and the chdir
intents = discord.Intents().all()
bot = commands.Bot(command_prefix = "!?!", intents = intents)
os.chdir(r"/home/pioucraft/Documents/programinc/discord-bot-main/")

#initialize the bot
@bot.event
async def on_ready():
    print("bot is ready")
    #sync commands
    try:
        synced = await bot.tree.sync()
        print(f"synced {len(synced)} commands")
    except Exception as e:
        print(f"failed to sync commands: {e}")



#/play command
@bot.tree.command(name=f"play", description="le bot va jouer la musique de ton choix")
async def play(interaction: discord.Interaction, music: str):
    if (interaction.user.voice):
        await interaction.response.send_message("je vais faire de mon mieux pour te satisfaire")
        channel = interaction.user.voice.channel
        voice = await channel.connect()
        FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
        YDL_OPTIONS = {'format': 'bestaudio'}
        if music.startswith("https://"):
            #load an url
            with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
                info = ydl.extract_info(music, download=False)
                url2 = info['formats'][0]['url']
        else:
            #search on youtube
            with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
                url = f"ytsearch: {music}"
                info = ydl.extract_info(url, download=False)['entries'][0]
                url2 = info['formats'][0]["url"]
        #play the music
        source = FFmpegPCMAudio(url2, **FFMPEG_OPTIONS)
        player = voice.play(source)

    else:
        await interaction.response.send_message("merci de rejoindre un salon vocal et de réessayer la commande")

#stop the music
@bot.tree.command(name="stop-music", description="le bot va arrêter de jouer la musique")
async def level(interaction: discord.Interaction):
    await interaction.response.send_message("j'essaie d'arrêter la musique")
    if (interaction.user.voice):
        await interaction.guild.voice_client.disconnect()



#show the level of the user
@bot.tree.command(name="level", description="affiche ton niveau ou celui d'un autre utilisateur")
async def level(interaction: discord.Interaction, user: discord.User):
    with open("users.json", "r") as f:
        users = json.load(f)
    
    #set an embed
    embed = discord.Embed(type = "rich", title = "niveau", description = f"{user.mention} est niveau {users[str(user.id)]['level']} et a {users[str(user.id)]['experience']} xp", color=0x2e60aa)
    embed.set_image(url = "https://media.tenor.com/iS-rIkKhpMgAAAAd/god-bless-america-american-flag.gif")
    await interaction.response.send_message(embed=embed)

#show the exact level of the user
@bot.tree.command(name="exactlevel", description="affiche ton niveau exact ou celui d'un autre utilisateur avec des décimales")
async def level(interaction: discord.Interaction, user: discord.User):
    with open("users.json", "r") as f:
        users = json.load(f)
    
    #set an embed
    embed = discord.Embed(type = "rich", title = "niveau exact", description = f"{user.mention} est niveau {str(float(users[str(user.id)]['experience']) ** (1/4))} et a {users[str(user.id)]['experience']} xp", color=0x2e60aa)
    embed.set_image(url = "https://media.tenor.com/iS-rIkKhpMgAAAAd/god-bless-america-american-flag.gif")
    await interaction.response.send_message(embed=embed)


#welcome message
@bot.event
async def on_member_join(member):
    channel = bot.get_channel(1062012487173681152)
    bienvenue = bot.get_channel(1050103281315233852)
    #set an embed
    embed = discord.Embed(type = "rich", title = "bienvenue", description = f"bienvenue {member.mention} sur america, n'oublie pas de regarder {bienvenue.mention}", color=0x2e60aa)
    embed.set_image(url = "https://media.tenor.com/iS-rIkKhpMgAAAAd/god-bless-america-american-flag.gif")
    await channel.send(embed=embed)




#quoifeur and xp
@bot.event
async def on_message(message):
    message.content = message.content
    message.content = message.content.lower()
    message.content = message.content.replace("kwa", "quoi")
    message.content = message.content.replace("qwa", "quoi")
    message.content = message.content.replace("koi", "quoi")
    message.content = message.content.replace("kaka", "caca")
    message.content = message.content.replace("oe", "ouais")
    message.content = message.content.replace(" ", "")
    message.content = message.content.replace("!", "")
    message.content = message.content.replace("?", "")
    message.content = message.content.replace("?", "")
    if not message.author.bot:
            with open("users.json", "r") as f:
                users = json.load(f)
    
            letters = len(message.content)
            if letters > 40:
                letters = 40
            await update_data(users, message.author, letters)
            users[str(message.author.id)]["experience"] = users[str(message.author.id)]["experience"] + letters
            await level_up(users, message.author, message.channel)

            with open("users.json", "w") as f:
                json.dump(users, f)


            if message.content.endswith('quoi'):
                await message.channel.send("feur")
                print("feur")
            if message.content.endswith('non'):
                await message.channel.send("bril")
                print("bril")
            if message.content.endswith('oui'):
                await message.channel.send("stiti")
                print("stiti")
            if message.content.endswith('caca'):
                await message.channel.send("mogus")
                print("mogus")
            if message.content.endswith('ouais'):
                await message.channel.send("stern")
                print("stern")




#update the user data if not in users.json
async def update_data(users, user, letters):
    if not user.bot:
        if not str(user.id) in users:
            users[str(user.id)] = {}
        if not "experience" in users[str(user.id)]:
            users[str(user.id)]["experience"] = letters
            users[str(user.id)]["level"] = 1

#level up the user if enough xp
async def level_up(users, user, channel):
    experience = users[str(user.id)]["experience"]
    lvl_start = users[str(user.id)]["level"]
    lvl_end = int(experience ** (1/4))

    if lvl_start < lvl_end:
        await channel.send("{} a atteint le niveau {}".format(user.mention, lvl_end))
        users[str(user.id)]["level"] = lvl_end

        #add roles
        if lvl_end >= 5 and not discord.utils.get(user.guild.roles, name="americain bg") in user.roles:
            await channel.send("bravo {} tu as atteint le niveau 5, tu vas donc recevoir le role americain bg".format(user.mention))
            await user.add_roles(discord.utils.get(user.guild.roles, name="americain bg"))

        if lvl_end >= 10 and not discord.utils.get(user.guild.roles, name="americain très bg") in user.roles:
            await channel.send("bravo {} tu as atteint le niveau 10, tu vas donc recevoir le role americain très bg".format(user.mention))
            await user.add_roles(discord.utils.get(user.guild.roles, name="americain très bg"))

        if lvl_end >= 15 and not discord.utils.get(user.guild.roles, name="americain ultra mega bg") in user.roles:
            await channel.send("bravo {} tu as atteint le niveau 15, tu vas donc recevoir le role americain ultra mega bg".format(user.mention))
            await user.add_roles(discord.utils.get(user.guild.roles, name="americain ultra mega bg"))
        
        if lvl_end >= 20 and not discord.utils.get(user.guild.roles, name="tah l'americain") in user.roles:
            await channel.send("bravo {} tu as atteint le niveau 20, tu vas donc recevoir le role americain tah l'americain".format(user.mention))
            await user.add_roles(discord.utils.get(user.guild.roles, name="tah l'americain"))
            

'''
politics part

'''
@bot.tree.command(name="drop", description="drop une lootbox avec des politiciens et des armes dedans")
async def drop():
    print("drop")

#run the bot with the token
bot.run(token)