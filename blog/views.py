from datetime import date

from django.shortcuts import render

# Create your views here.

all_posts = [
    {
        "slug": "hike-in-the-mountains",
        "image": "mountains.jpg",
        "author": "Natan",
        "date": date(2021, 7, 21),
        "title": "Mountain Hiking",
        "excerpt": "There's nothing like the views you get when hiking in the mountains! and I wansn't even prepared for what happened whilst I was enjoying the view!",
        "content": """
        Lorem ipsum dolor sit amet consectetur, adipisicing elit. 
        Suscipit ex atque magni quis nisi saepe consectetur velit, 
        quod dolorem earum neque dolor ab, id doloribus iusto eius beatae tempora quasi!

        Lorem ipsum dolor sit amet consectetur, adipisicing elit. 
        Suscipit ex atque magni quis nisi saepe consectetur velit, 
        quod dolorem earum neque dolor ab, id doloribus iusto eius beatae tempora quasi!

        Lorem ipsum dolor sit amet consectetur, adipisicing elit. 
        Suscipit ex atque magni quis nisi saepe consectetur velit, 
        quod dolorem earum neque dolor ab, id doloribus iusto eius beatae tempora quasi!
        """
    },
    {
        "slug": "programming-is-fun",
        "image": "coding.jpg",
        "author": "Natan",
        "date": date(2021, 3, 10),
        "title": "Programming Is Great",
        "excerpt": "There's nothing like Coding Django in Python!",
        "content": """
        Lorem ipsum dolor sit amet consectetur, adipisicing elit. 
        Suscipit ex atque magni quis nisi saepe consectetur velit, 
        quod dolorem earum neque dolor ab, id doloribus iusto eius beatae tempora quasi!

        Lorem ipsum dolor sit amet consectetur, adipisicing elit. 
        Suscipit ex atque magni quis nisi saepe consectetur velit, 
        quod dolorem earum neque dolor ab, id doloribus iusto eius beatae tempora quasi!

        Lorem ipsum dolor sit amet consectetur, adipisicing elit. 
        Suscipit ex atque magni quis nisi saepe consectetur velit, 
        quod dolorem earum neque dolor ab, id doloribus iusto eius beatae tempora quasi!
        """
    },
    {
        "slug": "into-the-woods",
        "image": "woods.jpg",
        "author": "Natan",
        "date": date(2021, 8, 13),
        "title": "Nature At Its Best!",
        "excerpt": "Nature is Amazing! The amount of inspiration I get when walking in the woods",
        "content":
        """
        Lorem ipsum dolor sit amet consectetur, adipisicing elit. 
        Suscipit ex atque magni quis nisi saepe consectetur velit, 
        quod dolorem earum neque dolor ab, id doloribus iusto eius beatae tempora quasi!

        Lorem ipsum dolor sit amet consectetur, adipisicing elit. 
        Suscipit ex atque magni quis nisi saepe consectetur velit, 
        quod dolorem earum neque dolor ab, id doloribus iusto eius beatae tempora quasi!

        Lorem ipsum dolor sit amet consectetur, adipisicing elit. 
        Suscipit ex atque magni quis nisi saepe consectetur velit, 
        quod dolorem earum neque dolor ab, id doloribus iusto eius beatae tempora quasi!
        """
    }
]


def get_date(post):
    return post['date']


def starting_page(request):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, 'blog/index.html', {
        "posts": latest_posts
    })


def posts(request):
    return render(request, 'blog/all-posts.html', {
        "all_posts": all_posts
    })


def post_detail(request, slug):
    identified_post = next(post for post in all_posts if post['slug'] == slug)
    return render(request, 'blog/post-detail.html', {
        "post": identified_post
    })
