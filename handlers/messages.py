from telegram import Update
from telegram.ext import ContextTypes
from nltk.tokenize import word_tokenize
from utilities.data_handler import tai_du_lieu_tro_chuyen
import random

async def xu_ly_tin_nhan(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    noi_dung = update.message.text.lower()
    du_lieu = tai_du_lieu_tro_chuyen()
    
    tu_khoa = word_tokenize(noi_dung)
    tu_khoa = [tu.lower() for tu in tu_khoa]
    
    matches = []
    for loai, data in du_lieu.items():
        if loai != "mac_dinh":
            for mau in data.get("mau", []):
                if mau in noi_dung:
                    matches.append((loai, data))
                    break  # Dừng lại khi tìm thấy mẫu

    if matches:
        # Chỉ trả lời một lần cho mỗi mẫu phù hợp
        tra_loi = random.choice(matches[0][1]["tra_loi"])
        await update.message.reply_text(tra_loi)
    else:
        tra_loi_mac_dinh = random.choice(du_lieu["mac_dinh"]["tra_loi"])
        await update.message.reply_text(tra_loi_mac_dinh)

