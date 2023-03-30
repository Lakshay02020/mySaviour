from django.db import models

class Year(models.Model):
    name = models.CharField(max_length = 50)
    number = models.IntegerField()
    image = models.ImageField(upload_to='academics/images', default="")
    
    def __str__(self):
        return self.name
    
class Branch(models.Model):
    name = models.CharField(max_length = 50)
    image = models.ImageField(upload_to='academics/images', default="")
    def __str__(self):
        return self.name
    
class Courses(models.Model):
    name = models.CharField(max_length = 50)
    year = models.ForeignKey(Year, on_delete = models.DO_NOTHING)
    branch = models.ForeignKey(Branch, on_delete = models.DO_NOTHING, related_name= "courses")

    def __str__(self):
        return f"{self.name} || {self.branch} || {self.year}"

class Document_type(models.Model) :
    name = models.CharField(max_length = 50)
    image = models.ImageField(upload_to='academics/images', default="")

    def __str__(self):
        return self.name  
    
class Documents(models.Model):
    name  =  models.CharField(max_length = 50)
    course = models.ForeignKey(Courses, on_delete = models.CASCADE, default = None)
    type  =  models.ForeignKey(Document_type, on_delete = models.DO_NOTHING)
    notes =  models.FileField(upload_to = 'academics/documents')

    def __str__(self):
        return self.name

class Wifi(models.Model):
    name  =  models.CharField(max_length = 50)
    password = models.CharField(max_length = 50)

    def __str__(self):
        return self.name
    
