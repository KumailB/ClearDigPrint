import discord
from discord.ext import commands

client = commands.Bot(command_prefix='!')


async def deleteMsgs(ctx, limiter=None):
    # Sending a temporary message while the bot cycles through messages
    deletingMsg = await ctx.send(f"Deleting {ctx.author.mention}'s messages....")
    msgsDeleted = 0
    iteration = 0
    # Looping through messages in channel history
    async for message in ctx.channel.history(limit=limiter):
        iteration += 1
        print(iteration)
        if message.author == ctx.author:  # Checking if message author is the user who typed the command
            await message.delete()
            msgsDeleted += 1
    await deletingMsg.delete()  # Deleting the temporary message
    # Sending a confirmation message that user's messages have been deleted
    await ctx.send(f'Deleted {msgsDeleted} messages from {ctx.author.mention}.')


@client.event
async def on_ready():
    print("ClearDigPrint is now online!")


@client.command()
async def clearall(ctx):
    await deleteMsgs(ctx)


@client.command()
async def clearlast(ctx, *, last=5):
    await deleteMsgs(ctx, last)


@client.command()
async def clearif(ctx, last, *, specificMsg):
    # Printing the arguments to console
    print(specificMsg)
    print(last)
    last = int(last)  # Converting first argument to int
    # Sending a temporary message while the bot cycles through messages
    deletingMsgStr = f"Deleting {ctx.author.mention}'s messages that contain:"
    deletingMsgStr += f' "{specificMsg}"'
    deletingMsg = await ctx.send(deletingMsgStr)

    # Looping through messages in channel history
    counter = 0
    iteration = 0
    async for message in ctx.channel.history(limit=(last + 2)):
        iteration += 1
        print(f"Iteration: {iteration}")
        # Checking the message author and content
        if message.author == ctx.author and specificMsg in message.content:
            await message.delete()
            counter += 1
    await deletingMsg.delete()  # Deleting the temporary message
    # Sending a confirmation message that user's messages have been deleted
    await ctx.send(f'Deleted {counter} messages from {ctx.author.mention}.')


client.run('NzI0MzU5NTU0NTU2NzU2MDcw.Xu_DQA.dgNAHNa3Gcdqoo2Tnhwodrw6yzo')
