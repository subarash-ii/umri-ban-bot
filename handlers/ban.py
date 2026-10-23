from aiogram import Router, F
from aiogram.types import Message, LinkPreviewOptions
from aiogram.enums import ChatMemberStatus
from aiogram.utils.text_decorations import html_decoration as html

router = Router()

@router.message(F.reply_to_message, F.text.lower().startswith("умри"))
async def ban(message: Message):
    member = await message.chat.get_member(message.from_user.id)

    if member.status not in [ChatMemberStatus.CREATOR, ChatMemberStatus.ADMINISTRATOR]:
        return

    banned_user = message.reply_to_message.from_user

    if banned_user.id == member.user.id:
        return

    try:
        await message.bot.ban_chat_member(chat_id=message.chat.id, user_id=banned_user.id)

        # banned_link = (
        #     f'<a href="tg://user?id={banned_user.id}">'
        #     f'{html.quote(banned_user.full_name)}</a>'
        # )

        # moderator_link = (
        #     f'<a href="tg://user?id={member.user.id}">'
        #     f'{html.quote(member.user.full_name)}</a>'
        # )
        #
        # await message.answer(
        #     f"🚫 {banned_link} получает бан навсегда\n"
        #     f"👮 Модератор: {moderator_link}",
        #     parse_mode="HTML",
        # )

        await message.answer(f'<a href="tg://user?id={banned_user.id}">🪦</a>', parse_mode="HTML", link_preview_options=LinkPreviewOptions(is_disabled=True))

    except Exception as e:
        print(f"Error: {e}")