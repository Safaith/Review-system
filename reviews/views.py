from typing import Any, Dict
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import reviewForm
from .models import Review
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView

# Create your views here.


class review(CreateView):
    model = Review
    form_class = reviewForm
    template_name = "reviews/review.html"
    success_url = "/thank-you"
    # form_class = reviewForm
    # template_name = "reviews/review.html"
    # success_url = "/thank-you"

    # def form_valid(self, form):
    #     form.save( )
    #     return super().form_valid(form)
    # --------------------------------------------------
    # def get(self, request):
    #     form = reviewForm()

    #     return render(request, "reviews/review.html", {
    #         "form": form
    #     })

    # def post(self, request):
    #     if request.method == 'POST':
    #         existing_data = Review.objects.get(pk=1)   # for updatting DATA
    #         form = reviewForm(request.POST, instance=existing_data)

    #         if form.is_valid():
    #             form.save()
    #         # reviews = Review(
    #         #     user_name=form.cleaned_data['user_name'],
    #         #     review_text=form.cleaned_data['review_text'],
    #         #     rating=form.cleaned_data['rating'])
    #         # reviews.save()
    #             return redirect("thank")


class Thank_you(TemplateView):
    template_name = "reviews/thank_you.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["message"] = "This works!"
        return context


# class ReviewList(TemplateView):
#     template_name = "reviews/review_list.html"


#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         reviews = Review.objects.all()
#         context["reviews"] = reviews
#         return context
class ReviewList(ListView):
    template_name = "reviews/review_list.html"

    model = Review
    context_object_name = "reviews"  # cause it uses as (object_list)

    # def get_queryset(self):
    #     base_query = super().get_queryset()
    #     data = base_query.filter(rating__gt=2)
    #     return data


class Detail_page(DetailView):
    template_name = "reviews/detail_page.html"

    model = Review
    context_object_name = "review"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        loaded_review = self.object
        request = self.request
        fav_id = request.session.get("favourite_review")
        context["is_favourite"] = fav_id == str(loaded_review.id)
        return context


class AddFavouriteView(View):
    def post(self, request):
        review_id = request.POST["review_id"]
        # fav_review = Review.objects.get(pk=review_id)
        # request.session["favourite_review"] = review_id
        return HttpResponseRedirect("/reviews/" + review_id)
