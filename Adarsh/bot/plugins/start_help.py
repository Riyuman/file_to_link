#harshil8981
from Adarsh.bot import StreamBot
from Adarsh.vars import Var
import logging
logger = logging.getLogger(__name__)
from Adarsh.bot.plugins.stream import MY_PASS
from Adarsh.utils.human_readable import humanbytes
from Adarsh.utils.database import Database
from pyrogram import filters, enums
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import UserNotParticipant
from Adarsh.utils.file_properties import get_name, get_hash, get_media_file_size
db = Database(Var.DATABASE_URL, Var.name)
from pyrogram.types import ReplyKeyboardMarkup

                      
@StreamBot.on_message(filters.command('start') & filters.private)
async def start(b, m):
    if not await db.is_user_exist(m.from_user.id):
        await db.add_user(m.from_user.id)
        await b.send_message(
            Var.BIN_CHANNEL,
            f"#NEW_USER: \n\nNew User [{m.from_user.first_name}](tg://user?id={m.from_user.id}) Started !!"
        )
    usr_cmd = m.text.split("_")[-1]
    if usr_cmd == "/start":
        if Var.UPDATES_CHANNEL is not None:
            try:
                user = await b.get_chat_member(Var.UPDATES_CHANNEL, m.chat.id)
                if user.status == enums.ChatMemberStatus.BANNED:
                    await b.send_message(
                        chat_id=m.chat.id,
                        text="**ʏᴏᴜ ᴀʀᴇ ʙᴀɴɴᴇᴅ../**",
                        disable_web_page_preview=True
                    )
                    return
            except UserNotParticipant:
                await b.send_message(
                    chat_id=m.chat.id,
                    text="**ᴊᴏɪɴ ᴍʏ ᴜᴘᴅᴀᴛᴇs ᴄʜᴀɴɴᴇʟ ᴛᴏ ᴜsᴇ  ᴍᴇ..**\n\n**ᴅᴜᴇ ᴛᴏ ᴏᴠᴇʀʟᴏᴀᴅ ᴏɴʟʏ ᴄʜᴀɴɴᴇʟ sᴜʙsᴄʀɪʙᴇʀs ᴄᴀɴ ᴜsᴇ ᴍᴇ..!**",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton("𝙹𝙾𝙸𝙽 𝚄𝙿𝙳𝙰𝚃𝙴𝚉 𝙲𝙷𝙰𝙽𝙽𝙴𝙻", url=f"https://t.me/{Var.UPDATES_CHANNEL}")
                            ]
                        ]
                    )
                    
                )
                return
            except Exception:
                await b.send_message(
                    chat_id=m.chat.id,
                    text="**𝙰𝙳𝙳 𝙵𝙾𝚁𝙲𝙴 𝚂𝚄𝙱 𝚃𝙾 𝙰𝙽𝚈 𝙲𝙷𝙰𝙽𝙽𝙴𝙻**",
                    
                    disable_web_page_preview=True)
                return
        await m.reply_photo(
            photo="https://telegra.ph/file/752b82b354a911c261be4.jpg",
            caption="**ʜᴇʟʟᴏ...⚡\n\nɪᴀᴍ ᴀ sɪᴍᴘʟᴇ ᴛᴇʟᴇɢʀᴀᴍ ғɪʟᴇ/ᴠɪᴅᴇᴏ ᴛᴏ ᴘᴇʀᴍᴀɴᴇɴᴛ ʟɪɴᴋ ᴀɴᴅ sᴛʀᴇᴀᴍ ʟɪɴᴋ ɢᴇɴᴇʀᴀᴛᴏʀ ʙᴏᴛ.**\n\n**ᴜsᴇ /help ғᴏʀ ᴍᴏʀᴇ ᴅᴇᴛsɪʟs\n\nsᴇɴᴅ ᴍᴇ ᴀɴʏ ᴠɪᴅᴇᴏ / ғɪʟᴇ ᴛᴏ sᴇᴇ ᴍʏ ᴘᴏᴡᴇʀᴢ...**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton("⚡ 𝚄𝙿𝙳𝙰𝚃𝙴𝚂 ⚡", url="https://t.me/movie_provider_official"), InlineKeyboardButton("⚡ 𝚂𝚄𝙿𝙿𝙾𝚁𝚃 ⚡", url="https://t.me/@movie_providing_group")],
                    [InlineKeyboardButton("©️ ᗪᗴᐯᒪOᑭᗴᖇ", url="https://t.me/Oogo_Nick"), InlineKeyboardButton("©️ ᗰᗩIᑎTᗩIᑎᗴᖇ", url="https://t.me/Movie_Flix_Zone")],
                    [InlineKeyboardButton("💌 𝗛𝗘𝗟𝗣𝗟𝗜𝗡𝗘 𝗕𝗢𝗧 💌", url="https://t.me/Movie_providing_group_bot")]
                ]
            ),
            
        )
    else:
        if Var.UPDATES_CHANNEL is not None:
            try:
                user = await b.get_chat_member(Var.UPDATES_CHANNEL, m.chat.id)
                if user.status == enums.ChatMemberStatus.BANNED:
                    await b.send_message(
                        chat_id=m.chat.id,
                        text="**ʏᴏᴜ ᴀʀᴇ ʙᴀɴɴᴇᴅ../**",
                        
                        disable_web_page_preview=True
                    )
                    return
            except UserNotParticipant:
                await b.send_message(
                    chat_id=m.chat.id,
                    text="**ᴊᴏɪɴ ᴍʏ ᴜᴘᴅᴀᴛᴇs ᴄʜᴀɴɴᴇʟ ᴛᴏ ᴜsᴇ  ᴍᴇ..**\n\n**ᴅᴜᴇ ᴛᴏ ᴏᴠᴇʀʟᴏᴀᴅ ᴏɴʟʏ ᴄʜᴀɴɴᴇʟ sᴜʙsᴄʀɪʙᴇʀs ᴄᴀɴ ᴜsᴇ ᴍᴇ..!**",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton("ᴊᴏɪɴ ᴍʏ ᴜᴘᴅᴀᴛᴇs ᴄʜᴀɴɴᴇʟ", url=f"https://t.me/{Var.UPDATES_CHANNEL}")
                            ]                           
                        ]
                    )
                    
                )
                return
            except Exception:
                await b.send_message(
                    chat_id=m.chat.id,
                    text="**𝙰𝙳𝙳 𝙵𝙾𝚁𝙲𝙴 𝚂𝚄𝙱 𝚃𝙾 𝙰𝙽𝚈 𝙲𝙷𝙰𝙽𝙽𝙴𝙻**",
                    disable_web_page_preview=True)
                return

        get_msg = await b.get_messages(chat_id=Var.BIN_CHANNEL, ids=int(usr_cmd))

        file_size = None
        if get_msg.video:
            file_size = f"{humanbytes(get_msg.video.file_size)}"
        elif get_msg.document:
            file_size = f"{humanbytes(get_msg.document.file_size)}"
        elif get_msg.audio:
            file_size = f"{humanbytes(get_msg.audio.file_size)}"

        file_name = None
        if get_msg.video:
            file_name = f"{get_msg.video.file_name}"
        elif get_msg.document:
            file_name = f"{get_msg.document.file_name}"
        elif get_msg.audio:
            file_name = f"{get_msg.audio.file_name}"

        stream_link = "https://{}/{}".format(Var.FQDN, get_msg.id) if Var.ON_HEROKU or Var.NO_PORT else \
            "http://{}:{}/{}".format(Var.FQDN,
                                     Var.PORT,
                                     get_msg.id)

        msg_text = "**ʟɪɴᴋ ɪs ɢᴇɴᴇʀᴀᴛᴇᴅ...⚡\n\n📧 ғɪʟᴇ ɴᴀᴍᴇ :-\n{}\n {}\n\n💌 ᴅᴏᴡɴʟᴏᴀᴅ ʟɪɴᴋ :- {}\n\n♻️ ᴛʜɪs ʟɪɴᴋ ɪs ᴘᴇʀᴍᴀɴᴇɴᴛ ᴀɴᴅ ᴡᴏɴ'ᴛ ɢᴇᴛ ᴇxᴘɪʀᴇᴅ ♻️\n\n@movie_providing_group**"
        await m.reply_photo(
            photo="https://telegra.ph/file/752b82b354a911c261be4.jpg",
            caption=msg_text.format(file_name, file_size, stream_link),
            
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("⚡ ᴅᴏᴡɴʟᴏᴀᴅ ɴᴏᴡ ⚡", url=stream_link)]])
        )


