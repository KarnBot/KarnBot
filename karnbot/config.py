from contextlib import contextmanager

import configparser


@contextmanager
def config_loader():
    config = configparser.ConfigParser()
    try:
        config.read("config.ini")
        yield config["Discord"]
    except KeyError:
        config.read("karnbot/config.ini")
        yield config["Discord"]


test_channel_id = None
test_guild: int = None

with config_loader() as discord_config:
    test_channel_id = int(discord_config.get("TestChannel", 0))
    test_guild = int(discord_config.get("TestGuild", 0))
