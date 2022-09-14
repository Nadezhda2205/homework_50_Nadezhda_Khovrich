import json
from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest
from cat_app.services.cat import Cat


def index(request):
    return render(request, "index.html")


def cat_stats(request: WSGIRequest):
    if request.method == 'GET':
        cat = Cat(name=request.GET.get('cat_name'))

    elif request.method == 'POST':
        
        with open('cat_app/services/cat.json', 'r') as f:
            from_json = json.load(f)

        cat = Cat(
            name=from_json['name'], 
            age=from_json['age'],
            mood=from_json['mood'], 
            satiety=from_json['satiety'],
            state_sleep=from_json['state_sleep'],
        )

        action = request.POST.get('action')
        
        if action == 'feed':
            cat.feed()
        elif action == 'play':
            cat.play()
        elif action == 'sleep':
            cat.sleep()
            
    cat.save()


    context = {
        'name': cat.name,
        'age': cat.age,
        'mood': cat.mood,
        'satiety': cat.satiety,
        'img_url': cat.img_url
    }
    return render(request, "cat_stats.html", context=context)
