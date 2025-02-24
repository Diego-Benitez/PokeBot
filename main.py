import discord
from discord.ext import commands
import requests
import keys

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.command()
async def poke(ctx, arg):
    try:
        pokemon = arg.split(" ", 1)[0].lower()
        result = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon}")
        if result.text == "Not Found":
            await ctx.send("Pokemon no encontrado")
        else:
            image_url = result.json()['sprites']['front_default']
            print(image_url)
            await ctx.send(image_url)

    except Exception as e:
        print("Error: ", e)    

@poke.error
async def error_type(ctx, error):
    if isinstance(error, commands.errors.MissingRequiredArgument):
        await ctx.send("Tienes que pasarme un Pokemon")

@bot.event
async def on_ready():
    print(f"Estamos dentro {bot.user}")

@bot.command()
async def limpiar(ctx):
    await ctx.channel.purge()
    await ctx.send("Mensajes eliminados", delete_after = 3)    

bot.run(keys.TOKEN) 