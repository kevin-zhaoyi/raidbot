# Import functions ******************************
from func.read_token import read_token
# Import functions ******************************

# Import modules ********************************
import nextcord
from nextcord import Interaction
from nextcord.ext import commands
# Import modules ********************************

# Global definitions ****************************
intents = nextcord.Intents.all()
intents.members = True

client = commands.Bot(command_prefix='!', intents=intents)
bot_token = read_token()



@client.event
async def on_ready():
    print("Bot is online")

@client.event
async def on_message(message):

    # This will allow for commands to work while the bot parses messages.
    await client.process_commands(message)

server_id = 1000330768846962799

@client.slash_command(name = "test", description = "testing nextcord slash commands", guild_ids=[server_id])
async def test(interaction: Interaction):
    await interaction.response.send_message("test done.")

@client.slash_command(name = "test1", description = "1 testing nextcord slash commands", guild_ids=[server_id])
async def test1(interaction: Interaction, variable: str, var2: str):
    await interaction.response.send_message(variable)

# Run the bot.
client.run(bot_token)
