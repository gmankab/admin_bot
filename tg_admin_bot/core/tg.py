import tg_admin_bot.core.common
import tg_admin_bot.funcs.logs
import pyrogram.handlers
import pyrogram.client
import pyrogram.types
import asyncio


async def on_msg(
    _,
    msg: pyrogram.types.Message,
):
    if not msg.from_user and not msg.author_signature:
        await msg.delete()
        tg_admin_bot.funcs.logs.log_msg(
            to_log='[red]deleted msg[/]',
            msg=msg,
        )


async def init():
    if not tg_admin_bot.core.common.path.data_dir.exists():
        tg_admin_bot.core.common.path.data_dir.mkdir(
            parents=True,
            exist_ok=True,
        )
    if tg_admin_bot.core.common.path.session.exists():
        bot_token = ''
    else:
        print('please input bot token\n>', end='')
        bot_token = input()
    tg_admin_bot.core.common.client = pyrogram.client.Client(
        name='tg_bot',
        api_id=1,
        api_hash='b6b154c3707471f5339bd661645ed3d6',
        bot_token=bot_token,
        workdir=tg_admin_bot.core.common.path.data_dir,
    )
    await tg_admin_bot.core.common.client.start()


async def set_handlers():
    for handler, to_run in {
        pyrogram.handlers.message_handler.MessageHandler: on_msg,
    }.items():
        tg_admin_bot.core.common.client.add_handler(handler(
            callback=to_run,
        ))
    tg_admin_bot.core.common.log('started')
    while True:
        await asyncio.sleep(1)

