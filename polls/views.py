from django.shortcuts import render, redirect
from .models import poll, choice
from django.shortcuts import get_object_or_404


def polls_list(request):
    polls = poll.objects.all()
    context = {'polls': polls}
    return render(request, 'polls/polls_list.html', context)


def polls_detail(request, poll_id):
    polls = get_object_or_404(poll, id=poll_id)
    context = {'poll': polls}
    return render(request, 'polls/polls_details.html', context)


def poll_vote(request, poll_id):
    choice_id = request.POST.get('choice')
    if choice_id:
        c = choice.objects.get(id=choice_id)
        p = c.question
        c.votes += 1
        c.save()
        return render(request, 'polls/polls_results.html', {'poll': p})
    return render(request, 'polls/polls_results.html', {'error': True})