# noinspection PyUnresolvedReferences
import discord
from discord.ext import commands
from random import choice as rnd
from .utils.dataIO import dataIO
import os

class chad:
    """Japanese Emoticons"""

    def __init__(self, bot):
        self.bot = bot
        self.toggle = False
        self.kaomojis = "data/chad/kaomojis.json"
        self.system = dataIO.load_json(self.kaomojis)

    def save_emotes(self):
        dataIO.save_json(self.kaomojis, self.system)
        dataIO.is_valid_json("data/chad/kaomojis.json")

    # @commands.group(aliases=["kao"], invoke_without_command=True, pass_context=True)
    def kaomoji(self):
        str_category = "happy"
        # m = ctx.message
        # amount = len(self.system.get(str_category, []))
        if str_category in self.system:
            # if n is None:
            return (rnd(self.system[str_category]))
            # else:
            #     if n > amount:
            #         print ("The highest kaomoji count for " + str_category + " is "
            #                            + str(amount) + ". \n(╯°□°）╯︵ ┻━┻")
            #     else:
            #         return (self.system[str_category])
                    # print (self.system[str_category][n])
            # print(str_category + " kaomoji called")
        # else:
        #     print (str_category + " category couldn't be found. \n¯\_(ツ)_/¯")
        # if self.toggle is True:
        #     try:
        #         await self.bot.delete_message(m)
        #         await self.bot.say("Deleted command msg {}".format(m.id))
        #     except discord.errors.Forbidden:
        #         await self.bot.say("Wanted to delete mid {} but no permissions".format(m.id))

    # @kaomoji.command(name="list")
    # async def _list(self):
    #     """Shows all categories"""
    #     categories = [i for i in self.system]
    #     await self.bot.say("```" + ', '.join(categories) + "```")
    #     print("Kaomoji list called")


    # @kaomoji.command()
    # async def count(self, category: str):
    #     """Displays count per category"""
    #     str_category = category.lower()
    #     amount = len(self.system[str_category])
    #     await self.bot.say("There are " + str(amount) + " kaomojis for " + str_category)

    # @kaomoji.command()
    # async def cleaner(self, on_off: str):
    #     """Cleans up your commands"""
    #     if on_off is True:
    #         await self.bot.say('Deleting commands is now ON.')
    #         self.toggle = True
    #     else:
    #         await self.bot.say('Deleting commands is now OFF.')
    #         self.toggle = False

def check_folders():
    if not os.path.exists("data/chad"):
        print("Creating data/chad folder...")
        os.makedirs("data/chad")


def check_files():
    f = "data/chad/kaomojis.json"
    if not dataIO.is_valid_json(f):
        print("No such thing as feelings.json...")


def setup(bot):
    check_folders()
    check_files()
    n = chad(bot)
    bot.add_cog(n)
