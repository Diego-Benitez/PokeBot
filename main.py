import discord
from discord.ext import commands
import requests
import random
import keys

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

def get_random_pokemon():
    random_id = random.randint(1, 1025) 
    result = requests.get(f"https://pokeapi.co/api/v2/pokemon/{random_id}")
    if result.status_code == 200:
        return result.json()
    return None

def format_stats(stats):
    stats_dict = {
        "hp": stats[0]['base_stat'],
        "ataque": stats[1]['base_stat'],
        "defensa": stats[2]['base_stat'],
        "ataque_especial": stats[3]['base_stat'],
        "defensa_especial": stats[4]['base_stat'],
        "velocidad": stats[5]['base_stat']
    }
    return stats_dict

@bot.command()
async def poke(ctx, *, arg=None):
    try:
        if arg is None:
            data = get_random_pokemon()
            if not data:
                await ctx.send("No se pudo encontrar un Pokémon aleatorio.")
                return
        else:
            pokemon = arg.split(" ", 1)[0].lower()
            result = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon}")
            if result.status_code == 404:
                await ctx.send("Pokémon no encontrado. Generando uno aleatorio...")
                data = get_random_pokemon()
                if not data:
                    await ctx.send("No se pudo encontrar un Pokémon aleatorio.")
                    return
            else:
                data = result.json()

        name = data['name'].capitalize()
        image_url = data['sprites']['front_default']
        types = ", ".join([t['type']['name'].capitalize() for t in data['types']])
        stats = format_stats(data['stats'])

        embed = discord.Embed(title=name, description=f"Tipo(s): {types}")
        embed.set_image(url=image_url)
        embed.add_field(name="HP", value=stats['hp'], inline=True)
        embed.add_field(name="Ataque", value=stats['ataque'], inline=True)
        embed.add_field(name="Defensa", value=stats['defensa'], inline=True)
        embed.add_field(name="Ataque Especial", value=stats['ataque_especial'], inline=True)
        embed.add_field(name="Defensa Especial", value=stats['defensa_especial'], inline=True)
        embed.add_field(name="Velocidad", value=stats['velocidad'], inline=True)

        await ctx.send(embed=embed)

    except Exception as e:
        print("Error: ", e)
        await ctx.send("Hubo un error al procesar tu solicitud.")
    
@poke.error
async def error_type(ctx, error):
    if isinstance(error, commands.errors.MissingRequiredArgument):
        await ctx.send("Tienes que pasarme un Pokemon o digita tu nombre para que se genere uno aleatorio...")

@bot.event
async def on_ready():
    print(f"Estamos dentro {bot.user}")

@bot.command()
async def limpiar(ctx):
    await ctx.channel.purge()
    await ctx.send("Mensajes eliminados", delete_after = 3)    

bot.run(keys.TOKEN) 
