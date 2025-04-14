import os
import discord
import requests
from discord.ext import commands

TOKEN = os.getenv("DISCORD_TOKEN")
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")

bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
    print(f"Bot {bot.user} sudah online!")

@bot.command()
async def cuaca(ctx, *, kota):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={kota}&appid={WEATHER_API_KEY}&units=metric&lang=id"
    data = requests.get(url).json()

    if data.get("cod") != 200:
        await ctx.send("Kota tidak ditemukan.")
        return

    nama = data["name"]
    suhu = data["main"]["temp"]
    deskripsi = data["weather"][0]["description"]

    await ctx.send(f"Cuaca di {nama}: {deskripsi}, suhu {suhu}°C")

bot.run(TOKEN)
