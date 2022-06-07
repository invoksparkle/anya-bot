from dotenv import load_dotenv
import nextcord
from nextcord.ext import commands

load_dotenv()

TESTING_GUILD_ID=813458127310946364

bot = commands.Bot()
@bot.event
async def on_ready():
    print(f'Я залогинился как {bot.user}')

@bot.slash_command(description='Привет новые технологии команд', guild_ids=[TESTING_GUILD_ID])
async def Hello(interaction: nextcord.Interaction):
    await interaction.send("Hello!")
    
bot.run(BOT_TOKEN)