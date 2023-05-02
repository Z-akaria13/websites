from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()


class IpAddress(models.Model):
    ip_address = models.CharField(max_length=255, unique=True)
    last_visited = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'IP address: {self.ip_address}, last visited: {self.last_visited}'


class HitCount(models.Model):
    count = models.IntegerField(default=0)
    ip_addresses = models.ManyToManyField(IpAddress)
    last_updated = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'Hit count: {self.count}, last updated: {self.last_updated}'
    
class Tag(models.Model):
    tag = models.CharField(max_length=50)
    metatag = models.CharField(max_length=50)

    def __str__(self):
        return self.tag

class Post(models.Model):
    blurb = models.TextField()
    body = models.TextField()
    date_made = models.DateField(auto_now_add=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.blurb