@StreamBot.on_message(filters.command('help') & filters.private)
async def help_handler(bot, message):
    if not await db.is_user_exist(message.from_user.id):
        await db.add_user(message.from_user.id)
        await bot.send_message(
            Var.BIN_CHANNEL,
            f"#NEW_USER: \n\nNew User [{message.from_user.first_name}](tg://user?id={message.from_user.id}) Started !!"
        )
    if Var.UPDATES_CHANNEL is not None:
        try:
            user = await bot.get_chat_member(Var.UPDATES_CHANNEL, message.chat.id)
            if user.status == enums.ChatMemberStatus.BANNED:
                await bot.send_message(
                    chat_id=message.chat.id,
                    text="**ʏᴏᴜ ᴀʀᴇ ʙᴀɴɴᴇᴅ../**",
                    
                    disable_web_page_preview=True
                )
                return
        except UserNotParticipant:
            await bot.send_message(
                chat_id=message.chat.id,
                text="**ᴊᴏɪɴ ᴍʏ ᴜᴘᴅᴀᴛᴇs ᴄʜᴀɴɴᴇʟ ᴛᴏ ᴜsᴇ  ᴍᴇ..**\n\n**ᴄʜᴀɴɴᴇʟᴏᴠᴇʀʟᴏᴀᴅ ᴏɴʟʏ ᴄʜᴀɴɴᴇʟ sᴜʙsᴄʀɪʙᴇʀs ᴄᴀɴ ᴜsᴇ ᴍᴇ..!**",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("ᴊᴏɪɴ ᴍʏ ᴜᴘᴅᴀᴛᴇs ᴄʜᴀɴɴᴇʟ", url=f"https://t.me/{Var.UPDATES_CHANNEL}")
                        ]
                    ]
                )
            )
            return
        except Exception:
            await bot.send_message(
                chat_id=message.chat.id,
                text="**𝙰𝙳𝙳 𝙵𝙾𝚁𝙲𝙴 𝚂𝚄𝙱 𝚃𝙾 𝙰𝙽𝚈 𝙲𝙷𝙰𝙽𝙽𝙴𝙻**",
                
                disable_web_page_preview=True)
            return
    await message.reply_photo(
            photo="https://telegra.ph/file/752b82b354a911c261be4.jpg",
            caption="**┣⪼ sᴇɴᴅ ᴍᴇ ᴀɴʏ ғɪʟᴇ/ᴠɪᴅᴇᴏ ᴛʜᴇɴ ɪ ᴡɪʟʟ ʏᴏᴜ ᴘᴇʀᴍᴀɴᴇɴᴛ sʜᴀʀᴇᴀʙʟᴇ ʟɪɴᴋ ᴏғ ɪᴛ...\n\n┣⪼ ᴛʜɪs ʟɪɴᴋ ᴄᴀɴ ʙᴇ ᴜsᴇᴅ ᴛᴏ ᴅᴏᴡɴʟᴏᴀᴅ ᴏʀ ᴛᴏ sᴛʀᴇᴀᴍ ᴜsɪɴɢ ᴇxᴛᴇʀɴᴀʟ ᴠɪᴅᴇᴏ ᴘʟᴀʏᴇʀs ᴛʜʀᴏᴜɢʜ ᴍʏ sᴇʀᴠᴇʀs.\n\n┣⪼ ғᴏʀ sᴛʀᴇᴀᴍɪɴɢ ᴊᴜsᴛ ᴄᴏᴘʏ ᴛʜᴇ ʟɪɴᴋ ᴀɴᴅ ᴘᴀsᴛᴇ ɪᴛ ɪɴ ʏᴏᴜʀ ᴠɪᴅᴇᴏ ᴘʟᴀʏᴇʀ ᴛᴏ sᴛᴀʀᴛ sᴛʀᴇᴀᴍɪɴɢ.\n\n┣⪼ ᴛʜɪs ʙᴏᴛ ɪs ᴀʟsᴏ sᴜᴘᴘᴏʀᴛ ɪɴ ᴄʜᴀɴɴᴇʟ. ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ ᴀs ᴀᴅᴍɪɴ ᴛᴏ ɢᴇᴛ ʀᴇᴀʟᴛɪᴍᴇ ᴅᴏᴡɴʟᴏᴀᴅ ʟɪɴᴋ ғᴏʀ ᴇᴠᴇʀʏ ғɪʟᴇs/ᴠɪᴅᴇᴏs ᴘᴏsᴛ../\n\n sᴇɴᴅ 𝟸 ғɪʟᴇs ᴘᴇʀ 𝟻 ᴍɪɴɪᴛᴜᴇs(sᴘᴀᴍ = ʙᴀɴ)\n\n 𝗗𝗢𝗡𝗧 𝗗𝗢𝗪𝗡𝗟𝗢𝗔𝗗 𝗣𝗢𝗥𝗡🔞\n\n\n┣⪼ ғᴏʀ ᴍᴏʀᴇ ɪɴғᴏʀᴍᴀᴛɪᴏɴ :- /about\n\n\nDM @Oogo_Nick**", 
  
        
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("⚡ 𝚄𝙿𝙳𝙰𝚃𝙴𝚂 ⚡", url="https://t.me/movie_provider_official"), InlineKeyboardButton("⚡ 𝚂𝚄𝙿𝙿𝙾𝚁𝚃 ⚡", url="https://t.me/@movie_providing_group")],
                [InlineKeyboardButton("©️ ᗪᗴᐯᒪOᑭᗴᖇ", url="https://t.me/Oogo_Nick"), InlineKeyboardButton("©️ ᗰᗩIᑎTᗩIᑎᗴᖇ", url="https://t.me/Movie_Flix_Zone")],
                [InlineKeyboardButton("💌 𝗛𝗘𝗟𝗣𝗟𝗜𝗡𝗘 𝗕𝗢𝗧 💌", url="https://t.me/Movie_providing_group_bot")]
            ]
        )
    )

