from core.bot import Bot
from core.commands import Command
from abstracts.base_command import BaseCommand
from colorama import Fore 

class TurnInQuestCmd(BaseCommand):
    
    def __init__(self, quest_id: int, item_id: int = -1):
        self.quest_id = quest_id
        self.item_id = item_id
    
    async def execute(self, bot: Bot, cmd: Command):
        bot.turn_in_quest(self.quest_id, self.item_id)
        
    def to_string(self):
        return f"Turn in quest : {self.quest_id}^{self.item_id}"