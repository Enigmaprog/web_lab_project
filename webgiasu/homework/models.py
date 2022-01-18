from django.forms.widgets import DateInput
from basic_stt.views import report
from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
User = get_user_model()
import datetime
from django.utils import timezone
# Create your models here.

class subs_homework(models.Model):


    list_user = models.ManyToManyField(User, default=None, blank=True)


class homeworkpost(models.Model):
    title = models.CharField(max_length=30, blank= False)
    main_content = models.TextField(max_length=200, blank= False)
    subject = models.CharField(max_length=30, blank= False)
    calendar = models.CharField(max_length=30, blank= False)
    salary = models.CharField(max_length=30, blank= False)
    contact = models.CharField(max_length=100, blank=False)
    date_posted = models.DateTimeField(auto_now_add=True)
    date_outdate = models.PositiveSmallIntegerField(blank=False, default=15)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    report = models.ManyToManyField(User, default=None, blank=True, related_name='homework_report_set')
    post_img1 = models.ImageField(_("Ảnh 1:"), upload_to='postImg/homework/', null=True, blank=True)
    post_img2 = models.ImageField(_("Ảnh 2:"), upload_to='postImg/homework/', null=True, blank=True)
    post_file = models.FileField(_("File:"), upload_to='postFile/homework/', null=True, blank=True)
    

    def __str__(self):
        return self.title
    @property
    def num_report(self):
        return self.report.all().count()
    @property
    def is_expired(self):
        return timezone.now() > (self.date_posted + datetime.timedelta(days=self.date_outdate))
