from django.contrib import admin
from .models import *

# import book models
admin.site.register(BookCardsModel)
admin.site.register(BookCategoryModel)
# import slider models
admin.site.register(SliderImagesContent)
