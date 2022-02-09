from django import forms
from django.contrib.auth import models
from django.forms import fields
from django.forms.models import ModelForm
from .models import Category, Listing, Bid, Comment

class newListing(forms.ModelForm):
    class Meta:
        model = Listing
        fields = ["name", "startingPrice", "description", "category", "imageURL"]

class BuyerBid(forms.ModelForm):
    class Meta:
        model = Bid
        fields = ["bid"]

class Comments(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["comment"]
        widgets = {
            'comment': forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Leave your comment here',
            })
        }

class NewCategory(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["category"]
        widgets = {
            'category': forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Your category',
            })
        }