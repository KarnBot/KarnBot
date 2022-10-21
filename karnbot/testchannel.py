import traceback
from config import test_channel_id


class TestChannel:
    channel_id: int = None
    test_channel = None

    def __init__(self) -> None:
        pass

    @classmethod
    def configure(cls, bot):
        cls.channel_id = test_channel_id
        cls.test_channel = bot.get_channel(cls.channel_id)

    @classmethod
    async def log_error(cls, cmd_name):
        tb = traceback.format_exc()
        await cls.test_channel.send(
            f"Exception on bot command: {cmd_name}\n{tb}"
        )
