from django.db import models
from django.contrib.auth.models import User






class Room(models.Model):
    name = models.CharField(max_length=64, unique=True, verbose_name='نام اتاق')
    slug = models.SlugField(unique=True, verbose_name='کد اتاق')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        super().__str__()
        return self.name
    
    class Meta:
        verbose_name = 'اتاق'
        verbose_name_plural = 'اتاق ها'
        





class Message(models.Model):
    room = models.ForeignKey(to=Room, on_delete=models.CASCADE, verbose_name='اتاق')
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, verbose_name='کاربر')
    value = models.TextField(max_length=1000, blank=True, null=True, verbose_name='مقدار')
    sent_at = models.DateTimeField(auto_now_add=True, blank=True, verbose_name='زمان ارسال پیام')
    
    def __str__(self) -> str:
        super().__str__()
        return str(self.user)
    
    class Meta:
        ordering = ['sent_at',]
        verbose_name = 'پیام'
        verbose_name_plural = 'پیام ها'