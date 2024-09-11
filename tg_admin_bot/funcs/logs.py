import pyrogram.types
import tg_admin_bot.core.common


def link(
    msg: pyrogram.types.Message,
) -> str:
    if msg.chat.username:
        return f'{msg.chat.username}/{msg.id}'
    else:
        return f'{msg.chat.full_name}/{msg.id}'

def log_msg(
    to_log: str,
    msg: pyrogram.types.Message,
):
    to_log += ' '
    to_log += link(
        msg=msg,
    )
    if msg.media:
        to_log += f' media={msg.media.value}'
    to_add = ''
    if msg.text:
        to_add = msg.text
    elif msg.caption:
        to_add = msg.caption
    if to_add:
        if len(to_add) > 30:
            to_add = f'{to_add[:30]}…'
        to_add = to_add.replace('\n', '')
        to_log += f" text='{to_add}'"
    tg_admin_bot.core.common.log(to_log)

