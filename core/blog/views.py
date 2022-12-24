from django.shortcuts import render
from django.views.generic.base import TemplateView , RedirectView
from django.views.generic import ListView , DetailView , FormView
from .models import Post
from .forms import ContactForm


# Create your views here.

# fbv for templateview
# def indexView(request):
#     """
#     function base view to show index page
#     """
#     return render(request,'index.html',{'type':'fbv'})

class CbvView(TemplateView):
    """
    class base view to show page
    """
    template_name = 'index.html'
    extra_context = {'type':'cbv','posts':Post.objects.all()}

class RedirectToGoogle(RedirectView):
    url='https://www.google.com'
    #permanent = False #it is False by default

class PostListView(ListView):
    model = Post 
    paginate_by =  1
    ordering = '-id'

    # def get_queryset(self):
    #     return super().get_queryset()

class PostDetailView(DetailView):
    model = Post
    context_object_name = 'object'
    pk_url_kwarg = 'test'

class PostFormView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = '/blog/cbv-listview/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.save()
        return super().form_valid(form)