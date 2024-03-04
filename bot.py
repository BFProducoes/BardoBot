import hikari
import lightbulb
import os

from consts import QUEM_E_GUNTER, TOKEN, COMPUTEIROS_GUILD_ID

bot = lightbulb.BotApp(
    token=TOKEN,
    default_enabled_guilds=COMPUTEIROS_GUILD_ID
)


@bot.listen()
async def load_plugin() -> None:
    bot.load_extensions('plugin')


@bot.command()
@lightbulb.command('ping', 'Responde caso esteja online')
@lightbulb.implements(lightbulb.SlashCommand)
async def ping(context):
    await context.respond('Estou online!')


@bot.command
@lightbulb.command('gunter', 'Quem é Gunter?')
@lightbulb.implements(lightbulb.SlashCommand)
async def gunter(context):
    await context.respond(QUEM_E_GUNTER)


bot.run()