@StreamBot.on_message(filters.command('about') & filters.private)
async def about_handler(bot, message):
    if not await db.is_user_exist(message.from_user.id):
        await db.add_user(message.from_user.id)
        await bot.send_message(
            Var.BIN_CHANNEL,
            f"#NEW_USER: \n\nNew User [{message.from_user.first_name}](tg://user?id={message.from_user.id}) Started !!"
        )
    if Var.UPDATES_CHANNEL is not None:
        try:
            user = await bot.get_chat_member(Var.UPDATES_CHANNEL, message.chat.id)
            if user.status == enums.ChatMemberStatus.BANNED:
                await bot.send_message(
                    chat_id=message.chat.id,
                    text="**ʏᴏᴜ ᴀʀᴇ ʙᴀɴɴᴇᴅ../**",
                    
                    disable_web_page_preview=True
                )
                return
        except UserNotParticipant:
            await bot.send_message(
                chat_id=message.chat.id,
                text="**ᴊᴏɪɴ ᴍʏ ᴜᴘᴅᴀᴛᴇs ᴄʜᴀɴɴᴇʟ ᴛᴏ ᴜsᴇ  ᴍᴇ..**\n\n**ᴅᴜᴇ ᴛᴏ ᴏᴠᴇʀʟᴏᴀᴅ ᴏɴʟʏ ᴄʜᴀɴɴᴇʟ ᴄᴀɴ ᴜsᴇ ᴍᴇ..!**",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("ᴊᴏɪɴ ᴍʏ ᴜᴘᴅᴀᴛᴇs ᴄʜᴀɴɴᴇʟ", url=f"https://t.me/{Var.UPDATES_CHANNEL}")
                        ]
                    ]
                )
            )
            return
        except Exception:
            await bot.send_message(
                chat_id=message.chat.id,
                text="**𝙰𝙳𝙳 𝙵𝙾𝚁𝙲𝙴 𝚂𝚄𝙱 𝚃𝙾 𝙰𝙽𝚈 𝙲𝙷𝙰𝙽𝙽𝙴𝙻**",
                
                disable_web_page_preview=True)
            return
    await message.reply_photo(
            photo="https://telegra.ph/file/752b82b354a911c261be4.jpg",
            caption="""<b>sᴏᴍᴇ ʜɪᴅᴅᴇɴ ᴅᴇᴛᴀɪʟs😜</b>

<b>╭━━━━━━━〔ғɪʟᴇ ᴛᴏ ʟɪɴᴋ ʙᴏᴛ〕</b>
┃
┣⪼<b>👨‍💻ᗪᗴᐯᒪOᑭᗴᖇ : <a href=https://t.me/Oogo_nick>۞ٍٍٖٖٖٖٖٖٖٖٖٖٖٖٖٖٖٖٖٖٖٖٖٖٖٖٖٖٖٖٖٖٖٖٖٖٖٖ 🇳 🇮 🇨 🇰 ۞ٖٖٖٖٖٖٖٖٖٖٖٖٖٖٖ</a></b>
┣⪼<b>👨‍💻ᗰᗩIᑎTᗩIᑎᗴᖇ : <a href='https://t.me/Oogo_noah'>۞ٍٍٖٖٖٖٖٖٖٖٖٖٖٖٖٖٖٖٖٖٖٖٖٖٖٖٖٖٖٖٖٖٖٖٖٖٖٖ🇳 🇴 🇦 🇭 ۞ٖٖٖٖٖٖٖٖٖٖٖٖٖٖٖٖ</a></b>
┣⪼<b>☃️Oғғɪᴄɪᴀʟ Gʀᴏᴜᴘ : <a href=https://t.me/movie_providing_group>𝙈𝙊𝙑𝙄𝙀 𝙂𝙍𝙊𝙐𝙋</a></b>
┣⪼<b>💾Oғғɪᴄɪᴀʟ ᴄʜᴀɴɴᴇʟ : <a href=https://t.me/movie_provider_official>𝙊𝙁𝙁𝙄𝘾𝙄𝘼𝙇 𝙐𝙋𝘿𝘼𝙏𝙀</a></b>
┣⪼<b>✏️Lᴀɴɢᴜᴀɢᴇ: <a href=https://www.python.org>Pyᴛʜᴏɴ 3</a></b>
┣⪼<b>📕Lɪʙʀᴀʀy : <a href=https://github.com/pyrogram>Pyʀᴏɢʀᴀᴍ</a></b>
┣⪼<b>🌀 ᴍʏ ꜱᴇʀᴠᴇʀ : <a href=https://dashboard.heroku.com>Heroku</a></b>
┣⪼<b>‼️🖥️ 𝐇𝐄𝐋𝐏𝐋𝐈𝐍𝐄 🖥️‼️ : <a href='https://t.me/Movie_providing_group_bot'>𝐇𝐄𝐋𝐏𝐋𝐈𝐍𝐄 𝗕𝗢𝗧
</a></b>
┃
<b>╰━━━━━━━〔ᴘʟᴇᴀsʀ sᴜᴘᴘᴏʀᴛ〕</b>""",
  
        
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("⚡ 𝚄𝙿𝙳𝙰𝚃𝙴𝚂 ⚡", url="https://t.me/movie_provider_official"), InlineKeyboardButton("⚡ 𝚂𝚄𝙿𝙿𝙾𝚁𝚃 ⚡", url="https://t.me/@movie_providing_group")],
                [InlineKeyboardButton("©️ ᗪᗴᐯᒪOᑭᗴᖇ", url="https://t.me/Oogo_Nick"), InlineKeyboardButton("©️ ᗰᗩIᑎTᗩIᑎᗴᖇ", url="https://t.me/Movie_Flix_Zone")],
                [InlineKeyboardButton("💌 𝗛𝗘𝗟𝗣𝗟𝗜𝗡𝗘 𝗕𝗢𝗧 💌", url="https://t.me/Movie_providing_group_bot")]
            ]
        )
    )
