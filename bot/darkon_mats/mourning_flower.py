from bot.darkon_mats.core_darkon_mats import mourning_flower
from core.bot import Bot
from core.commands import Command

async def main(bot: Bot):
    cmd = Command(bot)

    await mourning_flower(cmd, 1000)