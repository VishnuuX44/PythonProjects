import discord
from discord.ext import commands
from discord_buttons_plugin import *

client = commands.Bot(command_prefix=".")

client = discord.Client()
ddb = Discord_Button(client)

@client.event
async def on_ready():
	 print("Logged in")

@client.event()
async def cButtons(ctx):
	m = await ct.send(
		"command ran",
		cButtons=[
            cButtons(style=ButtonStyle.blue, label="Click Me"),
            cButtons(style=buttonStyle.URL, label="My Website", url='dopexd.unaux.com'),
            cButtons(style=ButtonStyle.disabled, label="this is disables"),
		],

	)
	res =  await ddb.wait_for_button_click(m)
	await res.respond(
    type=InteractionType.ChannelMessageWithSource,
    content=f'{res.button.label} had been clicked'

	)


		



 



client.run('NzgzNDAyMjM4MDM3OTgzMjQz.X8aOMA.tofkd2xQhSO7t53v8a3zp_H0YeM')
