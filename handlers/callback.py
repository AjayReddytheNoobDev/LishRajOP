# (C) 2021 SERPENTSMusic

from handlers.play import cb_admin_check
from helpers.decorators import authorized_users_only
from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from config import (
    ASSISTANT_NAME,
    BOT_NAME,
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_NAME,
    UPDATES_CHANNEL,
)


@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""!! Welcome [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !!\n
💭 **[LishRaj_VC_Bot](https://t.me/LishRaj_Vc_Bot) allows you to play music on groups through the new Telegram's voice chats!**

💡 **Find out all the Bot's commands and how they work by clicking on the » COMMANDS button!**

❔ **To know how to use this bot, please click on the » ❓ Basic Guide button!**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ Add me to your Group ➕",
                        url=f"https://t.me/LishRaj_Vc_Bot?startgroup=true",
                    )
                ],
                [InlineKeyboardButton("❓ Basic Guide", callback_data="cbhowtouse")],
                [
                    InlineKeyboardButton("COMMANDS", callback_data="cbcmds"),
                    InlineKeyboardButton("Donate (Me Ghareeb Hu)", url=f"https://t.me/LishRaj_Vc_Bot"),
                ],
                [
                    InlineKeyboardButton(
                        "SUPPORT Group", url=f"https://t.me/LishRaj"
                    ),
                    InlineKeyboardButton(
                        "UPDATES Channel", url=f"https://t.me/LishRaj"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "SOURCE", url="https:/t.me/LishRaj"
                    )
                ],
            ]
        ),
        disable_web_page_preview=True,
    )


@Client.on_callback_query(filters.regex("cbhelp"))
async def cbhelp(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""✨ **Hello** [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !

» **press the button below to read the explanation and see the list of available commands !**

Say Thanks to LishRaj""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("BASIC COMMANDS", callback_data="cbbasic"),
                    InlineKeyboardButton("ADVANCED COMMANDS", callback_data="cbadvanced"),
                ],
                [InlineKeyboardButton("ADMIN COMMANDS", callback_data="cbadmin")],
                [InlineKeyboardButton("🔙 Go Back", callback_data="cbguide")],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("cbbasic"))
