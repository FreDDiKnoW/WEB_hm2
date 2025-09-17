from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Place(models.Model):
    PLACE_TYPES = [
        ('restaurant', 'Ресторан'),
        ('cafe', 'Кафе'),
        ('park', 'Парк'),
        ('museum', 'Музей'),
        ('cinema', 'Кінотеатр'),
        ('other', 'Інше'),
    ]

    name = models.CharField('name', max_length=200)
    description = models.TextField()
    place_type = models.CharField(max_length=20, choices=PLACE_TYPES)
    location = models.CharField(max_length=200, blank=True, null=True)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    image = models.ImageField(upload_to='places/', blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_place_type_display_custom(self):
        return dict(self.PLACE_TYPES)[self.place_type]