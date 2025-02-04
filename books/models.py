from django.db import models

# Create your models here.


class Book(models.Model):
    booktitle = models.CharField(max_length = 50)
    bookdetail = models.CharField(max_length= 300)
    bookauthor = models.CharField(max_length= 50)
    bookimage= models.ImageField(upload_to='book_images/')
    bookpath = models.FileField(upload_to='book_path/')

    def __str__(self):
        return self.booktitle
        return self.bookdetail
        return self.bookauthor

