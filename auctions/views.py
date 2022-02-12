from xmlrpc.client import DateTime
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .forms import *
from .models import *
import urllib.request 



def index(request):
    return render(request, "auctions/index.html", {
        'listings': Listing.objects.all()
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")


def create(request):
    if request.method == "POST":
        newListingForm = newListing(request.POST)
        if newListingForm.is_valid:
            listing = newListingForm.save(commit=False)
            listing.creator = request.user
            listing.save()
            return render(request, "auctions/index.html", {
                'listings': Listing.objects.all()
            })
    else:
        newListingForm = newListing()
        return render(request, "auctions/create.html", {
            'newListingForm': newListingForm
        })


def watchlist(request):
    listings = request.user.watched_listings.all()
    if request.user.is_authenticated:
        for listing in listings:
            if request.user in listing.watcher.all():
                listing.is_watched = True
            else:
                listing.is_watched = False
    return render(request, "auctions/watchlist.html", {
        "listings": listings
    })

def alter_watchlist(request, listing_id):
    item = Listing.objects.get(id=listing_id)
    if request.user in item.watcher.all():
        item.watcher.remove(request.user)
    else:
        item.watcher.add(request.user)
    return listing(request, listing_id)

def listing(request, listing_id):
    listing = Listing.objects.get(id=listing_id)
    if request.user.is_authenticated:
        if request.user in listing.watcher.all():
            listing.is_watched = True
        else:
            listing.is_watched = False 
        return render(request, "auctions/listing.html", {
            "listing": listing,
            "commentForm": Comments(),
            "currentBid": BuyerBid()
        })
    else:
        return render(request, "auctions/listing.html", {
            "listing": listing,
            "commentForm": Comments(),
            "currentBid": BuyerBid()
        })

def comment(request, listing_id):
    listing = Listing.objects.get(id=listing_id)
    if request.method == "POST":
        commentary = Comments(request.POST)
        if commentary.is_valid:
            content = commentary.save(commit=False)
            content.user = request.user
            content.auction = listing
            content.save()
            return render(request, "auctions/listing.html", {
                "listing": listing,
                "commentForm": Comments(),
                "currentBid": BuyerBid()
            })
    else:
        return render(request, "auctions/listing.html", {
            "listing": Listing.objects.get(id=listing_id),
            "commentForm": Comments(),
            "currentBid": BuyerBid()
        })

def bid(request, listing_id):
    listing = Listing.objects.get(id=listing_id)
    offered_bid = float(request.POST['bid'])
    if offered_bid > listing.startingPrice and (listing.currentBid is None or offered_bid>listing.currentBid):
        form = BuyerBid(request.POST)
        buyer_bid = form.save(commit=False)
        buyer_bid.buyer = request.user
        buyer_bid.auction = listing
        buyer_bid.save()
        listing.currentBid = offered_bid
        listing.save()
        return render(request, "auctions/listing.html", {
            "listing": listing,
            "commentForm": Comments(),
            "currentBid": BuyerBid()
        })
    else: 
        message = "Your bid must be higher than the current bid or than the starting price"
        return render(request, "auctions/listing.html", {
            "listing": listing,
            "currentBid": BuyerBid(),
            "commentForm": Comments(),
            "message": message
        })

def close(request, listing_id):
    listing = Listing.objects.get(id=listing_id)
    if listing.isActive == True and request.user == listing.creator:
        listing.isActive = False
        try:
            buyer = Bid.objects.filter(auction=listing).last().buyer
            listing.buyer = buyer
            listing.save()
            return render(request, "auctions/listing.html", {
                "listing": listing,
                "commentForm": Comments(),
                "buyermessage": listing.buyer
            })
        except AttributeError:
            buyermessage = "No one set the bid. No buyers :("
            return render(request, "auctions/listing.html", {
                "listing": listing,
                "commentForm": Comments(),
                "buyermessage": buyermessage
            })
    else: 
        return render(request, "auctions/listing.html", {
            "listing": listing
        })

def categories(request):
    categories = Category.objects.all()
    listings = Listing.objects.all()
    if request.method == "POST":
        form = NewCategory(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return render(request, "auctions/categories.html", {
                "listings": listings,
                "categories": categories,
                'form': NewCategory()
            })
    else:
        return render(request, "auctions/categories.html", {
                "listings": listings,
                "categories": categories,
                'form': NewCategory()
        })

def category(request, category_id):
    category = Category.objects.get(id=category_id)
    listings = Listing.objects.filter(category=category)
    return render(request, "auctions/categories.html", {
            "listings": listings,
            "category": category,
            'form': NewCategory(),
            "categories": Category.objects.all()
    })
