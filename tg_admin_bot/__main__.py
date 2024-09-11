from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parent.parent.resolve()))
import tg_admin_bot.core.tg
import asyncio


async def async_main():
    await tg_admin_bot.core.tg.init()
    await tg_admin_bot.core.tg.set_handlers()


def main():
    asyncio.run(async_main())


if __name__ == '__main__':
    main()

