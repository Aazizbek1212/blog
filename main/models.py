from django.db import models



class Category(models.Model):
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name


class Post(models.Model):
    created_at = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=200)
    body = models.TextField()
    image = models.ImageField(upload_to='blog/')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    editors_pick = models.BooleanField(default=False)
    trending = models.BooleanField(default=False)
    hit_count = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return self.title