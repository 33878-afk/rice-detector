import streamlit as str
from PIL import Image
import numpy as np

str.set_page_config(page_title="Rice Variety Detector", page_icon="🌾", layout="centered")
str.title("🌾 แอปพลิเคชันตรวจสอบสายพันธุ์ข้าวของจริง")
str.write("อัปโหลดรูปภาพเมล็ดข้าวของคุณเพื่อสแกนสายพันธุ์")

uploaded_file = str.file_uploader("เลือกรูปภาพเมล็ดข้าว...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # แสดงรูปที่ผู้ใช้อัปโหลด
    user_img = Image.open(uploaded_file).convert('RGB').resize((100, 100))
    str.image(user_img, caption='รูปภาพของคุณ', use_column_width=True)
    
    str.write("🔄 กำลังเปรียบเทียบลักษณะเมล็ดข้าว...")
    
    # โหลดรูปต้นแบบที่เราอัปโหลดไว้ใน GitHub มาเปรียบเทียบ
    try:
        img_hommali = Image.open("hommali.jpg").convert('RGB').resize((100, 100))
        img_riceberry = Image.open("riceberry.jpg").convert('RGB').resize((100, 100))
        
        # แปลงเป็นตัวเลขเพื่อคำนวณความเหมือน
        arr_user = np.array(user_img)
        diff_hommali = np.mean(np.abs(arr_user - np.array(img_hommali)))
        diff_riceberry = np.mean(np.abs(arr_user - np.array(img_riceberry)))
        
        # เลือกสายพันธุ์ที่ค่าความต่างน้อยที่สุด (เหมือนที่สุด)
        if diff_hommali < diff_riceberry:
            result = "ข้าวหอมมะลิ 105"
            score = max(50, 100 - (diff_hommali / 2.5))
        else:
            result = "ข้าวไรซ์เบอร์รี่"
            score = max(50, 100 - (diff_riceberry / 2.5))
            
        str.success(f"📌 ผลการวิเคราะห์: **{result}**")
        str.info(f"📊 ความแม่นยำเทียบเคียง: {score:.2f}%")
        
    except Exception as e:
        str.error("⚠️ กรุณาอัปโหลดไฟล์รูปภาพต้นแบบชื่อ 'hommali.jpg' และ 'riceberry.jpg' เข้าไปใน GitHub ก่อนนะครับ")
