from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import *
from .forms import CommentForm, SearchForm, Comments
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.

def paginate(request, queryset, page):
    paginator = Paginator(queryset, page)
    page_number = request.GET.get('page', 1)
    try:
        posts = paginator.page(page_number)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    except PageNotAnInteger:
        posts = paginator.page(1)

    return posts


def comments(request, pk, ppv, sr):
    show = ppv.comments.filter(allowed=True).order_by('-created')
    form = CommentForm(data=request.POST)
    comment = None
    if form.is_valid():
        comment = form.save(commit=False)
        if 'post' == sr:
            comment.post = ppv
        elif 'video' == sr:
            comment.video = ppv
        elif 'photo' == sr:
            comment.photo = ppv
        comment.save()
    context = [comment, form, ppv, show]
    return context


def index(request):
    categories = Category.objects.all()
    note = Note.objects.all()
    photos = Photo.objects.all()
    comment = Comments.objects.all()
    post = Post.objects.all()
    view_up = post.filter(created__lte=timezone.now())
    view_dey = view_up.last()
    hot = post.filter(hot=True).all()
    reports = Report.objects.all()
    video = Video.objects.all().order_by('-created')
    video2 = video[:2]
    advertising = Advertising.objects.all()
    submitted = Submitted.objects.all()
    context = {
        'photos': photos[:3],
        'categories': categories,
        'notes': note[:5],
        'comments': comment,
        'posts': post[:6],
        'hots': hot[:3],
        'report': reports[:5],
        'view_day': view_dey,
        'view_up': view_up[:3],
        'video': video,
        'video2': video2,
        'advertising': advertising[:2],
        'submitted': submitted[:4]

    }
    return render(request, 'blog/index.html', context)


def article(request):
    posts = Post.objects.all()
    posts = paginate(request, posts, 12)
    context = {
        'posts': posts,
        'category': category,

    }
    return render(request, 'blog/article.html', context)


def article_detail(request, pk):
    post = Post.objects.get(pk=pk)
    comment = comments(request, pk, post, 'post')
    context = {
        'comment': comment[0],
        'form': comment[1],
        'post': comment[2],
        'show': comment[3],
    }
    return render(request, 'blog/detail.html', context)


def search(request):
    if 'query' in request.GET:
        query = request
        form = SearchForm(data=request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = Post.objects.all().filter(title=query)
            results = paginate(request, results, 12)
    context = {
        'query': query,
        'results': results,
    }
    return render(request, 'blog/search.html', context)


def category(request, slug=None):
    category = None
    categories = Category.objects.all()
    posts = Post.objects.all()

    if slug:
        category = get_object_or_404(Category, slug=slug)
        posts = posts.filter(category=category)
        posts = paginate(request, posts, 12)

    context = {
        'category': category,
        'categories': categories,
        'posts': posts,
    }
    return render(request, 'blog/category.html', context)


def about(request):
    resume = Resume.objects.all()
    context = {
        'resume': resume
    }
    return render(request, 'blog/about.html', context)


def contact_us(request):
    return render(request, 'blog/contact_us.html', )


def list_note(request):
    notes = Note.objects.all()
    notes = paginate(request, notes, 12)
    context = {
        'notes': notes
    }
    return render(request, 'blog/note_list.html', context)


def detail_note(request, pk):
    note = get_object_or_404(Note, pk=pk)
    context = {
        'notes': note
    }
    return render(request, 'blog/detail_note.html', context)


def photo_list(request):
    photos = Photo.objects.all()
    photos = paginate(request, photos, 12)
    context = {
        'photos': photos,
    }
    return render(request, 'blog/photo_list.html', context)


def detail_photo(request, pk):
    photo = Photo.objects.get(pk=pk)
    comment = comments(request, pk, photo, 'photo')
    context = {
        'comment': comment[0],
        'form': comment[1],
        'photo': comment[2],
        'show': comment[3],
    }
    return render(request, 'blog/detail_photo.html', context)


def report_list(request):
    reports = Report.objects.all()
    reports = paginate(request, reports, 12)
    context = {
        'reports': reports
    }

    return render(request, 'blog/report_list.html', context)


def report(request, pk):
    report = get_object_or_404(Report, pk=pk)
    return render(request, 'blog/report_detail.html', {'report': report})


def video_list(request):
    videos = Video.objects.all()
    videos = paginate(request, videos, 12)
    context = {
        'videos': videos,
    }
    return render(request, 'blog/video_list.html', context)


def video_detail(request, pk):
    video = Video.objects.get(pk=pk)
    comment = comments(request, pk, video, 'video')
    context = {
        'comment': comment[0],
        'form': comment[1],
        'video': comment[2],
        'show': comment[3],
    }
    return render(request, 'blog/video_detail.html', context)


def submitted_list(request):
    submitted = Submitted.objects.all()
    submitted = paginate(request, submitted, 12)
    context = {
        'submitted': submitted
    }
    return render(request, 'blog/submitted_list.html', context)


def submitted_detail(request, pk):
    submitted = get_object_or_404(Submitted, pk=pk)
    context = {
        'submitted': submitted
    }
    return render(request, 'blog/submitted_detail.html', context)


def not_found(request, exception):
    return render(request, 'blog/404.html')

