from django.db import models

# first page slider model
class SliderImagesContent(models.Model):
    class Meta:
        verbose_name = 'Slider Content'
        verbose_name = 'Slider Content'
        
    slider_img = models.ImageField()
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
    category = models.ForeignKey('BookCategoryModel', on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return str(self.book_name)
    
# book category model
class BookCategoryModel(models.Model):
    class Meta:
        verbose_name = 'Book Category'
        verbose_name_plural = 'Book Category'
        
    name = models.CharField(max_length=90, null=True, blank=True)
    
    def __str__(self):
        return self.name