#!/usr/bin/env python
import os
import jinja2
import webapp2


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
        # type: (object, object) -> object
        if not params:
            params = {}
        template = jinja_env.get_template(view_filename)
        return self.response.out.write(template.render(params)) #self pokazuje na objekte


class MainHandler(BaseHandler):
    def get(self):
        params = {
        "title": "Ovo je neki naslov",
        "number": -56
    }
        return self.render_template("hello.html", params=params)

    def post(self):
        inputValue = self.request.get("text-input")
        inputValue1 = self.request.get("broj-input")
        params = {
            "title": inputValue,
            "number": inputValue1
        }
        return self.render_template("hello.html", params=params)


class TestHandler(BaseHandler):
    def get(self):
        return self.render_template("test.html")


class ResponseHandler(BaseHandler):
    def post(self):
        data = self.request.get("text-input")
        return self.response.write("Ovo je u redu " + data)


class CalculatorHandler(BaseHandler):
    def get(self):
        return self.render_template("calculator.html")
    def post(self):
        response = "error check your data"
        try:
            num1 = float(self.request.get("number1-input"))
            num2 = float(self.request.get("number2-input"))
            operator = self.request.get("operator-input")
            if operator == "+":
                response = num1 + num2
            elif operator == "-":
                response = num1 - num2
            elif operator == "*":
                response = num1 * num2
            elif operator == "/":
                response = num1 / num2
            else:
                response = "Krivi operator"
        except:
            response = "First and last input must be numbers"
        return self.write(response)


app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
    webapp2.Route('/test', TestHandler),
    webapp2.Route('/response', ResponseHandler),
    webapp2.Route('/calculator', CalculatorHandler)

], debug=True)
