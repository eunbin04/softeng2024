from django.shortcuts import redirect, render
from django.views.generic import ListView, DetailView
from .models import Post, Category, Tag
from .forms import CommentForm

# Create your views here.
def category_posts(request, category_id):
    category =Category.objects.get(id=category_id)
    posts = Post.objects.filter(category=category)
    return render(request, 'blog/category_posts.html', {'category': category, 'posts':posts, 'categories': Category.objects.all()})

def tag_page(request, slug):
    tag = Tag.objects.get(slug=slug)
    post_list = tag.posts.all()
    post_count = tag.posts.count()

    return render(
        request,
        'blog/tag_page.html',
        {
            'tag': tag,
            'post_list': post_list,
            'post_count': post_count,
            'categories': Category.objects.all(),
            'no_category_post_count': Post.objects.filter(category=None).count(),
        }
    )

class PostList(ListView):
    model = Post
    ordering = '-pk'
    paginate_by = 5
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super(PostList, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


class PostDetail(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super(PostDetail, self).get_context_data(**kwargs)
        context['form'] = CommentForm()
        context['comments'] = self.object.comments.all()
        context['categories'] = Category.objects.all()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = self.object
            comment.save()
            return redirect(self.object.get_absolute_url())
        return self.get(request, *args, **kwargs)

