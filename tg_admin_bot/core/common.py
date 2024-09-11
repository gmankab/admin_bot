from pathlib import Path
import pyrogram.client
import rich.console


client: pyrogram.client.Client
console: rich.console.Console = rich.console.Console()
log = console.log


class path:
    src_dir = Path(__file__).parent.parent.resolve()
    app_dir = src_dir.parent.resolve()
    data_dir = app_dir / 'data'
    session = data_dir / 'tg_bot.session'
    pyproject_toml: Path = app_dir / 'pyproject.toml'

