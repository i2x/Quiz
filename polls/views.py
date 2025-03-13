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



#private

def private_index(request):
    questions = PrivateQuestion.objects.all()

    return render(request, 'polls/index_private.html', {'questions': questions})

def private_detail(request, question_id):
    question = get_object_or_404(PrivateQuestion, pk=question_id)
    return render(request, 'polls/detail_private.html', {'question': question})

def private_vote(request, question_id):
    question = get_object_or_404(PrivateQuestion, pk=question_id)
    try:
        selected_choice = question.privatechoice_set.get(pk=request.POST['choice'])
        selected_choice.votes += 1
        selected_choice.save()
    except (KeyError, PrivateChoice.DoesNotExist):
        return render(request, 'polls/detail_private.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    return redirect('polls:private_results', question_id=question.id)

def private_results(request, question_id):
    question = get_object_or_404(PrivateQuestion, pk=question_id)
    return render(request, 'polls/results_private.html', {'question': question})

def private_reset_votes(request, question_id):
    question = get_object_or_404(PrivateQuestion, pk=question_id)
    question.privatechoice_set.update(votes=0)  # รีเซ็ตคะแนนโหวตทั้งหมดเป็น 0
    return redirect('polls:private_index')  # รีเฟรชหน้า index หลังรีเซ็ต