## user story for poll app

สมปองเปิด url สำหรับ poll app
สมปองเห็นคำถามหลายข้อ
สมปองคลิ๊กที่คำถามข้อแรก
ทำการ redirect ไปที่หน้า detail แสดง คำถาม ตัวเลือก A,B
สมปองเลือกตัวเลือก A และกด submit
สมปองถูกส่งไปที่หน้าแสดง result แสดงจำนวนครั้งที่เลือก A,B ก่อนหน้านี้รวมกับของตน
สมปองกด back เพื่อกลับสู่หน้าคำถาม




## เวอรชั่น 0.0.1 
-คำถามที่มีการโหวต 50 ครั้งขึ้นไปให้แสดง hot
-คำถามที่มีการโหวต 15 ครั้งขึ้นไปให้แสดง warm



## คำถามพิเศษ ถ้าไม่ต้อง login แล้วให้ user เห็นเฉพาะตำถามของตัวเอง

ตอบ

ที่ polls/model เพิ่ม token เข้าไปดังนี้

class PrivateQuestion(models.Model):
    question_text = models.CharField(max_length=200)
    token = models.CharField(max_length=50) # เพิ่ม token

 โดย url จะให้มีการรับ param ของ token และเลขที่ของคำถามด้วยถ้าใส่ถูกถึงจะสามารถโหวตได้เช่น

 /private/1/{random}/   

ก็นำ token ไปเช็ตใน view.py
โดยแก้ให้ PrivateQuestion.objects.all() ทำการ fillter ด้วย token ก่อน


def private_index(request):
    questions = PrivateQuestion.objects.all() <= เราจะแก้ตรงนี้เป็น

    PrivateQuestion.objects.filter(token="random") <= เป็นแบบนี้เพื่อให้เขามีสิทธดูเฉพาะ token ที่เขาได้

    เช่น ร้านปลากก็อาจะมี token=fishing_sdfdsgshewher , 
    โรงบาลก็มี token=hospital_dsfsdfew33f






