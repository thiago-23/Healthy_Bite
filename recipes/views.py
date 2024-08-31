from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View
from django.urls import reverse_lazy, reverse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Recipe, Bookmark
from .forms import CommentForm, RecipeForm
from django.template.defaultfilters import slugify

# Create your views here.

class RecipeList(generic.ListView):
    model = Recipe
    queryset = Recipe.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6

class RecipeDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Recipe.objects.filter(status=1)
        recipe = get_object_or_404(queryset, slug=slug)
        comments = recipe.comments.filter(approved=True).order_by('created_on')

        # Check if the recipe is marked as a favourite by the current user
        favourite = False
        if request.user.is_authenticated:
            favourite = Bookmark.objects.filter(user=request.user, recipe=recipe).exists()

        return render(
            request,
            "recipe_detail.html",
            {
                "recipe": recipe,
                "comments": comments,
                "commented": False,
                "favourite": favourite,
                "comment_form": CommentForm()
            }
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Recipe.objects.filter(status=1)
        recipe = get_object_or_404(queryset, slug=slug)
        comments = recipe.comments.filter(approved=True).order_by('created_on')

        # Check if the recipe is marked as a favourite by the current user
        favourite = False
        if request.user.is_authenticated:
            favourite = Bookmark.objects.filter(user=request.user, recipe=recipe).exists()

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.recipe = recipe
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "recipe_detail.html",
            {
                "recipe": recipe,
                "comments": comments,
                "commented": True,
                "favourite": favourite,
                "comment_form": CommentForm()
            }
        )

@method_decorator(login_required, name='dispatch')
class RecipeCreate(generic.CreateView):
    model = Recipe
    form_class = RecipeForm
    template_name = 'recipe_create.html'

    def get_success_url(self):
        return reverse('recipe_detail', kwargs={'slug': self.object.slug})

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.slug = slugify(form.instance.title)
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class RecipeEdit(generic.UpdateView):
    model = Recipe
    form_class = RecipeForm
    template_name = 'recipe_edit.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class RecipeDelete(generic.DeleteView):
    model = Recipe
    template_name = 'recipe_delete.html'
    success_url = reverse_lazy('home')

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(author=self.request.user)

@login_required
def toggle_favourite(request, slug):
    recipe = get_object_or_404(Recipe, slug=slug)
    bookmark, created = Bookmark.objects.get_or_create(user=request.user, recipe=recipe)

    if not created:
        bookmark.delete()

    return redirect('recipe_detail', slug=slug)

@login_required
def like_recipe(request, id):
    recipe = get_object_or_404(Recipe, id=id)
    if recipe.likes.filter(id=request.user.id).exists():
        recipe.likes.remove(request.user)
    else:
        recipe.likes.add(request.user)
    return redirect('recipe_detail', slug=recipe.slug)