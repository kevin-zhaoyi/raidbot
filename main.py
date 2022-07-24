# Import functions ******************************
from func.read_token import read_token
# Import functions ******************************

# Import modules ********************************
import discord
from discord.ext import commands
help('modules')
from discord.utils import get
# Import modules ********************************

# Global definitions ****************************
intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix='!', intents=intents)
slash = SlashCommand(client, sync_commands=True)
bot_token = read_token()

bot = discord.ext.commands.Bot


@client.event
async def on_ready():
    print("Bot is online")

@client.event
async def on_message(message):

    # This will allow for commands to work while the bot parses messages.
    await client.process_commands(message)

@slash.slash(name="Ping", description="pings")
async def ping(ctx):
    await ctx.send("Pong")

# Run the bot.
client.run(bot_token)
