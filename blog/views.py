from django.views.generic import CreateView,DetailView,DeleteView,UpdateView,ListView
from blog.models import BlogPost
from django.urls import reverse_lazy, reverse
from pytils.templatetags.pytils_translit import slugify




class BlogpostCreateView(CreateView):
    model = BlogPost
    fields = ('title', 'text', 'published', 'image')
    success_url = reverse_lazy('blog:list')

    def form_valid(self, form):
        if form.is_valid():
            new = form.save()
            new.slug = slugify(new.title)
            new.save()
        return super().form_valid(form)

class BlogpostUpdateView(UpdateView):
    model = BlogPost
    fields = ('title', 'text', 'published', 'image')
    # success_url = reverse_lazy('blog:list')

    def form_valid(self, form):
        if form.is_valid():
            new = form.save()
            new.slug = slugify(new.title)
            new.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('blog:post', args=[self.kwargs.get('pk')])


class BlogpostListView(ListView):
    model = BlogPost

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(published = True)
        return queryset

class BlogpostDetailView(DetailView):
    model = BlogPost

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.view_count += 1
        self.object.save()
        return self.object

class BlogpostDeleteView(DeleteView):
    model = BlogPost
    success_url = reverse_lazy('blog:list')