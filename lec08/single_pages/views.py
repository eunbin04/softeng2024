from django.shortcuts import render

# Create your views here.
def landing_page(request):
    return render(request, 'single_pages/landing.html', {'title': 'Home'})

def about_page(request):
    return render(request, 'single_pages/about_me.html', {'title': 'About Me'})


def blog_list(request):
    post_list = [
        {
            'title': 'First Post',
            'content': 'This is the first post'
        },
        {
            'title': 'Second Post',
            'content': 'This is the second post'
        }
    ]
    return render(request, 'single_pages/blog.html', {'title': 'Blog List', 'posts': post_list})