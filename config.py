import os
from dataclasses import dataclass
from load_dotenv import load_dotenv

@dataclass
class DataBaseConfig:
    name: str
    host: str
    user: str
    password: str

@dataclass
class TgBot:
    token: str
    admin_ids: list[int]

@dataclass
class Config:
    bot: TgBot
    db: DataBaseConfig

load_dotenv()

config = Config(
    bot=TgBot(
        token=os.getenv('TOKEN'),
        admin_ids=os.getenv('ADMIN_IDS').split(',')
    ),
    db=DataBaseConfig(
        name=os.getenv('DB_NAME'),
        host=os.getenv('DB_HOST'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD')
    )
)

print('BOT_TOKEN:', config.bot.token)
print('ADMIN_IDS:', config.bot.admin_ids)
print()
print('DB_NAME:', config.db.name)
print('DB_HOST:', config.db.host)
print('DB_USER:', config.db.user)
print('DB_PASSWORD:', config.db.password)