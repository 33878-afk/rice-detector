import streamlit as str
import tensorflow as tf
from PIL import Image, ImageOps
import numpy as np

# 1. ตั้งค่าหน้าตาของแอปพลิเคชัน
str.set_page_config(page_title="Rice Variety Detector", page_icon="🌾", layout="centered")

str.title("🌾 แอปพลิเคชันตรวจสอบสายพันธุ์ข้าว")
str.write("อัปโหลดรูปภาพเมล็ดข้าวของคุณ เพื่อให้ AI ช่วยวิเคราะห์สายพันธุ์")

# 2. ฟังก์ชันโหลดโมเดล AI (ใส่ @str.cache_resource เพื่อให้แอปโหลดโมเดลแค่ครั้งเดียว ไม่โหลดใหม่ทุกรอบ)
@str.cache_resource
def load_my_model():
    try:
        model = tf.keras.models.load_model('rice_model.h5')
        return model
    except:
        return None

model = load_my_model()

# รายชื่อสายพันธุ์ข้าวที่รองรับ (ตัวอย่าง)
CLASS_NAMES = ['ข้าวหอมมะลิ 105', 'ข้าวไรซ์เบอร์รี่', 'ข้าว กข6', 'ข้าวเสาไห้']

# 3. ส่วนการรับรูปภาพจากผู้ใช้ (อัปโหลด หรือ เปิดกล้อง)
source_radio = str.radio("เลือกวิธีใส่รูปภาพ:", ("อัปโหลดรูปภาพ", "เปิดกล้องถ่ายรูป"))

uploaded_file = None
if source_radio == "อัปโหลดรูปภาพ":
    uploaded_file = str.file_uploader("เลือกรูปภาพเมล็ดข้าว...", type=["jpg", "jpeg", "png"])
else:
    uploaded_file = str.camera_input("ถ่ายรูปเมล็ดข้าว")

# 4. ส่วนการประมวลผลและแสดงผลลัพธ์
if uploaded_file is not None:
    # แสดงรูปภาพที่ผู้ใช้อัปโหลด
    image = Image.open(uploaded_file)
    str.image(image, caption='รูปภาพที่นำเข้า', use_column_width=True)
    
    str.write("🔄 กำลังวิเคราะห์สายพันธุ์...")
    
    if model is not None:
        # --- กรณีมีไฟล์โมเดลจริง ---
        size = (224, 224)
        image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)
        
        img_array = np.asarray(image)
        normalized_image_array = (img_array.astype(np.float32) / 127.5) - 1
        
        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
        data[0] = normalized_image_array
        
        prediction = model.predict(data)
        index = np.argmax(prediction)
        class_name = CLASS_NAMES[index]
        confidence_score = prediction[0][index]
        
        str.success(f"ผลลัพธ์: **{class_name}**")
        str.info(f"ความมั่นใจของ AI: {confidence_score * 100:.2f}%")
        
    else:
        # --- กรณีที่ยังไม่มีไฟล์โมเดล (ระบบจำลองเพื่อทดสอบ UI) ---
        import random
        import time
        time.sleep(2) 
        
        mock_breed = random.choice(CLASS_NAMES)
        mock_confidence = random.uniform(85.0, 99.9)
        
        str.warning("⚠️ ไม่พบไฟล์ 'rice_model.h5' (นี่คือระบบจำลองผลลัพธ์)")
        str.success(f"ผลลัพธ์ (จำลอง): **{mock_breed}**")
        str.info(f"ความมั่นใจ (จำลอง): {mock_confidence:.2f}%")

str.caption("พัฒนาโดยระบบ AI ตรวจสอบสายพันธุ์ข้าวไทย 2026")
