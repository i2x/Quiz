import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class PollAppFunctionalTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """เริ่มต้น WebDriver ครั้งเดียวสำหรับทั้งคลาส"""
        cls.driver = webdriver.Chrome()
        cls.driver.get("http://127.0.0.1:8000/polls/")

    def test_vote_until_hot(self):
        driver = self.driver

        # รีเซ็ตคะแนน
        driver.find_element(By.ID, "reset-button-1").click()
        time.sleep(0.05)

        while True:
            driver.find_element(By.ID, "question-link-1").click()
            time.sleep(0.05)

            driver.find_element(By.ID, "choice-1").click()
            driver.find_element(By.ID, "submit-button").click()
            time.sleep(0.05)

            driver.get("http://127.0.0.1:8000/polls/")
            time.sleep(0.05)

            # อ่านค่า vote count
            question_link = driver.find_element(By.ID, "question-link-1")
            vote_count = int(question_link.get_attribute("value"))

            # อ่านข้อความทั้งหมดของ question-1
            question_text = driver.find_element(By.ID, "question-1").text

            # กำหนดป้ายกำกับที่ควรจะเป็น
            expected_label = ""
            if vote_count >= 50:
                expected_label = "🔥 Hot"
            elif vote_count >= 10:
                expected_label = "🥰 Warm"

            # ตรวจสอบว่าป้ายกำกับที่แสดงในหน้าเว็บคืออะไร
            if "🔥 Hot" in question_text:
                actual_label = "🔥 Hot"
            elif "🥰 Warm" in question_text:
                actual_label = "🥰 Warm"
            else:
                actual_label = ""

            # ตรวจสอบว่าป้ายกำกับถูกต้อง
            self.assertEqual(expected_label, actual_label, 
                             f"Vote {vote_count} expected '{expected_label}' but got '{actual_label}'")

            # แสดงค่า vote_count
            print(f"vote: {vote_count} ✅ Label check passed ({expected_label})")

            if vote_count >= 55:
                break


    @classmethod
    def tearDownClass(cls):
        """ปิด WebDriver เมื่อทดสอบเสร็จ"""
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()
