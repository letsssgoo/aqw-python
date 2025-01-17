from typing import List, Union
from core.bot import Bot
from core.commands import Command
from abstracts.base_command import BaseCommand
import asyncio

class BankToInvCmd(BaseCommand):
    
    def __init__(self, itemName: Union[str, List[str]]):
        self.itemNames = itemName if isinstance(itemName, list) else [itemName]

    async def execute(self, bot: Bot, cmd: Command):
        for item in self.itemNames:
            item = bot.player.get_item_bank(item)        
            if item:
                packet = f"%xt%zm%bankToInv%{bot.areaId}%{item.item_id}%{item.char_item_id}%"
                bot.write_message(packet)
                is_exist = False
                for itemInv in bot.player.INVENTORY:
                    if itemInv.item_name == item.item_name:
                        bot.player.INVENTORY.remove(itemInv)
                        bot.player.INVENTORY.append(item)
                        is_exist = True
                        break
                if not is_exist:
                    bot.player.INVENTORY.append(item)
                for itemBank in bot.player.BANK:
                    if itemBank.item_name == item.item_name:
                        bot.player.BANK.remove(itemBank)
                        break
                await asyncio.sleep(1)
        
    def to_string(self):
        if len(self.itemNames) == 1:
            return f"Bank to inv: {self.itemNames[0]}"
        else:
            return f"Bank to inv: {', '.join(self.itemNames)}"