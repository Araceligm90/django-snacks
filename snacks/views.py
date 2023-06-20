from django.shortcuts import render
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["snacks"] = [
            {
                "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/91/Pizza-3007395.jpg/2560px-Pizza-3007395.jpg",
                "title": "Pizza",
                "description": "It is an Italian dish consisting of a usually round, flat base of leavened "
                               "wheat-based dough topped with tomatoes, cheese, and often various other ingredients, "
                               "which is then baked at a high temperature, traditionally in a wood-fired oven.",
                "reference_url": "https://en.wikipedia.org/wiki/Pizza"
            }, {
                "image_url": "https://upload.wikimedia.org/wikipedia/commons/4/47/Hamburger_%28black_bg%29.jpg",
                "title": "Hamburger",
                "description": "It is a food consisting of a patty of ground meat, placed inside a sliced bun.",
                "reference_url": "https://en.wikipedia.org/wiki/Hamburger"
            }, {
                "image_url": "https://upload.wikimedia.org/wikipedia/commons/0/09/Crepes_dsc07085.jpg",
                "title": "Crêpe",
                "description": "A very thin type of pancake often served with a wide variety of fillings such as "
                               "cheese, fruit, vegetables, meats, and a variety of spreads",
                "reference_url": "https://en.wikipedia.org/wiki/Cr%C3%AApe"
            },
        ]

        return context


class AboutView(TemplateView):
    template_name = 'about.html'
