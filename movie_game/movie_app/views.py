from django.shortcuts import render
from movie_app.models import actor_name
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_protect

def home(request):
    return render(request, 'movie_app/home.html')

def evaluate(request):
    if request.method == 'POST':

        form_submitted = True

        true_actor = request.POST.get('actor')
        user_answer = request.POST.get('answer')

        correct_answer = user_answer.lower() == true_actor
        return render(request, 'movie_app/quiz.html', {'actor': true_actor, 'is_correct': correct_answer, 'form_submitted': form_submitted})

    
def refresh(request):
    random_actor = actor_name.objects.order_by('?').first()
    html_content = render_to_string('movie_app/quiz.html', {'actor': random_actor})
    return HttpResponse(html_content)