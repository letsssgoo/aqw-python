from bot.darkon_mats.core_darkon_mats import bounty_hunter_dubloon
from core.bot import Bot
from core.commands import Command

async def main(bot: Bot):
    cmd = Command(bot)

    await bounty_hunter_dubloon(cmd, 300)