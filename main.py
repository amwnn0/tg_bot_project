import asyncio
import logging

from config.config import load_config
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

# Import routers
# Import middlewares
# Import additional functions

from keyboards.main_menu import set_main_menu

# Initialize logger
logger = logging.getLogger(__name__)

# Configure and start bot
async def main():
    # Configure logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(filename)s:%(lineno)d #%(levelname)-8s '
                '[%(asctime)s] - %(name)s - %(message)s'
    )
    logger.info('Starting bot')

    config = load_config()

    storage = ...

    bot = Bot(
        token=config.bot.token,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML)
    )
    dp = Dispatcher(storage=storage)

    # Initialize other objects (db, etc.)

    # Add objects to Dispatcher workflow_data
    dp.workflow_data.update({})
    dp[...] = ...

    # Set bot main menu
    await set_main_menu(bot)

    # Register routers
    logger.info('Registering routers')

    # Register middleware
    logger.info('Registering middleware')

    # Skip updates and start polling
    await bot.delete_webhook(drop_pending_updates=True)
    logger.info('Bot running...')
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())