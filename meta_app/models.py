from django.db import models

# class User(models.Model):
#     name = models.CharField(max_length=30)
#     email = models.EmailField(max_length=50)
    
#     def __str__(self):
#         return self.name + " : " + self.email

# #create two classes menu category and menu (foreign key "many to one")

# class MenuCategory(models.Model):
#     menu_category_name=models.CharField(max_length=20)

# class Menu(models.Model):
#     menu_item = models.CharField(max_length=20)
#     price = models.IntegerField(default=10)
#     category_id = models.ForeignKey(MenuCategory, on_delete=models.PROTECT, default=None)

# # if you want to create a drop-down from which the user should select a value for this field, set this parameter to a list of two-item tuples.
# # SEMESTE_CHOICES = (
# #     ("1","Civil"),
# #     ("2","Electrical"),
# #     ("3","Mechanical"),
# #     ("4","CompSci"),
# # )
# # class Student(models.Model):
# #     semester = models.CharField(max_length=20,choices=SEMESTE_CHOICES,default='1')
# #     #It can store a floating-point number. Its variant DecimalField stores a number with fixed digits in the fractional part.
# #     grade = models.DecimalField(max_digits=5,
# #                                 decimal_places=2)


# class Artist(models.Model):
#     name = models.CharField(max_length=20)

# class Album(models.Model):
#     artist = models.ForeignKey(Artist,on_delete=models.CASCADE) 

# class Sorng(models.Model):
#     artist = models.ForeignKey(Artist,on_delete=models.CASCADE)
#     album = models.ForeignKey(Album,on_delete=models.RESTRICT)

# class Logger(models.Model):
#     first_name = models.CharField(max_length=20)
#     last_name = models.CharField(max_length=20)
#     time_log = models.TimeField(help_text='Enter the exact time!')

# class Reservation(models.Model):
#     name = models.CharField(max_length=100,blank=True)
#     contact = models.CharField('Phone number',max_length=200)
#     time = models.TimeField()
#     count = models.IntegerField()
#     notes = models.CharField(max_length=300,blank=True)

class Reservation(models.Model):
    first_name = models.CharField(max_length=20, default='')
    last_name = models.CharField(max_length=20, default='')
    booking_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name