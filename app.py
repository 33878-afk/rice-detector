import streamlit as str
from PIL import Image
import random
import time

# 1. ตั้งค่าหน้าตาของแอปพลิเคชัน
str.set_page_config(page_title="Rice Variety Detector", page_icon="🌾", layout="centered")

str.title("🌾 แอปพลิเคชันตรวจสอบสายพันธุ์ข้าว")
str.write("อัปโหลดรูปภาพเมล็ดข้าวของคุณ เพื่อให้ระบบช่วยวิเคราะห์สายพันธุ์")

# รายชื่อสายพันธุ์ข้าวที่รองรับ
CLASS_NAMES = ['ข้าวหอมมะลิ 105', 'ข้าวไรซ์เบอร์รี่', 'ข้าว กข6', 'ข้าวเสาไห้']

# 2. ส่วนการรับรูปภาพจากผู้ใช้ (อัปโหลด หรือ เปิดกล้อง)
source_radio = str.radio("เลือกวิธีใส่รูปภาพ:", ("อัปโหลดรูปภาพ", "เปิดกล้องถ่ายรูป"))

uploaded_file = None
if source_radio == "อัปโหลดรูปภาพ":
    uploaded_file = str.file_uploader("เลือกรูปภาพเมล็ดข้าว...", type=["jpg", "jpeg", "png"])
else:
    uploaded_file = str.camera_input("ถ่ายรูปเมล็ดข้าว")

# 3. ส่วนการประมวลผลและแสดงผลลัพธ์
if uploaded_file is not None:
    # แสดงรูปภาพที่ผู้ใช้อัปโหลด
    image = Image.open(uploaded_file)
    str.image(image, caption='รูปภาพที่นำเข้า', use_column_width=True)
    
    str.write("🔄 กำลังวิเคราะห์สายพันธุ์...")
    
    # ระบบจำลองเวลาประมวลผล
    time.sleep(2) 
    
    mock_breed = random.choice(CLASS_NAMES)
    mock_confidence = random.uniform(85.0, 99.9)
    
    # แสดงผลลัพธ์
    str.success(f"ผลลัพธ์ (จำลอง): **{mock_breed}**")
    str.info(f"ความมั่นใจ: {mock_confidence:.2f}%")

str.caption("พัฒนาโดยระบบ AI ตรวจสอบสายพันธุ์ข้าวไทย 2026")
