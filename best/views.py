from django.shortcuts import render


def new_best_post(request):
    return render(request, 'best/best_post.html')
