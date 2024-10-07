from .models import Category, Report, Photo


def category(request):
    categories = Category.objects.all()
    return {'categories': categories}


def report(request):
    report = Report.objects.all()
    return {'reports': report}


def photo(request):
    photos = Photo.objects.all()
    return {'photos': photos}