async def cbbasic(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""!! Here are the basic commands!! Dhyan se padhlo, samjha nhi toh support me aake puchlo

 [ GROUP VC CMD ]

/play - play song from youtube (Just type the song name)
/ytp - play song directly from youtube (Just type the song name)
/stream (reply to an audio file) - play song using audio file
/playlist - show the list of songs in queue
/song (song name) - download a song from youtube

 [ CHANNEL VC CMD ]

/cplay - play music in the voice chat of channel
/cplayer - show the song which is being played
/cpause - pause the music
/cresume - resume the music
/cskip - skip to the next song
/cend - end the play
/refresh - refresh the admin cache
/ubjoinc - invite the assistant for join to your channel

Say Thanks to LishRaj""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbhelp")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbadvanced"))
async def cbadvanced(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""Yooo !! Here you go with the advanced commands !! Dhyan se padhlo, samja me nhi aaya toh support me pucho

/start (in group) - see whether the bot is alive/dead
/reload - reload the bot and refresh the admin list
/ping - check the bot ping status

Say Thanks to @TEAM_SERPENT""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbhelp")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbadmin"))
async def cbadmin(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""I understood that u r an admin of a grp/channel. Admin toh bnaya na muje?? OK OK OK, **here are the admin commands**

/player - Show the music play status
/pause - pause the music streaming
/resume - resume the music was paused
/skip - skip to the next song
/end - stop the music play
/join - invite the userbot to your group
/leave - Makes the userbot to leave your group
/auth - Authorizes the non admin user for using music bot in your group
/unauth - unauthorizes the authorixed user for using music bot
/control - opens the player settings panel
/delcmd (on | off) - enable / disable del cmd featurep

Say Thanks to LishRaj""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbhelp")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbsudo"))
async def cbsudo(_, query: CallbackQuery):
    await query.edit_message_text(
        f""" OK, are u a sudo user?? agar hai toh tuje cmds @SERPENT_BOTS_SUPPORT me explain karunga aaja **here is the sudo commands**

/leaveall - order the assistant to leave from all group
/stats - show the bot statistic
/rmd - remove all downloaded files
/eval (query) - execute code
/sh (query) - run code

⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbhelp")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbowner"))
async def cbowner(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 **here is the owner commands**

/stats - show the bot statistic
/broadcast (reply to message) - send a broadcast message from bot
/block (user id - duration - reason) - block user for using your bot
/unblock (user id - reason) - unblock user you blocked for using your bot
/blocklist - show you the list of user was blocked for using your bot

📝 note: all commands owned by this bot can be executed by the owner of the bot without any exceptions.

⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbhelp")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbguide"))
async def cbguide(_, query: CallbackQuery):
    await query.edit_message_text(
        f""" !! HOW TO USE THIS BOT:

1.) *Add me to your group.*
2.) **Promote me in your group as admin and give all permissions including Add admins, but dont give me Reamin anonymous right**
3.) **add @HERPENTSVCPLAYER to your group or type /join to invite that kid**
4.) **Turn on the voice chat first before start to play music.**
Say Thanks to LishRaj""",
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("COMMANDS", callback_data="cbhelp")],
                [InlineKeyboardButton("🗑 Close", callback_data="close")],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("close"))
async def close(_, query: CallbackQuery):
    await query.message.delete()


@Client.on_callback_query(filters.regex("cbback"))
@cb_admin_check
async def cbback(_, query: CallbackQuery):
    await query.edit_message_text(
        "YOO YOO YOO *Here You Go with the control menu of bot :**",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("⏸ pause", callback_data="cbpause"),
                    InlineKeyboardButton("▶️ resume", callback_data="cbresume"),
                ],
                [
                    InlineKeyboardButton("⏩ skip", callback_data="cbskip"),
                    InlineKeyboardButton("⏹ stop", callback_data="cbend"),
                ],
                [InlineKeyboardButton("⛔ anti cmd", callback_data="cbdelcmds")],
                [InlineKeyboardButton("🗑 Close", callback_data="close")],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("cbdelcmds"))
@cb_admin_check
@authorized_users_only
async def cbdelcmds(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""Here you go with the features information:**
        
* Feature:* Delets every command sent by users(Noob kids) to avoid spam in groups !!

How to use :**

 1️⃣ to turn on feature:
     » type `/delcmd on`
    
 2️⃣ to turn off feature:
     » type `/delcmd off`
Say thanks to @TEAM_SERPENT""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbback")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbcmds"))
async def cbhelps(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""**Hello** [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) bhau !

» **press the button below to read the explanation and see the list of available commands !**

Say thanks to @TEAM_SERPENT""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("BASIC COMMANDS", callback_data="cblocal"),
                    InlineKeyboardButton("ADVANCED COMMANDS", callback_data="cbadven"),
                ],
                [
                    InlineKeyboardButton("ADMIN COMMANDS", callback_data="cblamp"),
                ],
                [InlineKeyboardButton("🔙 Go Back", callback_data="cbstart")],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("cbhowtouse"))
async def cbguides(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""**HOW TO USE THIS BOT:**

1.) **Add me to your group.**
2.) **Promote me as admin in your group and give all permissions including Add Admins but dont gibe me Remain Anonymous right.**
3.) **add @{ASSISTANT_NAME} to your group or type /join to invite her.**
4.) **Turn on the voice chat first before you start to play music.**

Say thanks to @LishRaj""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbstart")]]
        ),
    )


@Client.on_callback_query(filters.regex("cblocal"))
async def cblocal(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""!! Here are the basic commands!! Dhyan se padhlo, samjha nhi toh support me aake puchlo

 [ GROUP VC CMD ]

/play - play song from youtube (Just type the song name)
/ytp - play song directly from youtube (Just type the song name)
/stream (reply to an audio file) - play song using audio file
/playlist - show the list of songs in queue
/song (song name) - download a song from youtube

 [ CHANNEL VC CMD ]

/cplay - play music in the voice chat of channel
/cplayer - show the song which is being played
/cpause - pause the music
/cresume - resume the music
/cskip - skip to the next song
/cend - end the play
/refresh - refresh the admin cache
/ubjoinc - invite the assistant for join to your channel

Say thanks to @LishRaj""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbadven"))
async def cbadven(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""Yooo !! Here you go with the advanced commands !! Dhyan se padhlo, samja me nhi aaya toh support me pucho

/start (in group) - see whether the bot is alive/dead
/reload - reload the bot and refresh the admin list
/ping - check the bot ping status

Say Thanks to @LishRaj""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cblamp"))
async def cblamp(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""I understood that u r an admin of a grp/channel. Admin toh bnaya na muje?? OK OK OK, **here are the admin commands

/player - Show the music play status
/pause - pause the music streaming
/resume - resume the music was paused
/skip - skip to the next song
/end - stop the music play
/join - invite the userbot to your group
/leave - Makes the userbot to leave your group
/auth - Authorizes the non admin user for using music bot in your group
/unauth - unauthorizes the authorixed user for using music bot
/control - opens the player settings panel
/delcmd (on | off) - enable / disable del cmd feature

Say thanks to LishRaj""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cblab"))
async def cblab(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 **here is the sudo commands**

/leaveall - order the assistant to leave from all group
/stats - show the bot statistic
/rmd - remove all downloaded files
/eval (query) - execute code
/sh (query) - run code

⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbmoon"))
async def cbmoon(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 **here is the owner commands**

/stats - show the bot statistic
/broadcast - send a broadcast message from bot
/block (user id - duration - reason) - block user for using your bot
/unblock (user id - reason) - unblock user you blocked for using your bot
/blocklist - show you the list of user was blocked for using your bot

📝 note: all commands owned by this bot can be executed by the owner of the bot without any exceptions.

⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbcmds")]]
        ),
    )
