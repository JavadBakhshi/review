from django import forms
import django
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from testi.form import ReviewForm
from django.views import View
from django.views.generic.base import TemplateView
from .models import Review
from django.views.generic import ListView,DetailView
from django.views.generic.edit import FormView
# Create your views here.
#django class base viewed
class ReviewView(FormView):
    form_class = ReviewForm
    template_name = "testi/review.html"
    success_url = "thank-you"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
   
    # def post(self,request):
    #     form = ReviewForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return HttpResponseRedirect("/thank-you") 
    #     return render(request,"testi/review.html",{
    #     "form":form
    #     })
class ThankView(TemplateView):
    template_name = "testi/thank.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["message"] = "This is work"
        return context
class ReviewListView(ListView):
    template_name = "testi/review_list.html"
    model = Review
    context_object_name = "reviews"

class SingleReviewView(ListView):
    template_name = "testi/single_review.html"
    model = Review
    context_object_name = "reviews"








    #def review(request):
    #if request.method =="POST":
        #form = ReviewForm(request.POST)

        #if form.is_valid():
            #form.save()
            ##review = Review(
              ##  user_name=form.cleaned_data["user_name"],
              # # review_text=form.cleaned_data["review_text"],
               ##review.save()    
            #return HttpResponseRedirect("/thank-you")    
    #else:
       # form = ReviewForm()
    #return render(request,"testi/review.html",{
        #"form":form
        #})
    

#def thank(request):
   # return render(request,"testi/thank.html")