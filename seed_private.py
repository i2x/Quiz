import os
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mypoll.settings')  
django.setup()

from polls.models import PrivateQuestion, PrivateChoice  

def seed_data():
    questions = [
        {
            "question_text": "Private: What is your favorite hospital?",
            "token": "hospital",  
            "choices": ["Bangkok Hospital", "Samitivej", "Bumrungrad", "Rajavithi"]
        },
        {
            "question_text": "Private: What is your fishing preference?",
            "token": "fishing", 
            "choices": ["Freshwater", "Saltwater", "Fly Fishing", "Deep Sea"]
        },
        {
            "question_text": "Private: Which sports do you enjoy?",
            "token": "sport", 
            "choices": ["Football", "Basketball", "Tennis", "Badminton"]
        },
    ]

    for q_data in questions:
        question, created = PrivateQuestion.objects.get_or_create(
            question_text=q_data["question_text"],
            defaults={"token": q_data["token"]}  # กำหนด token
        )

        if created:
            print(f"Created question: {question} (Token: {q_data['token']})")
        else:
            print(f"Question already exists: {question} (Updating token: {q_data['token']})")
            question.token = q_data["token"]
            question.save()  # อัปเดต token ถ้าเปลี่ยนแปลง

        for choice_text in q_data["choices"]:
            choice, _ = PrivateChoice.objects.get_or_create(question=question, choice_text=choice_text)
            print(f"  - Added choice: {choice_text}")

if __name__ == "__main__":
    seed_data()
