#MADE BY PANDIT
ok = "https://telegra.ph/file/f092c5e302854f146da74.jpg"
ok1 = 'https://telegra.ph/file/bfee4639f6d0e777f11d4.jpg'
ok2 = "https://telegra.ph/file/0a1f4dd861247158d1c78.jpg"
ok3 = "https://telegra.ph/file/2f198cfb45b7dae3e7b67.jpg"
ok4 = "https://telegra.ph/file/d8dfff58472681c196a10.jpg"
ok5 = "https://telegra.ph/file/d7663a8372268c4e066a9.jpg"
ok6 = "https://telegra.ph/file/1901fd8c1dbe69527c280.jpg"
ok7 = "https://telegra.ph/file/069b3be8f57b84e8c8001.jpg"
ok8 = "https://telegra.ph/file/c6e15e553c519bef360e9.jpg"
ok9 = "https://telegra.ph/file/fac51f7b738a122a2222b.jpg"
ok10 = "https://telegra.ph/file/4dce355acbb2c057309a4.jpg"
ok11 = "https://telegra.ph/file/f2dd6742417c0d7ae7ce2.jpg"
ok12 = "https://telegra.ph/file/cadf5668940c07f9d9bba.jpg"
ok13 = "https://telegra.ph/file/8f88d3f8919c617da78d9.jpg"
ok14 = "https://telegra.ph/file/07f7154e2f733fb0181ba.jpg"
ok15 = "https://telegra.ph/file/5e1e97e558f073ea36b54.jpg"
ok16 = "https://telegra.ph/file/a21b08e83dd7c476aae64.jpg"
ok17 = "https://telegra.ph/file/2d37ca276751e846b1c7b.jpg"
cap = "CHUP RNDI"
cap2 = "TU CHUP HOGA YA TERI GAND M SRIA DU BETICHOD"
cap3 = "RANDI AURAT"
cap4 = "CHUT KA PIYASA AADMI"
cap5 = "FULL RAMDIBAAZI BHIYA"
cap6 = "WHAT'S NEW I ALREADY KNEW"
cap7 = "I TRIED SO HARD AND GO SO FAR"
cap8 = "BUT IN THE END"
cap9 = "IT DOES NOT EVEN MATTER"
cap10 = "CHEEMS IS LOVE"
cap11 = "I KNOW I M PRO"
cap12 = "LOOK WHAT U DID"
cap13 = "TWO MINUTES SILENCE PLIMS"
cap14 = "AAGE JAKE GAND MRAWA BHOSDIWALE"
cap15 = "FULL SUPPORT"
cap16 = "YAR MEIN ITNA COOL KYU HU YAAR"
cap17 = "U MAH LOMVE"
cap18 = "CHEEMS IS LOVE"
import asyncio
from . import *
@borg.on(admin_cmd(pattern="cb"))# by PANDIT
@borg.on(sudo_cmd(pattern="cb", allow_sudo=True))
async def _(event):
  await event.delete()
  if not event.is_reply:
    file = await bot.send_file(event.chat, ok, caption=cap)
    await asyncio.sleep(4)
    await bot.edit_message(event.chat, file, cap2, file=ok1)
    await asyncio.sleep(4)
    await bot.edit_message(event.chat, file, cap3, file=ok2)
    await asyncio.sleep(4)
    await bot.edit_message(event.chat, file, cap4, file=ok3)
    await asyncio.sleep(4)
    await bot.edit_message(event.chat, file, cap5, file=ok4)
    await asyncio.sleep(4)
    await bot.edit_message(event.chat, file, cap6, file=ok5)
    await asyncio.sleep(4)
    await bot.edit_message(event.chat, file, cap7, file=ok6)
    await asyncio.sleep(4)
    await bot.edit_message(event.chat, file, cap8, file=ok7)
    await asyncio.sleep(4)
    await bot.edit_message(event.chat, file, cap9, file=ok8)
    await asyncio.sleep(4)
    await bot.edit_message(event.chat, file, cap10, file=ok9)
    await asyncio.sleep(4)
    await bot.edit_message(event.chat, file, cap11, file=ok10)
    await asyncio.sleep(4)
    await bot.edit_message(event.chat, file, cap12, file=ok11)
    await asyncio.sleep(4)
    await bot.edit_message(event.chat, file, cap13, file=ok12)
    await asyncio.sleep(4)
    await bot.edit_message(event.chat, file, cap14, file=ok13)
    await asyncio.sleep(4)
    await bot.edit_message(event.chat, file, cap15, file=ok14)
    await asyncio.sleep(4)
    await bot.edit_message(event.chat, file, cap16, file=ok15)
    await asyncio.sleep(4)
    await bot.edit_message(event.chat, file, cap17, file=ok16)
    await asyncio.sleep(4)
    await bot.edit_message(event.chat, file, cap18, file=ok17)
  elif event.is_reply:
    Pro = await event.get_reply_message()
    file = await bot.send_file(event.chat, ok, caption=cap, reply_to=Pro)
    await asyncio.sleep(4)
    await bot.edit_message(event.chat, file, cap2, file=ok1)
    await asyncio.sleep(4)
    await bot.edit_message(event.chat, file, cap3, file=ok2)
    await asyncio.sleep(4)
    await bot.edit_message(event.chat, file, cap4, file=ok3)
    await asyncio.sleep(4)
    await bot.edit_message(event.chat, file, cap5, file=ok4)
    await asyncio.sleep(4)
    await bot.edit_message(event.chat, file, cap6, file=ok5)
    await asyncio.sleep(4)
    await bot.edit_message(event.chat, file, cap7, file=ok6)
    await asyncio.sleep(4)
    await bot.edit_message(event.chat, file, cap8, file=ok7)
    await asyncio.sleep(4)
    await bot.edit_message(event.chat, file, cap9, file=ok8)
    await asyncio.sleep(4)
    await bot.edit_message(event.chat, file, cap10, file=ok9)
    await asyncio.sleep(4)
    await bot.edit_message(event.chat, file, cap11, file=ok10)
    await asyncio.sleep(4)
    await bot.edit_message(event.chat, file, cap12, file=ok11)
    await asyncio.sleep(4)
    await bot.edit_message(event.chat, file, cap13, file=ok12)
    await asyncio.sleep(4)
    await bot.edit_message(event.chat, file, cap14, file=ok13)
    await asyncio.sleep(4)
    await bot.edit_message(event.chat, file, cap15, file=ok14)
  
CmdHelp("cheemsbaazi").add_command(
  "cd", None, "tag someone and see"
).add_warning(
  "✅ Harmless Module"
).add()
