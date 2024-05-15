#!/usr/bin/env python

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
from line_notify import LineNotify
from datetime import datetime, time

# กำหนด Token ที่คุณได้จาก LINE Notify
token = "Your Token"
notify = LineNotify(token)

reader = SimpleMFRC522()

# เวลาเข้างานและเวลาออกงาน
start_work_time = time(9, 0)  # 9:00 เช้า
end_work_time = time(17, 0)   # 8:00 โมงเย็น

try:
    id, text = reader.read()
    print('hello')
    print(id)
    print(text)

    # ส่งข้อความผ่าน LINE Notify
    message = f"\n🔖 : {id}\n👤 :คุณ {text}\n📅 : {datetime.now().strftime('%Y-%m-%d')}\n🕒 : {datetime.now().strftime('%H:%M')}\n📝 :"


    # ตรวจสอบเวลาและส่งข้อความตามเงื่อนไข
    now = datetime.now().time()
    if now < start_work_time:
        message += "You're early! Please wait for the work time."
    elif now >= start_work_time and now <= time(11, 0):
        message += "You're on time! Have a productive day!"
    elif now > time(11, 0) and now <= time(14, 0):
        late_minutes = (now.hour - start_work_time.hour) * 60 + (now.minute - start_work_time.minute)
        message += f"You're late! Please inform your supervisor. Late for {late_minutes} minutes."
    elif now > time(14, 0) and now <= end_work_time:
        message += "You're on time! Have a productive afternoon!"
    elif now > end_work_time and now <= time(20, 0):
        message += "You're leaving! Goodbye, see you tomorrow!"
    else:
        message += "Today's date: " + datetime.now().strftime("%Y-%m-%d")

    notify.send(message)
    print("Message sent to LINE Notify")
finally:
    GPIO.cleanup()
