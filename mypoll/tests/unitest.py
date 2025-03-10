from django.test import TestCase
from polls.models import Question, Choice

class QuestionModelTest(TestCase):

    def setUp(self):
        """สร้างคำถามและตัวเลือกก่อนการทดสอบ"""
        self.question = Question.objects.create(question_text="What's your favorite color?")
        self.choice1 = Choice.objects.create(question=self.question, choice_text="Red", votes=5)
        self.choice2 = Choice.objects.create(question=self.question, choice_text="Blue", votes=10)

    def test_question_str(self):
        """ทดสอบว่า __str__() ของ Question แสดงข้อความถูกต้อง"""
        self.assertEqual(str(self.question), "What's your favorite color?")

    def test_total_votes(self):
        """ทดสอบว่า total_votes() คำนวณผลรวมคะแนนโหวตถูกต้อง"""
        total = self.question.total_votes()
        self.assertEqual(total, 15)  # 5 + 10

class ChoiceModelTest(TestCase):

    def setUp(self):
        """สร้างคำถามและตัวเลือกก่อนการทดสอบ"""
        self.question = Question.objects.create(question_text="What is your favorite fruit?")
        self.choice = Choice.objects.create(question=self.question, choice_text="Apple", votes=3)

    def test_choice_str(self):
        """ทดสอบว่า __str__() ของ Choice แสดงข้อความถูกต้อง"""
        self.assertEqual(str(self.choice), "Apple")

    def test_choice_default_votes(self):
        """ทดสอบว่า votes เริ่มต้นเป็น 0 ถ้าไม่ได้กำหนดค่า"""
        new_choice = Choice.objects.create(question=self.question, choice_text="Banana")
        self.assertEqual(new_choice.votes, 0)  # ค่าเริ่มต้นต้องเป็น 0
