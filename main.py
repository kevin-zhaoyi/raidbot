# Import functions ******************************
from func.read_token import *
from cls.raid import Raid
# Import functions ******************************

# Import modules ********************************
import nextcord
from nextcord import Interaction, SlashOption
from nextcord.ext import commands
import pickle
import pymongo
# Import modules ********************************

# Global definitions ****************************
intents = nextcord.Intents.all()
intents.members = True

client = commands.Bot(command_prefix='!', intents=intents)

db_client = pymongo.MongoClient(read_db_url())
db = db_client.test


raid_db = db_client["raid_info"]
raid_col = raid_db["raid"]
query_tag = {"name": "raid_set"}


raids = []



#************************************************

@client.event
async def on_ready():
    load_raid_info()
    print("Bot is online")
    

@client.event
async def on_message(message):

    # This will allow for commands to work while the bot parses messages.
    await client.process_commands(message)

server_id = 1000330768846962799




@client.slash_command(name = "test", description = "testing nextcord slash commands", guild_ids=[server_id])
async def test(interaction: Interaction):
    await interaction.response.send_message("test done.")




@client.slash_command(
    name = "create_raid",
    description = "Creates a raid",
    guild_ids=[server_id]
    )
async def create_raid(
    interaction: Interaction,
    raid_date: str,
    raid_month: str,
    raid_hour: str,
    raid_minute: str,
    raid_timezone: str = SlashOption(
        name = "timezone",
        choices = ["aest", "pt", "utc"]
    ),
    raid_type: str = SlashOption(
        name = "raid_type",
        choices = ["argos", "valtan", "vykas", "kakul-sadon", "brelshaza"]
    ),
    raid_difficulty: str = SlashOption(
        name = "difficulty",
        choices = ["normal", "hard", "inferno"]
    ),
    
):
    """Creates a raid at time

    Paramaters
    ----------
    interaction: Interaction
        The interaction object
    raid_date: str,
    raid_month: str,
    raid_hour: str,
    raid_minute: str,
    raid_timezone: str,
    raid_type: str,
    raid_difficulty: str,

    """

    new_raid = Raid(raid_type, raid_difficulty, f"{raid_date}/{raid_month}/22 {raid_hour}:{raid_minute} {raid_timezone}")
    global raids
    raids.append(new_raid)
    save_raid_info()
    await interaction.response.send_message(f"Created a {raid_type} {raid_difficulty} raid at {raid_date}, {raid_month} at {raid_hour}:{raid_minute} {raid_timezone}")





@client.slash_command(
    name = "view_raids",
    description = "Views the raids",
    guild_ids=[server_id]
)
async def view_raids(interaction: Interaction):
    await interaction.response.send_message("Here are the raids listed.")
    for raid_idx in range(len(raids)):
        await interaction.channel.send(f"**id: {raid_idx}**\n{str(raids[raid_idx])}\n\n")





@client.slash_command(
    name = "apply",
    description = "Views the raids",
    guild_ids=[server_id]
)
async def apply(
    interaction: Interaction,
    raid_id: int,
    ign: str,
    subclass: str
):
    if raid_id >= len(raids):
        await interaction.response.send_message("Enter a valid raid id.")
    else:
        n = raids[raid_id].apply(interaction.user.id, ign, subclass)
        if n == -1:
            await interaction.response.send_message("This raid is full.")
        elif n == -2:
            await interaction.response.send_message("You're already in this raid.")
        else:
            await interaction.response.send_message("Joined raid.")
            save_raid_info()
    




    
def load_raid_info():
    global raids, raid_col
    #raids = pickle.load(open("./pkl/raids.p", "rb"))
    #raids = pickle.loads()
    raids = pickle.loads(raid_col.find_one()["data"])
    print(raids)
def save_raid_info():
    global raids, raid_col
    pickle.dump(raids, open("./pkl/raids.p", "wb"))
    raid_col.update_one(query_tag, {"$set": {"data": pickle.dumps(raids)}})

# Run the bot.
client.run(read_token())
