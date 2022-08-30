#thanos_pros
#crediteds rishabh anand -thanosceo
import random
thank = ["⋆*⁎ ᎢℋᎪɳᏦ ᎩӫᏌ ⁎*⋆","ପ(๑•̀ᴗ•̀)* ॣ৳৸ᵃᵑᵏ Ꮍ৹੫ᵎ *","ᐝ୨୧ Ƭʜᵃℕҡ ყօϋ ୨୧ᐝ","ෆ⃛ෆ⃛ෆ⃛ ♡♡[τ̲̅н̲̅a̲̅и̲̅κ̲̅ ч̲̅o̲̅u̲̅]ᴗ͈ₒᴗ͈♡","ᵗᑋᵃᐢᵏ ᵞᵒᵘ ♡⃝⃜","τнänκ чöü♥","⠒̫⃝♡ᵗʱᵃᵑᵏઽ","Thanks : ✚⃞ ⸌̷̻( ᷇ॢ〰ॢ ᷆◍)⸌̷̻"]
@rishu_cmd(pattern="thanks")
async def thanks(ult):
  t = random.choice(thank)
  return await eor(ult, t)
  
CmdHelp("thanks").add_command(
  "thanks", None, "thanks message"
).add_warning(
  "✅ Harmless Module"
).add()