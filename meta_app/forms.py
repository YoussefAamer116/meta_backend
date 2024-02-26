from django import forms
# class NameForm(forms.Form):
#     your_name = forms.CharField(label='Your name',max_length=100)

# class UserForm(ModelForm):
#     class Meta:
#         model = Booking
#         fields = "__all__"

# from django import forms
# class MyForm(forms.Form):
#     name = forms.CharField()
#     age = forms.IntegerField()

# from django import forms
# class DemoForm(forms.Form):
#     email = forms.EmailField(label='Enter your Email')

# from django.forms.widgets import NumberInput
# class DemoForm(forms.Form):
#     reservation_date = forms.DateField(widget=NumberInput(attrs={'type':'date'}))
# FAVORITE_DISH = [
#     ('italian','Italian'),
#     ('greek','Greek'),
#     ('turkish','Turkish'),
# ]
# class DemoForm(forms.Form):
#     favorite_dish = forms.ChoiceField(widget=forms.RadioSelect,choices=FAVORITE_DISH)

# class ApplicationForm(forms.Form):
#     name = forms.CharField(label='name of applicant',max_length=20)
#     address = forms.CharField(label='address',max_length=50)
#     posts = (('manager','Manager'),('cashier','Cashier'),('operator','Operator'))
#     field = forms.ChoiceField(choices=posts)

# SHIFTS = (
#     ("1","Morning"),
#     ("2","Aftrenoon"),
#     ("3","Evening"),
# )
# class InputForm(forms.Form):
#     first_name = forms.CharField(max_length=20,required=False)
#     last_name = forms.CharField(max_length=20)
#     shift = forms.ChoiceField(choices=SHIFTS)
#     time_log = forms.TimeField()


# from myapp.models import Reservation
# class ReservationForm(ModelForm):
#         class meta:
#                 model = Reservation
#                 fields = ['name','seats','content','reporter']

# form = ReservationForm()

# from django.forms import ModelForm
# from .models import Logger
# class LogForm(ModelForm):
#     class Meta:
#             model = Logger
#             fields = '__all__'