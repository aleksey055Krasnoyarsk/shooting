from django.db import models
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.


class Post(models.Model):
    autor = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = RichTextUploadingField(blank=True, default='')
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    class Meta:
        verbose_name = 'Новости'           


    def publish(self):
        self.published_date = timezone.now()
        self.save()


    def __str__(self):
        return self.title









class About_federation(models.Model):
    autor = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = RichTextUploadingField(blank=True, default='')
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    class Meta:
        verbose_name = 'О_федерации'           

    def publish(self):
        self.published_date = timezone.now()
        self.save()


    def __str__(self):
        return self.title





class Regions(models.Model):
    autor = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = RichTextUploadingField(blank=True, default='')
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    class Meta:
        verbose_name = 'Регионы'           


    def publish(self):
        self.published_date = timezone.now()
        self.save()


    def __str__(self):
        return self.title




class Referee(models.Model):
    autor = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = RichTextUploadingField(blank=True, default='')
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    class Meta:
        verbose_name = 'Судьи'           


    def publish(self):
        self.published_date = timezone.now()
        self.save()


    def __str__(self):
        return self.title







class Instructor(models.Model):
    autor = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = RichTextUploadingField(blank=True, default='')
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    class Meta:
        verbose_name = 'Инструкторы'           


    def publish(self):
        self.published_date = timezone.now()
        self.save()


    def __str__(self):
        return self.title






class Rukovodstvo(models.Model):
    autor = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = RichTextUploadingField(blank=True, default='')
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    class Meta:
        verbose_name = 'Руководство'           


    def publish(self):
        self.published_date = timezone.now()
        self.save()


    def __str__(self):
        return self.title






class Inst_korpus(models.Model):
    autor = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = RichTextUploadingField(blank=True, default='')
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    class Meta:
        verbose_name = 'Инструкторский корпус'           


    def publish(self):
        self.published_date = timezone.now()
        self.save()


    def __str__(self):
        return self.title







class Sud_corpus(models.Model):
    autor = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = RichTextUploadingField(blank=True, default='')
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    class Meta:
        verbose_name = 'Судейский корпус'           


    def publish(self):
        self.published_date = timezone.now()
        self.save()


    def __str__(self):
        return self.title





class Uch_corpus(models.Model):
    autor = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = RichTextUploadingField(blank=True, default='')
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    class Meta:
        verbose_name = 'Учебный корпус'           


    def publish(self):
        self.published_date = timezone.now()
        self.save()


    def __str__(self):
        return self.title





class In_federation(models.Model):
    autor = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = RichTextUploadingField(blank=True, default='')
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    class Meta:
        verbose_name = 'В_федерацию'           


    def publish(self):
        self.published_date = timezone.now()
        self.save()


    def __str__(self):
        return self.title




class Docx(models.Model):
    autor = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = RichTextUploadingField(blank=True, default='')
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    class Meta:
        verbose_name = 'Документы'           


    def publish(self):
        self.published_date = timezone.now()
        self.save()


    def __str__(self):
        return self.title








class Turnirs(models.Model):
    autor = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = RichTextUploadingField(blank=True, default='')
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    class Meta:
        verbose_name = 'Турниры'           


    def publish(self):
        self.published_date = timezone.now()
        self.save()


    def __str__(self):
        return self.title






class Turnirs_result(models.Model):
    autor = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = RichTextUploadingField(blank=True, default='')
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    class Meta:
        verbose_name = 'Результаты турниров'           


    def publish(self):
        self.published_date = timezone.now()
        self.save()


    def __str__(self):
        return self.title






class Articles(models.Model):
    autor = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = RichTextUploadingField(blank=True, default='')
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    class Meta:
        verbose_name = 'Статьи'           


    def publish(self):
        self.published_date = timezone.now()
        self.save()


    def __str__(self):
        return self.title








class Contacts(models.Model):
    autor = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = RichTextUploadingField(blank=True, default='')
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    class Meta:
        verbose_name = 'Контакты'           


    def publish(self):
        self.published_date = timezone.now()
        self.save()


    def __str__(self):
        return self.title





class Glavnaya(models.Model):
    autor = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = RichTextUploadingField(blank=True, default='')
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    class Meta:
        verbose_name = 'Главная страница'           


    def publish(self):
        self.published_date = timezone.now()
        self.save()


    def __str__(self):
        return self.title
