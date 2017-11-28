# Create your views here.

from django.http import QueryDict, HttpResponse
from django.urls import reverse
from django.views import View
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormMixin

from blog.forms import SortingForm, CreateCommentForm
from blog.models import Post, Like, Comment


class PostListView(FormMixin, ListView):

    model = Post
    paginate_by = 5
    form_class = SortingForm

    def get_queryset(self):
        keyword = self.request.session.get('keyword')
        city = self.request.session.get('city')
        country = self.request.session.get('country')
        filter_kwargs = {}
        order_args = []
        if keyword:
            filter_kwargs['title__contains'] = keyword
        if city!='0':
            sign = '-' if city=='-1' else ''
            order_args.append(sign+'author__city')
        if country!='0':
            sign = '-' if country=='-1' else ''
            order_args.append(sign+'author__country')

        return self.model.objects.filter(**filter_kwargs).order_by(*order_args)

    def get_success_url(self):
        return reverse('postlist')

    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        form = self.get_form()
        form.fields['keyword'].initial = self.request.session.get('keyword')
        form.fields['city'].initial = self.request.session.get('city')
        form.fields['country'].initial = self.request.session.get('country')
        context['form'] = form
        return context

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            self.request.session['keyword'] = form.data['keyword']
            self.request.session['city'] = form.data['city']
            self.request.session['country'] = form.data['country']


            return self.form_valid(form)
        else:
            return self.form_invalid(form)

def likes_view(request):
    try:
        post_id= request.POST['post_id']
        post = Post.objects.get(pk=post_id)
    except:
        return HttpResponse('Post not found', status=404)

    like, created = Like.objects.get_or_create(post = post,user = request.user)

    if not created:
        like.delete()

    return HttpResponse(post.likes)


class  PostDetailsView(DetailView):
    model = Post

class PostCommentsView(FormMixin, ListView):
    model = Comment
    paginate_by = 5
    form_class = CreateCommentForm

    def get_queryset(self):
        return Comment.objects.filter(post_id=self.kwargs['pk']).order_by('-created_date')

    def get_success_url(self):
         return reverse('post_details', kwargs={'pk':self.kwargs['pk']})

    def get_context_data(self, **kwargs):
        context = super(PostCommentsView, self).get_context_data(**kwargs)
        context['post_id'] = self.kwargs['pk']
        return context

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            Comment.objects.create(
                user=self.request.user,
                post_id=self.kwargs['pk'],
                text=form.data.get('text')
            )
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
