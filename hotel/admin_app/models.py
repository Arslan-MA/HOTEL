from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import Sum
from django.db.models.signals import post_save
from django.template.defaultfilters import slugify
from django.urls import reverse


class Client(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.first_name} - {self.last_name}"


class Comment(models.Model):
    author = models.ForeignKey(Client, on_delete=models.CASCADE)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author} - {self.date}"


class Room(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    image = models.ImageField(max_length=255, upload_to='images/')

    CHOICE_TYPE = [
        ('Cheap', 'Cheap'),
        ('Comfortable', 'Comfortable'),
        ('V.I.P.', 'V.I.P.')
    ]

    type = models.CharField(max_length=255, choices=CHOICE_TYPE)
    reserved = models.BooleanField(default=False)
    is_hidden = models.BooleanField(default=False)
    comment = models.ForeignKey(Comment,
                                blank=True,
                                null=True,
                                on_delete=models.SET_NULL)
    likes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.title} - {self.type}"

    def save(self, *args, **kwargs):
        if self.title:
            self.slug = slugify(self.title)
        super(Room, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('slug_room', args=[self.slug])


class Service(models.Model):
    title = models.CharField(max_length=255)
    price = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.title} - {self.price}"


class BookApplication(models.Model):
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE)
    room_id = models.OneToOneField(Room, on_delete=models.CASCADE)
    number_persons = models.IntegerField()
    services = models.ManyToManyField(Service, blank=True)
    start_book = models.DateField()
    end_book = models.DateField()
    total_price = models.PositiveIntegerField(default=0)
    approve_status = models.BooleanField(null=True)

    def __str__(self):
        return f"{self.end_book} {self.total_price} - {self.approve_status}"

    def calculate_total_price(self):
        total = 0
        for service in self.services.all():
            total += service.price
        self.total_price = total
        self.save()

    def get_absolute_url(self):
        return reverse('slug_book_application', args=[self.pk])
