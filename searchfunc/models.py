from django.core.files.storage import default_storage as storage
from django.db import models
from .validators import validate_file_extension
from django.contrib.auth.models import AbstractUser


# create User here
class User(AbstractUser):
    is_organised = models.BooleanField(default=False)
    is_agent = models.BooleanField(default=False)


# Extending User Model Using a One-To-One Link
class Profile(models.Model):
    user = models.OneToOneField(User, blank=True, on_delete=models.CASCADE)

    avatar = models.ImageField(default='static/img/read-book2.jpg')
    bio = models.TextField()

    def save(self, *args, **kwargs):
        super().save()

    def __str__(self):
        return self.user.username


# first page slider model
class SliderImagesContent(models.Model):

    class Meta:
        verbose_name = 'Slider Content'
        verbose_name = 'Slider Content'

    slider_img = models.ImageField(upload_to="images")
    slider_header_content = models.CharField(max_length=100)
    slider_text_content = models.TextField(max_length=400)

    def __str__(self):
        return str(self.slider_header_content)


# create who we are page
class WhoWeAreModel(models.Model):

    class Meta:
        verbose_name = 'Who we are'
        verbose_name_plural = 'Who we are page'

    left_image = models.ImageField()
    right_content_text = models.TextField(max_length=700)
    right_content_1 = models.CharField(max_length=60)
    right_content_2 = models.CharField(max_length=60)
    right_content_3 = models.CharField(max_length=60)

    def __str__(self):
        return self.right_content_2


# what i do page model here
class EssentialsPageModel(models.Model):

    class Meta:
        verbose_name = 'Essential'
        verbose_name_plural = 'Essentials'

    essential_header_text = models.CharField(max_length=200)
    esential_paragraph = models.TextField(max_length=700)
    essential_page_image = models.FileField(
        validators=[validate_file_extension])

    def __str__(self):
        return self.essential_header_text


# create essentials right content here
class EssentialRightContent(models.Model):

    class Meta:
        verbose_name = 'Essential Right'
        verbose_name_plural = 'Essential Right'

    essential_right_image = models.ImageField()
    essentials_right_content = models.CharField(max_length=100)

    def __str__(self):
        return self.essentials_right_content


# create count model here
class CountPageModel(models.Model):

    class Meta:
        verbose_name = 'Count Page'
        verbose_name_plural = 'Count Page'

    count_img = models.FileField(validators=[validate_file_extension])
    count_number = models.IntegerField()
    count_text = models.CharField(max_length=100)

    def __str__(self):
        return self.count_text


# create books to know page
class BooksToRead(models.Model):

    class Meta:
        verbose_name = 'Book to read'
        verbose_name_plural = 'Books to read'

    book_name = models.CharField(max_length=100)
    book_subititle = models.CharField(max_length=70)
    book_cover_image = models.ImageField()

    def __str__(self):
        return self.book_name


# create book card class
class BookCardsModel(models.Model):

    class Meta:
        verbose_name = 'Card Books'
        verbose_name_plural = 'Card Books'

    book_cover = models.ImageField()
    book_name = models.CharField(max_length=100)
    book_subtitle = models.CharField(max_length=100)
    book_description = models.TextField(max_length=300)
    full_description = models.TextField(max_length=700)
    # shop details
    shop_details_description = models.TextField(max_length=700, blank=True)
    shop_cost = models.IntegerField(default=1, blank=True)
    # category model with foreignkey
    category = models.ForeignKey('BookCategoryModel',
                                 on_delete=models.CASCADE,
                                 null=True,
                                 blank=True)

    def __str__(self):
        return str(self.book_name)


# create contact me part here
class ContactMePartContext(models.Model):

    class Meta:
        verbose_name = 'Contact context'
        verbose_name = 'Contact me Context'

    contact_header = models.CharField(max_length=60)
    contact_text = models.TextField(max_length=300)

    def __str__(self):
        return self.contact_header


# book category model
class BookCategoryModel(models.Model):

    class Meta:
        verbose_name = 'Book Category'
        verbose_name_plural = 'Book Category'

    name = models.CharField(max_length=90, null=True, blank=True)

    def __str__(self):
        return self.name


# create user here model
class UserModel(models.Model):

    class Meta:
        verbose_name = 'Users Online'
        verbose_name_plural = 'Users Model'

    name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    age = models.IntegerField(default=0)
    email = models.EmailField()
    organiser = models.ForeignKey(Profile, on_delete=models.CASCADE)
    agent = models.ForeignKey("Agent", null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name

# create agent model
class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    organiser = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user)