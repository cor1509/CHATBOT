from telegram import Update
from telegram.ext import ContextTypes
import os
import random
from utilities.config import THU_MUC_ANH

async def bat_dau(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    nguoi_dung = update.effective_user
    await update.message.reply_text(
        f'Xin chào {nguoi_dung.first_name}! Tôi là bot trợ giúp của bạn.\n'
        'Các lệnh có sẵn:\n'
        '/thongtin - Xem thông tin profile\n'
        '/anh - Nhận một tấm ảnh ngẫu nhiên\n'
        '/tatcaanh - Xem tất cả ảnh\n'
        'Bạn cũng có thể trò chuyện với tôi về nhiều chủ đề khác nhau!'
    )

async def thong_tin(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    nguoi_dung = update.effective_user
    ten_day_du = f"{nguoi_dung.first_name} {nguoi_dung.last_name if nguoi_dung.last_name else ''}"
    noi_dung = (
        f"🆔 ID: {nguoi_dung.id}\n"
        f"👤 Tên đầy đủ: {ten_day_du.strip()}\n"
        f"👥 Username: @{nguoi_dung.username if nguoi_dung.username else 'Không có'}\n"
        f"🌐 Ngôn ngữ: {nguoi_dung.language_code if nguoi_dung.language_code else 'Không xác định'}"
    )
    await update.message.reply_text(noi_dung)

async def gui_anh(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    danh_sach_anh = [f for f in os.listdir(THU_MUC_ANH) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.jfif'))]
    
    if danh_sach_anh:
        anh_ngau_nhien = random.choice(danh_sach_anh)
        duong_dan = os.path.join(THU_MUC_ANH, anh_ngau_nhien)
        tong_so_anh = len(danh_sach_anh)
        
        with open(duong_dan, 'rb') as tep_anh:
            await update.message.reply_photo(
                photo=tep_anh,
                caption=f"Đây là ảnh '{anh_ngau_nhien}' (1 trong {tong_so_anh} ảnh trong bộ sưu tập của tôi)"
            )
    else:
        await update.message.reply_text("Xin lỗi, tôi không tìm thấy ảnh nào trong thư mục.")

async def gui_tat_ca_anh(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    danh_sach_anh = [f for f in os.listdir(THU_MUC_ANH) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp','.jfif'))]
    
    if danh_sach_anh:
        await update.message.reply_text(f"Đang gửi {len(danh_sach_anh)} ảnh...")
        for ten_anh in danh_sach_anh:
            duong_dan = os.path.join(THU_MUC_ANH, ten_anh)
            with open(duong_dan, 'rb') as tep_anh:
                await update.message.reply_photo(
                    photo=tep_anh,
                    caption=f"Ảnh: {ten_anh}"
                )
        await update.message.reply_text("Đã gửi tất cả ảnh!")
    else:
        await update.message.reply_text("Xin lỗi, tôi không tìm thấy ảnh nào trong thư mục.")
