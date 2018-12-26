from django import forms

# our new form
class ContactForm(forms.Form):
    contact_name = forms.CharField(required=True)
    contact_email = forms.EmailField(required=True)
    content = forms.CharField(
        required=True,
        widget=forms.Textarea
    )





from django import forms

from .models import Customer

class PostForm(forms.Form):

    class Meta:
        model = Customer
        fields = ('first_name', 'last_name',)


'''
from django import forms

#from .models import Customer

class NameForm(forms.Form):

    class Meta:
#        model = Customer
#        fields = ('last_name', 'first_name',)
        your_name = forms.CharField(label='Your name', max_length=100)
'''

