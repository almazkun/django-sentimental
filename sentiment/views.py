from django.views.generic import FormView
from django.contrib import messages

from sentiment.forms import SentimentForm

from sentiment.quotes import get_random_quote


class Home(FormView):
    form_class = SentimentForm
    template_name = "sentiment/home.html"
    success_url = "/"

    def form_valid(self, form):
        sentiment = form.save()
        messages.success(self.request, sentiment.msg, extra_tags=sentiment.tag)
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["quote"] = get_random_quote()
        return context
