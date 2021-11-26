from django.shortcuts import render
from django.http import HttpResponseNotFound, HttpResponseRedirect, Http404, HttpResponse
from django.urls import reverse
from datetime import date

post_dict = {
    'one': 'good morning',
    'two': 'good afternoon',
    'three': 'good evening',
    'four': 'good night',
    'five': 'goodbye'
}

post_dicts = [
    {
        'slug': 'hike-in-the-moutains',
        'author': 'helen',
        'date': date(2021, 11, 26),
        'image': 'mountains.jpg',
        'title': 'Hiking in the Mountains',
        'excerpt': 'I love hiking in the mountains',
        'content': """
                Lorem ipsum dolor sit amet consectetur adipisicing elit.
                 Doloremque unde ad sint accusantium veritatis laborum ex,
                 facilis eos sequi! Beatae, asperiores? Error nisi nam optio
                 assumenda quasi aperiam sint ullam? """
    },
    {
        "slug": "programming-is-fun",
        "image": "coding.jpg",
        "author": "Maximilian",
        "date": date(2022, 3, 10),
        "title": "Programming Is Great!",
        "excerpt": "Did you ever spend hours searching that one error in your code? Yep - that's what happened to me yesterday...",
        "content": """
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
        """
    },
    {
        "slug": "into-the-woods",
        "image": "woods.jpg",
        "author": "Maximilian",
        "date": date(2020, 8, 5),
        "title": "Nature At Its Best",
        "excerpt": "Nature is amazing! The amount of inspiration I get when walking in nature is incredible!",
        "content": """
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
        """
    }
]

def get_date(post):
    return post['date']

# Create your views here.
def index(request):
    """ returns homepage """
    sorted_posts = sorted(post_dicts, key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, 'blog/index.html', {
        'posts': latest_posts
    })


def posts(request):
    """ returns summary of all posts """
    return render(request, 'blog/posts.html', {
        'all_posts': post_dicts
    })


def post_by_number(request, selected_post):
    post_list = list(post_dict.keys())
    
    if selected_post > len(post_list):
        return HttpResponseNotFound('Sorry there aren\'t that many posts!') 

    post_num = post_list[selected_post-1]
    redirect_path = reverse("post", args=[post_num])
    return HttpResponseRedirect(redirect_path)



def post(request, selected_post):
    try:
        text = post_dict[selected_post]
        return render(request, "blog/post.html", {
            'text': text,
            'post': selected_post
        })
    except:
        raise Http404()

  