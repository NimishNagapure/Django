from django.db import models

# Create your models here.

class CheckList(models.Model):
    title = models.CharField(max_length=100)
    id_delete= models.BooleanField(default=False)
    is_archived  = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title



from django.db import models


class Status(models.TextChoices):
    UNPUBLISHED = "UN", "Unpublished"
    PUBLISHED = "PB", "Published"


class Book(models.Model):
    status = models.CharField(
        max_length=2,
        choices=Status.choices,
        default=Status.UNPUBLISHED,
    )

    # def __str__(self):
    #     return f"{self.id} - {Status(self.status).label}"       


class CheckListItem(models.Model):
    text = models.CharField(max_length=250)
    is_checked = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    checklist = models.ForeignKey(CheckList,on_delete=models.CASCADE)
    book = models.ForeignKey(Book,on_delete = models.DO_NOTHING,null=True)
    

    def __str__(self):
        return self.text