from django.contrib import admin
from .models import ModelLevel, ModelPost, ModelMethod, ModelAlgorithm, ModelDifficulty, ModelPattern

# Register your models here.
admin.site.register(ModelLevel)
admin.site.register(ModelPost)

admin.site.register(ModelMethod)
admin.site.register(ModelAlgorithm)

admin.site.register(ModelDifficulty)
admin.site.register(ModelPattern)
