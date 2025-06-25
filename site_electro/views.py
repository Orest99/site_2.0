from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

from .models import Product, Category,ContactInfo,Photo,Review

def home(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    contact = ContactInfo.objects.all()
    photo = Product.objects.filter(category__name='Галерея')[:8]
    context = {'categories': categories,
               'products': products,
               'contact': contact,
               'photos': photo,
               'title': 'Ph - Фото тільки для вас'}
    return render(request, 'myapp/Home.html', context)
# def category_detail(request, id=None):
#     category = get_object_or_404(Category, id=id)
#     products = Product.objects.filter(category=category)
#     context = {
#         'title': f'Категорія: {category.name}',
#         'category': category,
#         'products': products,
#     }
#     return render(request, 'myapp/page.html', context=context)


def category_detail(request, id=None):
    category = get_object_or_404(Category, id=id)

    if category.name == 'Галерея':
        photos_in_gallery_category = Photo.objects.filter(category=category)
        context = {
            'title': f'Категорія: {category.name}',
            'category': category,
            'photos': photos_in_gallery_category, # Передаємо об'єкти Photo
        }
        return render(request, 'myapp/photo_g.html', context=context)
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {
        'title': product.nazva,
        'product': product,
    }
    return render(request, 'myapp/page.html', context=context)
def photos(request):
    all_photos = Photo.objects.all()
    context = {
        'photos': all_photos,
        'title': 'Всі фото'
    }
    return render(request, 'myapp/photo_g.html', context)

def buys(request):
    google_form_url = "https://docs.google.com/forms/d/e/1FAIpQLSfBPGdZRUCVvzzHlL-DR7lF-89FNDRDEZuWBu67dpGXIVS_lA/viewform?usp=preview"
    context = {
        'title': 'Оформлення замовлення',
        'google_form_url': google_form_url,
    }
    return render(request, "myapp/buy.html", context)


def reviews_page(request):
    all_reviews = Review.objects.all().order_by('-created_at')

    if request.method == 'POST':
        Review.objects.create(
            author_name=request.POST.get('author_name'),
            author_email=request.POST.get('author_email'),
            rating=request.POST.get('rating'),
            comment=request.POST.get('comment'),
            is_approved=True
        )
        messages.success(request, 'Відгук додано!')
        return redirect('reviews_page')

    context = {
        'reviews': all_reviews,
        'title': 'Відгуки'
    }
    return render(request, 'myapp/comment.html', context)