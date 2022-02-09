from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.deletion import CASCADE, PROTECT
from django.utils import timezone
import urllib.request 

class User(AbstractUser):
    pass

class Category(models.Model):
    category = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.category}"

class Listing(models.Model):
    name = models.CharField(max_length=80)
    category = models.ForeignKey(Category, on_delete=CASCADE, blank=True, related_name="belongs_to")
    imageURL = models.URLField(blank=True,null=True, default="https://upload.wikimedia.org/wikipedia/commons/thumb/6/65/No-Image-Placeholder.svg/1665px-No-Image-Placeholder.svg.png")
    startingPrice = models.FloatField(max_length=10)
    currentBid = models.FloatField(null=True, blank=True)
    description = models.TextField(max_length=300)
    buyer = models.ForeignKey(User, on_delete=PROTECT, null=True, blank=True)
    creator = models.ForeignKey(User, on_delete=models.PROTECT, null=True, related_name="all_creators")
    watcher = models.ManyToManyField(User, blank=True, related_name="watched_listings")
    created = models.DateTimeField(default=timezone.now())
    isActive = models.BooleanField(default=True)

    def get_picture(Self):
        if Self.imageURL:
            urllib.request.urlretrieve(Self.imageURL, 'auctions/static/media/img1.jpg')
            Self.save()

    def __str__(self):
        return f"{self.name} - {self.category} - {self.startingPrice}"


class Bid(models.Model):
    bid = models.FloatField(max_length=10)
    buyer = models.ForeignKey(User, on_delete=CASCADE, null=True)
    auction = models.ForeignKey(Listing, on_delete=CASCADE, null=True, related_name="listing_bids")

class Comment(models.Model):
    comment = models.TextField(max_length=300)
    user = models.ForeignKey(User, on_delete=CASCADE, null=True)
    auction = models.ForeignKey(Listing, on_delete=CASCADE, null=True, related_name="listing_comment")
    created = models.DateTimeField(default=timezone.now())