from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest

class PollAppFunctionalTest(unittest.TestCase):
    
    def setUp(self):
        """เปิดเว็บเบราว์เซอร์ก่อนเริ่มการทดสอบ"""
        options = webdriver.ChromeOptions()
        self.browser = webdriver.Chrome(options=options)
        self.browser.implicitly_wait(5)  # รอให้ elements โหลด

    def tearDown(self):
        """ปิดเบราว์เซอร์หลังจากทดสอบเสร็จ"""
        self.browser.quit()

    def test_sompong_takes_poll(self):
        """สมปองเข้าร่วมโพลและโหวตตัวเลือกที่ชอบ"""

        # เปิดหน้าโพล
        self.browser.get('http://127.0.0.1:8000/polls/')
        
        # เช็คว่ามีคำถามอย่างน้อย 1 ข้อ
        questions = self.browser.find_elements(By.TAG_NAME, "li")
        self.assertGreater(len(questions), 0, "ไม่มีคำถามให้โหวต!")

        # เลือกคำถามแรก
        first_question_link = questions[0].find_element(By.TAG_NAME, "a")
        first_question_link.click()

        # เช็คว่าไปที่หน้าโหวตแล้วหรือนัง
        self.assertIn("/polls/", self.browser.current_url)
        choices = self.browser.find_elements(By.NAME, "choice")
        # เช็คว่ามีตัวเลือกอย่างน้อย 2
        self.assertGreaterEqual(len(choices), 2, "ตัวเลือกไม่ครบ!")

        # สมปองเลือก "หมา" แล้วคลิ๊ก
        choice_dog = self.browser.find_element(By.CSS_SELECTOR, "input[value='1']")
        choice_dog.click()
        
        # กดปุ่มส่งคำตอบ
        submit_button = self.browser.find_element(By.CSS_SELECTOR, "input[type='submit']")
        submit_button.click()

        # ตรวจสอบว่าถูกนำไปยังหน้าผลลัพธ์
        self.assertIn("/results/", self.browser.current_url)

        # ดูว่าผลโหวตถูกบันทึกแล้ว
        results = self.browser.find_elements(By.TAG_NAME, "li")
        self.assertTrue(any("dog -" in result.text.lower() for result in results), "ไม่มีผลโหวตของ 'หมา'!")
        self.assertTrue(any("cat -" in result.text.lower() for result in results), "ไม่มีผลโหวตของ 'แมว'!")

        # สมปองกดปุ่ม Back to Polls เพื่อกลับไปที่หน้าคำถาม
        back_to_polls_link = self.browser.find_element(By.LINK_TEXT, "Back to Polls")
        back_to_polls_link.click()
        
        self.assertIn("/polls/", self.browser.current_url)

if __name__ == '__main__':
    unittest.main()
