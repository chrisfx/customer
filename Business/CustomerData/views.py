from django.shortcuts import render

# Create your views here.


from CustomerData.models import Customer



def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
#   num_books = Book.objects.all().count()
#   num_instances = BookInstance.objects.all().count()
    
    # Available books (status = 'a')
#    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    
    # The 'all()' is implied by default.    
    num_Customer = Customer.objects.count()
    name_Customer = Customer.objects.values('first_name', 'last_name', 'street_name', 'city', 'state', 'Zip')
#    name_Customer = Customer.objects.all()


   
    context = {
#        'num_books': num_books,
#        'num_instances': num_instances,
#        'num_instances_available': num_instances_available,
        'num_Customer': num_Customer,
        'name_Customer': name_Customer,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

from django.views import generic

class CustomerListView(generic.ListView):
    model = Customer


class CustomerDetailView(generic.DetailView):
    model = Customer


from .forms import PostForm

def post_new(request):
    form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

# add 
from CustomerData.models import Customer

# add to your views
def contact(request):
    form_class = ContactForm

    return render(request, 'contact.html', {
        'form': form_class,
    })

'''
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import NameForm

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'name.html', {'form': form})
'''
