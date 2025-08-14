from core.bot import Bot
from core.commands import Command
import json
from colorama import Fore

is_locked_zone = False

async def main(cmd: Command):
    global is_locked_zone

    await cmd.join_map("whitemap")

    await cmd.equip_item("Legion Revenant")

    skill_list = [0,1,2,0,3,4]
    skill_index = 0

    list_maps = [
        "shadowrealmpast"
    ]
    index_count = 0

    cmd.bot.subscribe(message_handler)

    while cmd.isStillConnected():
        if is_locked_zone:
            await cmd.join_map(list_maps[index_count])
            is_locked_zone = False
            index_count = (index_count + 1) % len(list_maps)
            await cmd.sleep(1000)
        if cmd.bot.follow_player != "" and cmd.bot.followed_player_cell != cmd.bot.player.CELL:
            await cmd.bot.goto_player(cmd.bot.follow_player)
            await cmd.sleep(1000)
            continue 
        await cmd.use_skill(skill_list[skill_index])
        skill_index += 1
        if skill_index >= len(skill_list):
            skill_index = 0
        await cmd.sleep(100)

def message_handler(message):
    global is_locked_zone
    if message:
        if message.startswith("%") and message.endswith("%"):
            if "locked zone" in message.lower():
                msg = message.split('%')
                text = msg[4]
                print(Fore.RED + f"server warning: {text}" + Fore.WHITE)
                is_locked_zone = True

def is_valid_json(s):
    try:
        json.loads(s)
        return True
    except json.JSONDecodeError:
        return False