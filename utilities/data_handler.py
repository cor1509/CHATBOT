import json

def tai_du_lieu_tro_chuyen():
    try:
        with open('du_lieu_tro_chuyen.json', 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        return {
            "chao_hoi": {
                "mau": ["xin chào", "chào", "hi", "hello", "hey"],
                "tra_loi": [
                    "Xin chào! Rất vui được gặp bạn!",
                    "Chào bạn! Hôm nay bạn thế nào?",
                    "Hello! Mình có thể giúp gì cho bạn không?"
                ]
            },
            "loi_biet": {
                "mau": ["tạm biệt", "bye", "goodbye", "gặp lại sau"],
                "tra_loi": [
                    "Tạm biệt bạn! Hẹn gặp lại!",
                    "Goodbye! Chúc bạn một ngày tốt lành!",
                    "Hẹn gặp lại bạn sau nhé!"
                ]
            },
            "cam_on": {
                "mau": ["cảm ơn", "thank", "thanks"],
                "tra_loi": [
                    "Không có gì! Rất vui được giúp bạn!",
                    "Không có chi! Bạn cần gì cứ nói nhé!",
                    "Rất vui khi được giúp đỡ bạn!"
                ]
            },
            "hoi_suc_khoe": {
                "mau": ["khỏe không", "thế nào", "how are you"],
                "tra_loi": [
                    "Mình khỏe, cảm ơn bạn! Còn bạn thì sao?",
                    "Mình vẫn ổn! Hy vọng bạn cũng vậy!",
                    "Mình luôn trong trạng thái tốt nhất để phục vụ bạn!"
                ]
            },
            "thoi_tiet": {
                "mau": ["thời tiết", "weather", "nắng", "mưa"],
                "tra_loi": [
                    "Bạn quan tâm đến thời tiết à? Hãy tận hưởng ngày hôm nay!",
                    "Dù thời tiết thế nào, quan trọng là tâm trạng bạn tốt!",
                    "Thời tiết là một chủ đề thú vị đấy!"
                ]
            },
            "so_thich": {
                "mau": ["sở thích", "thích gì", "hobby"],
                "tra_loi": [
                    "Mình thích trò chuyện với mọi người như thế này!",
                    "Việc giúp đỡ mọi người là sở thích của mình!",
                    "Mình thích học hỏi những điều mới từ các cuộc trò chuyện!"
                ]
            },
            "hoc_tap": {
                "mau": ["học", "bài tập", "kiến thức", "giáo dục"],
                "tra_loi": [
                    "Học tập là chìa khóa của sự phát triển! Bạn đang học gì thú vị không?",
                    "Kiến thức là sức mạnh! Tôi luôn sẵn sàng hỗ trợ bạn trong việc học.",
                    "Việc học không bao giờ là vô ích. Mỗi ngày chúng ta đều có thể học được điều mới!",
                    "Giáo dục mở ra những cánh cửa mới. Bạn đang theo đuổi điều gì?",
                    "Học tập là hành trình suốt đời. Tôi rất thích nghe về những điều bạn đang nghiên cứu!"
                ]
            },
            "am_thuc": {
                "mau": ["ăn", "ẩm thực", "nấu ăn", "món ăn"],
                "tra_loi": [
                    "Ẩm thực là một trong những niềm đam mê tuyệt vời của con người! Bạn thích ẩm thực gì nhất?",
                    "Nấu ăn là một nghệ thuật tuyệt vời. Bạn có sở thích nấu nướng không?",
                    "Mỗi món ăn đều có câu chuyện riêng của nó. Bạn có câu chuyện thú vị về ẩm thực không?",
                    "Ẩm thực là cầu nối văn hóa. Tôi rất thích nghe về các món ăn đặc trưng!",
                    "Thức ăn không chỉ là để no, mà còn là để thưởng thức!"
                ]
            },
            "du_lich": {
                "mau": ["du lịch", "travel", "phượt", "đi chơi"],
                "tra_loi": [
                    "Du lịch là cách tuyệt vời để khám phá thế giới! Bạn đã từng đi du lịch ở đâu?",
                    "Mỗi chuyến đi là một câu chuyện mới. Bạn có kỷ niệm du lịch nào thú vị không?",
                    "Khám phá những địa điểm mới luôn là trải nghiệm tuyệt vời!",
                    "Du lịch giúp chúng ta mở rộng tầm nhìn và hiểu biết. Bạn thích loại hình du lịch nào?",
                    "Những chuyến đi mang đến cho chúng ta những kỷ niệm đáng nhớ!"
                ]
            },
            "cong_nghe": {
                "mau": ["công nghệ", "máy tính", "internet", "smartphone"],
                "tra_loi": [
                    "Công nghệ đang thay đổi thế giới một cách nhanh chóng! Bạn có suy nghĩ gì về điều này?",
                    "Những tiến bộ công nghệ mới luôn làm tôi thích thú. Bạn đang quan tâm đến công nghệ gì?",
                    "Internet đã kết nối chúng ta như thế nào! Bạn nghĩ gì về điều này?",
                    "Smartphone đã trở thành một phần không thể thiếu trong cuộc sống hiện đại.",
                    "Công nghệ mang đến những giải pháp tuyệt vời cho cuộc sống!"
                ]
            },
            "mac_dinh": {
                "tra_loi": [
                    "Rất tiếc, tôi không hiểu ý bạn. Bạn có thể nói rõ hơn không?",
                    "Xin lỗi, tôi chưa hiểu bạn muốn nói gì. Bạn có thể giải thích thêm không?",
                    "Tôi chưa hiểu được ý của bạn. Bạn có thể nói lại không?",
                    "Có vẻu như chúng ta đang gặp khó khăn trong việc giao tiếp. Bạn có thể diễn đạt lại không?",
                    "Tôi rất muốn hiểu bạn, nhưng có vẻ như tôi đang bỡ ngỡ. Bạn giúp tôi hiểu rõ hơn được không?"
                ]
            }
        }