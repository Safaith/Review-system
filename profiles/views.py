from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from .forms import ProfileForm
from .models import UserProfile
from django.views.generic.edit import CreateView
from django.views.generic import ListView


# Create your views here
class CreateProfile(CreateView):
    template_name = "profiles/create_profile.html"
    model = UserProfile
    fields = "__all__"
    success_url = "/profiles"


class ProfileList(ListView):
    model = UserProfile
    template_name = "profiles/user_profile.html"
    context_object_name = "profiles"


# def store_files(file):
#     # wb+ mean incoming binary files stored in tempo directory (Incoming files in request.FILES)
#     with open("tempo/image.png", "wb+") as destination:
#         for chunk in file.chunks():
#             destination.write(chunk)


# class CreateProfileView(View):
#     def get(self, request):
#         form = ProfileForm()
#         return render(request, "profiles/create_profile.html", {"form": form})

#     def post(self, request):
#         submitted_files = ProfileForm(request.POST, request.FILES)

#         if submitted_files.is_valid():
#             # store_files(request.FILES['image'])
#             profile = UserProfile(image=request.FILES["user_image"])
#             profile.save()
#             return HttpResponseRedirect("/profiles")

#         return render(
#             request, "profiles/create_profile.html", {"form": submitted_files}
#         )
