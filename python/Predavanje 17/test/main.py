#!/usr/bin/env python
import os
import jinja2
import webapp2
import random

template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=False)


class BaseHandler(webapp2.RequestHandler):

    def write(self, *a, **kw):
        return self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        return self.write(self.render_str(template, **kw))

    def render_template(self, view_filename, params=None):
        if not params:
            params = {}
        template = jinja_env.get_template(view_filename)
        return self.response.out.write(template.render(params))

trenutna_drzava = "drzava"
class MainHandler(BaseHandler):
    drzave = {
        "Hrvatska": "Zagreb",
        "Slovenija": "Ljubljana",
        "Austrija": "Bec",

    }
    trenutna_drzava = "Hrvatska"
    trenutna_pozicija = random.randint(0,2)
    self.trenutna_drzava = self.drzave.keys()[trenutna_pozicija]
    def get(self):
        parametri = {
            "drzava": "Hrvatska"
        }

        return self.render_template("homepage.html", parametri)
    def post(self):
        rezultati = "Nema"
        grad = self.request.get("grad").lower()
        if(self.drzave[self.trenutna_drzava].lower() == grad):
            rezultati = "odgovor je tocan"


app = webapp2.WSGIApplication([
    ('/', MainHandler),
], debug=True)
