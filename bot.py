import discord
import time
from bot_logic import gen_pass
from bot_logic import flip_coin
# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Hemos iniciado sesión como {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send("Hi!")
    elif message.content.startswith('$bye'):
        await message.channel.send("👌")
    elif message.content.startswith('$password'):
        await message.channel.send(gen_pass(15))
    elif message.content.startswith("$Coin Flip"):
        await message.channel.send(flip_coin())
    else:
        await message.channel.send(message.content)
        time.sleep(0.5)
        await message.channel.send("Lol! No puedo hacer eso bobo.Este mensaje esta hecho para personas que piensan en que en este bot hay comandos infinitos y no es asi.")

client.run("Aqui Va el token")
