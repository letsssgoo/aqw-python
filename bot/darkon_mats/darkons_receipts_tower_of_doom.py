from bot.darkon_mats.core_darkon_mats import darkons_receipts_tower_of_doom
from core.bot import Bot
from core.commands import Command

async def main(bot: Bot):
    cmd = Command(bot)

    await darkons_receipts_tower_of_doom(cmd, 222)