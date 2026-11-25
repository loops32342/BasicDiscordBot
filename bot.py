import discord
import time
from discord.ext import commands
from bot_logic import gen_pass
from bot_logic import flip_coin
# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios
bot = commands.Bot(command_prefix="/",intents=intents)

@bot.event
async def on_ready():
    print(f'Hemos iniciado sesión como {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send("Este es un bot estupido")
@bot.command()
async def bye(ctx):
   await ctx.send("😊")
@bot.command()
async def genpass(ctx,caracteres:int):
   await ctx.send (gen_pass(caracteres))
@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    try:
        await ctx.send(left + right)
    except Exception:
        await ctx.send("Dos numeros son requeridos para esta operacion")
        return
@bot.command()
async def memerandom(ctx):
    image=random.choice(os.listdir("images"))
    with open(f'images/{image}', 'rb') as f:
            picture = discord.File(f)
@bot.command('duck')
async def duck(ctx):
    '''Una vez que llamamos al comando duck, 
    el programa llama a la función get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

bot.run("Tu_Token_Va_Aqui")
