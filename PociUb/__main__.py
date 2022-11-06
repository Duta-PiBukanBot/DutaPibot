# Credits: @mrismanaziz
# Copyright (C) 2022 Pyro-ManUserbot
#
# This file is a part of < https://github.com/mrismanaziz/PyroMan-Userbot/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/mrismanaziz/PyroMan-Userbot/blob/main/LICENSE/>.
#
# ReC0de @pocongonlen

from pyrogram import idle
from uvloop import install

from config import BOT_VER, CMD_HANDLER
from PociUb import BOTLOG_CHATID, LOGGER, LOOP, aiosession, bot1, bots
from PociUb.helpers.misc import create_botlog, git, heroku

MSG_ON = """
‼️ **DutaPibot Berhasil Di Aktifkan**

**┌ [ Userbot Version -** `{}` 
**├ [ Ketik** `{}alive` **untuk Mengecek bot**
**└ [ Harap Gunakan DutaPibot ini dengan bijak!!**
"""


async def main():
    for bot in bots:
        try:
            await bot.start()
            bot.me = await bot.get_me()
            await bot.join_chat("pocongonlen")
            await bot.join_chat("PocongUserbot")
            await bot.join_chat("Poocongonlen")
            try:
                await bot.send_message(
                    BOTLOG_CHATID, MSG_ON.format(BOT_VER, CMD_HANDLER)
                )
            except BaseException:
                pass
            LOGGER("PociUb").info(
                f"Login sebagai {bot.me.first_name} | [ {bot.me.id} ]"
            )
        except Exception as a:
            LOGGER("main").warning(a)
    LOGGER("PociUb").info(f"PociUb v{BOT_VER} [🔥 - BERHASIL DIAKTIFKAN! - 🔥]")
    if bot1 and not str(BOTLOG_CHATID).startswith("-100"):
        await create_botlog(bot1)
    await idle()
    await aiosession.close()


if __name__ == "__main__":
    LOGGER("PociUb").info("Starting DutaPiBot")
    install()
    git()
    heroku()
    LOOP.run_until_complete(main())
