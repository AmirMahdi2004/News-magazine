from django.db import models
from django.urls import reverse
from django_resized import ResizedImageField


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=25, verbose_name="نام")
    slug = models.SlugField(max_length=50, unique=True, verbose_name="اسلاگ")

    class Meta:
        ordering = ('name',)
        indexes = [
            models.Index(fields=['name'])
        ]
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها '

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('blog:category', args=[self.slug])


class Post(models.Model):
    category = models.ForeignKey(Category, related_name='posts', on_delete=models.CASCADE, blank=True, null=True,
                                 verbose_name="دسته بندی")
    title = models.CharField(max_length=150, verbose_name='عنوان')
    slug = models.SlugField(max_length=50, verbose_name='اسلاگ')
    content = models.TextField(verbose_name='محتوا')
    full_content = models.TextField(verbose_name='محتوا کامل ')
    created = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ساخت ')
    updated = models.DateTimeField(auto_now=True, verbose_name='تاریخ اپدیت')
    image = ResizedImageField(upload_to='media', verbose_name='تصویر', size=[500, 500])
    hot = models.BooleanField(default=False, verbose_name='تیتر خبر ها ')

    def get_absolute_url(self):
        return reverse('blog:article_detail', args=[self.id])

    class Meta:
        verbose_name = 'پست'
        verbose_name_plural = 'پست ها'

    def __str__(self):
        return self.title


class Note(models.Model):
    title = models.CharField(max_length=50, verbose_name='عنوان')
    note = models.TextField(verbose_name='متن')
    likes = models.IntegerField(default=0, verbose_name='لایک ها ')
    created = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ساخت ')
    updated = models.DateTimeField(auto_now=True, verbose_name='تاریخ اپدیت')

    def get_absolute_url(self):
        return reverse('blog:detail_note', args=[self.id])

    class Meta:
        verbose_name = 'یادداشت'
        verbose_name_plural = 'یادداشت ها'

    def __str__(self):
        return self.title


class Photo(models.Model):
    title = models.CharField(max_length=50, verbose_name='عنوان')
    image1 = ResizedImageField(upload_to='media', verbose_name='تصویر1', size=[500, 500])
    image2 = ResizedImageField(upload_to='media', verbose_name='تصویر2', size=[500, 500], blank=True, null=True)
    image3 = ResizedImageField(upload_to='media', verbose_name='تصویر3', size=[500, 500], blank=True, null=True)
    image4 = ResizedImageField(upload_to='media', verbose_name='تصویر4', size=[500, 500], blank=True, null=True)
    image5 = ResizedImageField(upload_to='media', verbose_name='تصویر5', size=[500, 500], blank=True, null=True)
    content = models.TextField(verbose_name='متن تصویر')
    created = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ساخت ')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'تصویری '
        verbose_name_plural = 'تصویری ها'

    def get_absolute_url(self):
        return reverse('blog:detail_photo', args=[self.id])


class Report(models.Model):
    title = models.CharField(max_length=50, verbose_name='عنوان')
    content = models.TextField(verbose_name='متن')
    created = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ساخت ')

    def get_absolute_url(self):
        return reverse('blog:report_detail', args=[self.id])

    class Meta:
        verbose_name = 'گزارش'
        verbose_name_plural = 'گزارش ها'

    def __str__(self):
        return self.title


class Resume(models.Model):
    title = models.CharField(max_length=50, verbose_name='عنوان')
    image1 = ResizedImageField(upload_to='media', verbose_name='تصویر1')
    image2 = ResizedImageField(upload_to='media', verbose_name='تصویر 2', blank=True, null=True)


class Video(models.Model):
    category = models.ForeignKey(Category, related_name='videos', on_delete=models.CASCADE, blank=True, null=True,
                                 verbose_name='دسته بندی ')
    title = models.CharField(max_length=250, verbose_name='عنوان')
    content = models.TextField(verbose_name='متن')
    created = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ساخت ')
    video = models.FileField(upload_to='media', verbose_name='فیلم')
    image = ResizedImageField(upload_to='media', verbose_name='تصویر', blank=True, null=True, )

    def get_absolute_url(self):
        return reverse('blog:video_detail', args=[self.id])

    class Meta:
        verbose_name = 'ویدیو'
        verbose_name_plural = 'ویدیو ها'

    def __str__(self):
        return self.title


class Advertising(models.Model):
    title = models.CharField(max_length=250, verbose_name='عنوان')
    video = models.FileField(upload_to='Advertising/%Y/%m/%d', verbose_name='تبلیغ')
    created = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ انتشار ')
    updated = models.DateTimeField(auto_now=True, verbose_name='تاریخ تمدید ')

    class Meta:
        verbose_name = 'تبلیغ'
        verbose_name_plural = 'تبلیغات'

    def __str__(self):
        return self.title


class Submitted(models.Model):
    sender = models.CharField(max_length=50, verbose_name='ارسال کننده')
    title = models.CharField(max_length=250, verbose_name='عنوان ')
    video = models.FileField(upload_to='Submitted', verbose_name='ویدیو', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ارسال', )
    image = models.ImageField(upload_to='Submitted', verbose_name='تصویر')
    content = models.TextField(verbose_name='محتوا')

    def get_absolute_url(self):
        return reverse('blog:submitted_detail', args=[self.id])

    class Meta:
        verbose_name = 'گفت گو'
        verbose_name_plural = 'گفت گو ها'

    def __str__(self):
        return self.title


class Comments(models.Model):
    sender = models.CharField(max_length=50, verbose_name='نویسنده')
    email = models.EmailField(max_length=254, verbose_name='ایمیل')
    content = models.TextField(verbose_name='کامنت')
    created = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ارسال')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments", verbose_name='پست', null=True,
                             blank=True)
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name="comments", verbose_name='ویدیو', null=True
                              , blank=True)
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE, related_name="comments", verbose_name='تصویری', null=True
                              , blank=True)
    allowed = models.BooleanField(default=False, verbose_name='مجوز')

    class Meta:
        verbose_name = 'کامنت'
        verbose_name_plural = 'کامنت ها'

    def __str__(self):
        return self.sender
