from django.shortcuts import render, get_object_or_404, redirect
from .models import Question, Choice ,PrivateQuestion,PrivateChoice

def index(request):
    questions = Question.objects.all()

    return render(request, 'polls/index.html', {'questions': questions})

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
        selected_choice.votes += 1
        selected_choice.save()
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    return redirect('polls:results', question_id=question.id)

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

def reset_votes(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    question.choice_set.update(votes=0)  # รีเซ็ตคะแนนโหวตทั้งหมดเป็น 0
    return redirect('polls:index')  # รีเฟรชหน้า index หลังรีเซ็ต


# Private Polls
def private_index(request, token=None):

    questions = PrivateQuestion.objects.filter(token=token)
    return render(request, 'polls/index_private.html', {'questions': questions, 'token': token})

def private_detail(request, token, question_id):

    question = get_object_or_404(PrivateQuestion, token=token, pk=question_id)
    return render(request, 'polls/detail_private.html', {'question': question, 'token': token})

def private_vote(request, token, question_id):

    question = get_object_or_404(PrivateQuestion, token=token, pk=question_id)
    try:
        selected_choice = question.privatechoice_set.get(pk=request.POST['choice'])  # ใช้ related_name
        selected_choice.votes += 1
        selected_choice.save()
    except (KeyError, PrivateChoice.DoesNotExist):
        return render(request, 'polls/detail_private.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
            'token': token,
        })
    return redirect('polls:private_results', token=token, question_id=question.id)

def private_results(request, token, question_id):

    question = get_object_or_404(PrivateQuestion, token=token, pk=question_id)
    return render(request, 'polls/results_private.html', {'question': question, 'token': token})

def private_reset_votes(request, token, question_id):

    question = get_object_or_404(PrivateQuestion, token=token, pk=question_id)
    question.privatechoice_set.update(votes=0)  # ใช้ related_name
    return redirect('polls:private_index_with_token', token=token)  # รีเฟรชหน้า index ของ token นั้น
