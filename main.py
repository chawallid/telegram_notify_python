import requests

def telegram_notify(message):
    # API Token ของบอทที่ได้จาก BotFather
    bot_token = 'YOUR_BOT_API_TOKEN'  # ใส่ API Token ของคุณที่นี่
    # Chat ID ของผู้ใช้ที่ต้องการให้บอทส่งข้อความไป
    chat_id = 'YOUR_CHAT_ID'  # ใส่ Chat ID ของคุณที่นี่

    # URL สำหรับส่งข้อความผ่าน API
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"

    # พารามิเตอร์ที่ใช้ส่งข้อความ
    payload = {
        'chat_id': chat_id,
        'text': message
    }

    # ส่ง request ไปยัง API ของ Telegram
    response = requests.post(url, data=payload)

    # ตรวจสอบสถานะการส่งข้อความ
    if response.status_code == 200:
        print("Notification sent successfully!")
    else:
        print(f"Failed to send notification. Error: {response.status_code}")

# ตัวอย่างการใช้งานฟังก์ชัน telegram_notify
telegram_notify("Hello from Python! This is a test notification.")
