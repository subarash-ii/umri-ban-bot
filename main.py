import asyncio
from aiogram import Bot, Dispatcher

from config import TOKEN
from handlers.ban import router as ban_router

bot = Bot(token=TOKEN)
dp = Dispatcher()


async def on_startup():
    print("Bot is running")


async def main():
    dp.startup.register(on_startup)

    dp.include_router(ban_router)

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(main())