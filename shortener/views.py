from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from .models import KirrURL
from .forms import SubmitUrlForm


class HomeView(View):
	def get(self, request, *args, **kwargs):
		the_form = SubmitUrlForm()
		context = {
			"title": "ShortenMe.com",
			"form": the_form,
		}
		return render(request, "url_shortner/home.html", context)

	def post(self, request, *args, **kwargs):
		the_form = SubmitUrlForm(request.POST)
		template = "url_shortner/home.html"
		context = {
			"form": the_form,
			"title": "ShortenMe.com"
		}
		if the_form.is_valid():
			new_url = the_form.cleaned_data.get("url")
			obj, created = KirrURL.objects.get_or_create(url = new_url)
			context = {
				'Object': obj,
				'Created': created,
			}
			if created:
				template = "url_shortner/success.html"
			else:
				template = "url_shortner/already-exists.html"
		
		return render(request, template , context)		



class UrlRedirectView(View):
   def get(self, request, shortcode=None, *args, **kwargs):
      obj = get_object_or_404(KirrURL, shortcode=shortcode)
      return HttpResponseRedirect(obj.url)
