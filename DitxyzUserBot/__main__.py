# Credits: @mrismanaziz
# Copyright (C) 2022 Pyro-ManUserbot
#
# This file is a part of < https://github.com/mrismanaziz/PyroMan-Userbot/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/mrismanaziz/PyroMan-Userbot/blob/main/LICENSE/>.
#
# t.me/DitxyzSupport & t.me/Pyzn0de

from pyrogram import idle
from uvloop import install

from config import BOT_VER, CMD_HANDLER
from DitxyzUbot import BOTLOG_CHATID, LOGGER, LOOP, aiosession, bot1, bots
from DitxyzUbot.helpers.misc import create_botlog, git, heroku

MSG_ON = """
(つ●~●)つ **Ditxyz-UserBot Udah Aktif Nih Ngab**
━━
➠ **Userbot Version -** `{}`
➠ **Ketik** `{}alive` **Coba Cek Bot Nya**
━━
"""


async def main():
    for bot in bots:
        try:
            await bot.start()
            bot.me = await bot.get_me()
            await bot.join_chat("Lunatic0de")
            await bot.join_chat("SharingUserbot")
            try:
                await bot.send_message(
                    BOTLOG_CHATID, MSG_ON.format(BOT_VER, CMD_HANDLER)
                )
            except BaseException:
                pass
            LOGGER("ProjectMan").info(
                f"Logged in as {bot.me.first_name} | [ {bot.me.id} ]"
            )
        except Exception as a:
            LOGGER("main").warning(a)
    LOGGER("ProjectMan").info(f"Ditxyz-UserBot v{BOT_VER} [×͜× UDAH AKTIF NIH PAKE YANG BENER!×͜×]")
    if not str(BOTLOG_CHATID).startswith("-100"):
        await create_botlog(bot1)
    await idle()
    await aiosession.close()


if __name__ == "__main__":
    LOGGER("ProjectMan").info("Starting Ditxyz-UserBot")
    install()
    git()
    heroku()
    LOOP.run_until_complete(main())
