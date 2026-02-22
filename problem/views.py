from django.shortcuts import render
from .models import Problem
from django.core.paginator import Paginator

def problem_list(request):
    difficulty = request.GET.get('difficulty')

    problems = Problem.objects.all().order_by('-created_at')

    if difficulty:
        problems = problems.filter(difficulty=difficulty)

    paginator = Paginator(problems, 5)  # 5 per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'difficulty': difficulty
    }

    return render(request, 'problems/problem_list.html', context)


from django.shortcuts import get_object_or_404

def problem_detail(request, pk):
    problem = get_object_or_404(Problem, pk=pk)

    context = {
        'problem': problem
    }

    return render(request, 'problems/problem_detail.html', context)