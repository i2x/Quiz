import os
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mypoll.settings')  # Replace with your project name
django.setup()

from polls.models import Question, Choice  # Replace 'your_app' with your Django app name

def seed_data():
    questions = [
        {
            "question_text": "What is your favorite color?",
            "choices": ["Red", "Blue", "Green", "Yellow"]
        },
        {
            "question_text": "Which season do you prefer?",
            "choices": ["Spring", "Summer", "Autumn", "Winter"]
        },
        {
            "question_text": "What is your preferred programming language?",
            "choices": ["Python", "JavaScript", "Java", "C++"]
        },
        {
            "question_text": "What type of movies do you like?",
            "choices": ["Action", "Comedy", "Drama", "Horror"]
        },
        {
            "question_text": "What is your favorite pet?",
            "choices": ["Dog", "Cat", "Bird", "Fish"]
        },
    ]

    for q_data in questions:
        question, created = Question.objects.get_or_create(question_text=q_data["question_text"])
        if created:
            print(f"Created question: {question}")
        else:
            print(f"Question already exists: {question}")

        for choice_text in q_data["choices"]:
            choice, _ = Choice.objects.get_or_create(question=question, choice_text=choice_text)
            print(f"  - Added choice: {choice_text}")

if __name__ == "__main__":
    seed_data()
