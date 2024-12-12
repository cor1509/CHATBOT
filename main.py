import platform
import asyncio
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from utilities.config import TOKEN
from handlers.commands import bat_dau, thong_tin, gui_anh, gui_tat_ca_anh
from handlers.messages import xu_ly_tin_nhan
from utilities.setup_nltk import cai_dat_nltk

async def lenh_khong_xac_dinh(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
   
    await update.message.reply_text(
        "Tôi không chắc phải trả lời như thế nào. "
        "Bạn có thể dùng lệnh /batdau để xem danh sách lệnh có sẵn"
    )

def chay_bot():
    if platform.system() == "Windows":
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    try:
        cai_dat_nltk()
        application = Application.builder().token(TOKEN).build()

        application.add_handler(CommandHandler("batdau", bat_dau))
        application.add_handler(CommandHandler("thongtin", thong_tin))
        application.add_handler(CommandHandler("anh", gui_anh))
        application.add_handler(CommandHandler("tatcaanh", gui_tat_ca_anh))
        application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, xu_ly_tin_nhan))
        application.add_handler(MessageHandler(filters.COMMAND, lenh_khong_xac_dinh))
        print("Bot đã sẵn sàng!")
        application.run_polling(allowed_updates=Update.ALL_TYPES)

    except Exception as e:
        print(f"Lỗi: {e}")
    finally:
        loop.close()

if __name__ == '__main__':
    chay_bot()