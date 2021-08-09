from django.db import models

# Create your models here.

# Posts
class ModelLevel(models.Model):
    level = models.CharField(max_length=150, null=False, blank=False)
    
    def __str__(self):
        return self.level

class ModelPost(models.Model):
    title = models.CharField(max_length=150)
    level = models.ForeignKey(ModelLevel, on_delete=models.CASCADE)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return "Post {} created at {}".format(self.title, self.created)

    class Meta:
        pass

# 3x3 Algorithm
class ModelMethod(models.Model):
    method = models.CharField(max_length=150, null=False, blank=False)
    
    def __str__(self):
        return self.method

class ModelAlgorithm(models.Model):
    title = models.CharField(max_length=150)
    method = models.ForeignKey(ModelMethod, on_delete=models.CASCADE)
    content = models.TextField()
    youtube = models.CharField(max_length=150)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return "Post {} created at {}".format(self.title, self.created)

    class Meta:
        pass

# 3x3 Pattern
class ModelDifficulty(models.Model):
    difficulty = models.CharField(max_length=150, null=False, blank=False)
    
    def __str__(self):
        return self.difficulty

class ModelPattern(models.Model):
    title = models.CharField(max_length=150)
    difficulty = models.ForeignKey(ModelDifficulty, on_delete=models.CASCADE)
    content = models.TextField()
    image_url = models.CharField(max_length=150)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return "Post {} created at {}".format(self.title, self.created)

    class Meta:
        pass
