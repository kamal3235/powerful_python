import abc
import json


class WebApp:
    def __init__(self):
        self._routes = {}     # initiated dictionary

    def add_route(self, url, view):
        self._routes[url] = view

    def get(self, url):
        view = self._routes[url]
        return view.render()

    def urls(self):
        return sorted(self._routes.keys())



class View(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def render(self):
        pass


class HTMLView(View):
    body = ''

    def render(self):
        return '<html><body>' + self.body + '</body></html>'


class ShoutingHTMLView(HTMLView):

    def render(self):
        return super().render().upper()


class LegalView(HTMLView):
    pass


# class ContactView(HTMLView):
#     body = "Get in touch at hello@example.com"
#     view = '{"calories": 25, "fat": 0.1, "protein": 0.6, "serving_size": 61}'
#     pass


class JSONView(View):

    @abc.abstractmethod
    def data(self):
        pass

    def render(self):
        return json.dumps(self.data(), sort_keys=True)


class HomePageView(HTMLView):
    body = 'Welcome!'


class AboutPageView(HTMLView):
    body = 'This is a simple website about nutrition.'


# class CarrotInfoView(JSONView):
#     def data(self):
#         return {
#             'serving_size': 61,
#             'fat': 0.1,
#             'calories': 25,
#             'protein': 0.6,
#         }


class ChickenInfoView(JSONView):
    def data(self):
        return {
            'serving_size': 140,
            'fat': 5,
            'calories': 231,
            'protein': 43,
        }


class TomatoInfoView(JSONView):
    def data(self):
        return {
            'serving_size': 123,
            'fat': 0.2,
            'calories': 22,
            'protein': 1.1,
        }



home_view = HomePageView()
print(home_view.render())
print(home_view.body)
about_view = AboutPageView()
print(about_view.render())
app = WebApp()
print(type(app._routes))
app.add_route("/", home_view)
app.add_route("/about/", about_view)
print(app.get("/"))

print(app.get("/about/"))
class ContactView(HTMLView):
    body = 'Get in touch at hello@example.com'

app.add_route("/contact/", ContactView())
print(app.get("/contact/"))
class CarrotInfoView(JSONView):
    def data(self):
        return {
        'serving_size': 61,
        'fat': 0.1,
        'calories': 25,
        'protein': 0.6,
    }

carrot_view = CarrotInfoView()
print(carrot_view.render())
app.add_route("/api/carrot/", carrot_view)
app.add_route("/api/chicken/", ChickenInfoView())
print(app.get("/api/chicken/"))
app.add_route("/api/tomato/", TomatoInfoView())
print(app.get("/api/tomato/"))
print(app.urls())
print(type(View.render))
print(isinstance(home_view, View))
print(issubclass(ChickenInfoView, View))
class LegalView(ShoutingHTMLView):
    body = 'you agree to our terms of service!'

legal_view = LegalView()
app.add_route("/legal/", legal_view)
print(app.get("/legal/"))
print(isinstance(legal_view, HTMLView))

original_htmlview_render = HTMLView.render
def new_htmlview_render(self):
    # Add <p> tag around content
    return '<html><body><p>' + self.body + '<p></body></html>'

HTMLView.render = new_htmlview_render
print(legal_view.render())