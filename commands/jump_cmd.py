from core.bot import Bot
from abstracts.command import Command

class JumpCmd(Command):
    
    def __init__(self, cell: str, pad: str):
        self.cell = cell
        self.pad = pad
    
    async def execute(self, bot: Bot):
        if bot.player.CELL.lower() != self.cell or bot.player.PAD.lower() != self.pad:
            bot.jump_cell(self.cell, self.pad)
        
    def to_string(self):
        return f"Jump : {self.cell} {self.pad}"