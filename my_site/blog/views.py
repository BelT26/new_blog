from django.shortcuts import render
from django.http import  HttpResponseNotFound, HttpResponseRedirect, Http404


post_dict = {
    'one': 'good morning',
    'two': 'good afternoon',
    'three': 'good evening',
    'four': 'good night',
    'five': 'goodbye'
}


# Create your views here.
def index(request):
    """ returns homepage """
    post_list = list(post_dict.keys())
    return render(request, 'blog/index.html')


def posts(request):
    """ returns summary of all posts """
    post_list = list(post_dict.keys())
    return render(request, 'blog/posts.html', {
        'posts': post_list
    })


def post(request):
    """ returns an individual post """
    return render(request, 'blog/post.html')
    

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {
            'text': challenge_text,
            'month': month
        })
    except:
        raise Http404()
  