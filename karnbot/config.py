import configparser


def config_loader():
    config = configparser.ConfigParser()
    config.read("config.ini")
    yield config["Discord"]


test_channel_id = None
test_guild: int = None

with config_loader() as discord_config:
    test_channel_id = discord_config.get("TestChannel", "")
    test_guild = int(discord_config.get("TestGuild", 0))
