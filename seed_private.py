import os
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mypoll.settings')  
django.setup()

from polls.models import PrivateQuestion, PrivateChoice  
def seed_data():
    questions = [
        {
            "question_text": "Private:What is your favorite animal?",
            "choices": ["Cat", "Bat", "Rat", "Dog"]
        },
        {
            "question_text": "Private:Which website do you prefer?",
            "choices": ["google", "facebook", "shopee", "lasada"]
        },
        {
            "question_text": "Private:What is your preferred  language?",
            "choices": ["English", "Thai", "India", "Russia"]
        },

    ]

    for q_data in questions:
        question, created = PrivateQuestion.objects.get_or_create(question_text=q_data["question_text"])
        if created:
            print(f"Created question: {question}")
        else:
            print(f"Question already exists: {question}")

        for choice_text in q_data["choices"]:
            choice, _ = PrivateChoice.objects.get_or_create(question=question, choice_text=choice_text)
            print(f"  - Added choice: {choice_text}")

if __name__ == "__main__":
    seed_data()
