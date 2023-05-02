from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

from .models import Blog, HitCount, IpAddress,Tag, Post

def view_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    context = {'post': post}
    return render(request, 'postview.html', context)

def location_posts(request):
    location_tags = Tag.objects.filter(metatag='Location')
    location_posts = Post.objects.filter(tags__in=location_tags).distinct() # add the distinct() method
    context = {'location_posts': location_posts, 'title': 'Destinations'}
    return render(request, 'destinations.html', context)


def antiquities_post(request):
    location_tags = Tag.objects.filter(tag='Antique')
    location_posts = Post.objects.filter(tags__in=location_tags).distinct() # add the distinct() method
    context = {'location_posts': location_posts, 'title': 'Antiquities'}
    return render(request, 'destinations.html', context)


def posts(request):
    posts = Post.objects.all()
    context = {'location_posts': posts, 'title': 'Blogs'}
    return render(request, 'destinations.html', context)


def create_tag(request):
    if request.method == 'POST':
        tag = request.POST['tag']
        metatag = request.POST['metatag']
        Tag.objects.create(tag=tag, metatag=metatag)
        return redirect('home')

    return render(request, 'tagmaker.html')


def create_post(request):
    if request.method == 'POST':
        blurb = request.POST['blurb']
        body = request.POST['body']
        tag_ids = request.POST.getlist('tags')
        city = request.POST.get('city', '')
        country = request.POST.get('country', '')
        post = Post.objects.create(blurb=blurb, body=body)
        
        # Only add location tags if city and country are provided
        if city and country:
            location_tags = Tag.objects.filter(metatag='Location', tag__iexact=city, metatag__iexact=country)
            for tag in location_tags:
                post.tags.add(tag)
        
        for tag_id in tag_ids:
            tag = Tag.objects.get(pk=tag_id)
            post.tags.add(tag)
        return redirect('home')

    tags = Tag.objects.all()
    context = {'tags': tags}
    return render(request, 'postmaker.html', context)


def blog_list(request):
    Blog.objects.all().delete()
    b = Blog.objects.create(title='John', content="25")
    blogs = Blog.objects.all()
    return render(request, 'blog_list.html', {'blogs': blogs})

def sanctum(request):
    return render(request, 'sanctum.html')

def sanctumInner(request):
    return render(request, 'innerSanctum.html')

def home(request):
    return render(request, 'home.html')

def abt(request):
    return render(request, 'about.html')

def old(request):
    # Get the IP address of the user
    ip_address = request.META.get('REMOTE_ADDR')

    # Get the hit count object
    hit_count = HitCount.objects.first()

    # Try to get the IpAddress object for the user's IP
    ip_address_obj, created = IpAddress.objects.get_or_create(ip_address=ip_address)

    # Check if the IP address has been counted in the last minute
    if created or ip_address_obj.last_visited < timezone.now() - timezone.timedelta(hours=4):
        # Increment the hit count and update the timestamp
        hit_count.count += 1
        hit_count.last_updated = timezone.now()
        hit_count.save()

        # Update the last_visited timestamp for the IpAddress object
        ip_address_obj.last_visited = timezone.now()
        ip_address_obj.save()

        # Add the IpAddress object to the hit count's ip_addresses set
        hit_count.ip_addresses.add(ip_address_obj)

    # Render the template with the updated hit count
    return render(request, 'old.html', {'hit_count': hit_count.count})