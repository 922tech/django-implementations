
from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.urls import reverse
from djangoProject4.custome_module import slugify



class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='نام دسته')
    # is_delete = models.BooleanField(verbose_name='پاک شود؟')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'دسته'
        verbose_name_plural = 'دسته بندی های پست های وبلاگ'


class Tag(models.Model):
    tag = models.CharField(max_length=100)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE,related_name='weblog_tag')
    object_id = models.PositiveBigIntegerField()
    content_objects = GenericForeignKey('content_type','object_id')

    def __str__(self):
        return self.tag

    class Meta:
        indexes = [
            models.Index(fields=["content_type", "object_id"]),
        ]
 

class BlogFile(models.Model):
    files = models.FileField(upload_to='files', verbose_name='فایل', help_text='فایل هایی که میخواهید در پست وبلاگ قرار دهید را در اینجا اپلود کنید')
    url = models.CharField(max_length=1000, blank=True)

    def get_absolute_url(self):
        return reverse('view_file', args=[self.url])

    def save(self, *args, **kwargs):

        if not self.url:
            self.url = self.files.url
        print(self.url)
        return super().save(*args, **kwargs)

    def __str__(self):
        return "blog".join(self.files.url)

    class Meta:
        verbose_name = 'فایل'
        verbose_name_plural = 'فایل های وبلاگ'


class BlogImage(models.Model):
    image = models.ImageField(upload_to='images/blog', verbose_name='تصویر')
    url = models.CharField(max_length=300, blank=True)

    def __str__(self):
        return "blog"+self.image.url

    def save(self, *args, **kwargs):
        if not self.url:
            self.url = self.image.url

        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'تصویر'
        verbose_name_plural = 'تصاویر وبلاگ'


class Comment(models.Model):
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def get_related_posts(self):
        return self.post_set.all()
    


class Post(models.Model):
    title = models.CharField(max_length=300, verbose_name='عنوان')
    category = models.ForeignKey(to=Category, on_delete=models.SET_DEFAULT, default='عمومی', verbose_name='دسته بندی')
    slug = models.SlugField(unique=True, max_length=300, null=False, blank=True)
    writer = models.CharField(max_length=300, verbose_name='نویسنده')
    thumbnail = models.ImageField(upload_to='./images/blog/thumbnails', blank=True, null=True, default=None)
    date = models.DateTimeField(auto_now_add=True)
    content = RichTextField(verbose_name='محتوا')
    is_visible = models.BooleanField(default=True)
    tags = GenericRelation(Tag)
    views = models.IntegerField(verbose_name='تعداد بازدیدها', default=0, blank=True) 
    comment = models.ForeignKey(to=Comment, on_delete=models.CASCADE, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('view_post', args=[self.slug])

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'پست'
        verbose_name_plural = 'پست های وبلاگ'

