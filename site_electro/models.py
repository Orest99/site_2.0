from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
class Category(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Назва')
    description = models.TextField(blank=True)
    photos = models.CharField(max_length=50, blank=True, null=True, verbose_name='Фото')
    contacts = models.CharField(max_length=50, blank=True, null=True, verbose_name='Контакти')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f"/category/{self.id}"
class Product(models.Model):
    nazva = models.CharField(max_length=100, unique=True, verbose_name='Назва')
    description = models.TextField(blank=True, null=True, verbose_name='Опис')
    image = models.ImageField(upload_to='products/', blank=True, null=True, help_text="", verbose_name='Зображення')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категорія', null=True, blank=True)
    def __str__(self):
        return self.nazva

    def get_absolute_url(self):
        return f"/products/{self.id}"
class ContactInfo(models.Model):
    phone = models.CharField(max_length=20, blank=True, null=True, verbose_name='Телефон')
    email = models.EmailField(blank=True, null=True, verbose_name='Email')
    telegram_link = models.URLField(blank=True, null=True, verbose_name='Посилання на Telegram(особисто)')
    telegram_group = models.URLField(blank=True, null=True, verbose_name='Посилання на Telegram(група)')
    def __str__(self):
        return 'Контактна інформація'
class Photo(Product):
    def get_absolute_url(self):
        return f"/products/photos/{self.id}"

class Review(models.Model):
    product = models.ForeignKey(
        'Product',
        on_delete=models.CASCADE,
        related_name='reviews',
        null=True,
        blank=True,
        verbose_name='Продукт'
    )
    author_name = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name='Ваше ім\'я'
    )
    author_email = models.EmailField(
        blank=True,
        null=True,
        verbose_name='Ваш Email'
    )
    rating = models.IntegerField(
        default=5,
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        verbose_name='Рейтинг (від 1 до 5)'
    )
    comment = models.TextField(
        verbose_name='Ваш відгук'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата створення'
    )
    # Змінено: автоматично схвалюється
    is_approved = models.BooleanField(
        default=True,
        verbose_name='Затверджено модератором'
    )

    class Meta:
        verbose_name = 'Відгук'
        verbose_name_plural = 'Відгуки'
        ordering = ['-created_at']

    def __str__(self):
        author_info = self.author_name if self.author_name else (self.author_email if self.author_email else 'Анонім')
        product_info = f' про {self.product.nazva}' if self.product else ''
        return f'Відгук від {author_info} ({self.rating} зірок){product_info}'
