from django.shortcuts import redirect, render, get_object_or_404
from django.core.paginator import Paginator
from django.utils.text import slugify
from django.contrib.auth.decorators import permission_required
from .models import Post
from .forms import CreatePostForm
from feeds.models import Source


def post_list(request):
    posts = Post.published.all()
    paginator = Paginator(posts, 5)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'blog/post/list.html', {'page_obj': page_obj})


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post,
                             status='published',
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)
    return render(request, 'blog/post/detail.html', {'post': post})


@permission_required('blog.can_publish_articles')
def create_post(request):
    if request.method == 'POST':
        form = CreatePostForm(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.slug = slugify(new_post.title)
            new_post.save()
            return redirect(new_post)
    else:
        form = CreatePostForm()

    return render(request, 'blog/post/create.html', {'form': form})


def episode_list(request):
    feed = Source.objects.get(name='One Stream in Bristol')
    episodes = feed.posts.all()
    return render(request, 'blog/podcast/list.html', {'episodes': episodes})
