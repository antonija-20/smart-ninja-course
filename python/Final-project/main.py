#!/usr/bin/env python
import json
import os
import jinja2
import webapp2

from google.appengine.api import users
from google.appengine.api import urlfetch

from model import Todo
from model import Message


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

        user = users.get_current_user()
        params["user"] = user

        if user:
            logged_in = True
            logout_url = users.create_logout_url('/logout')
            params["logout_url"] = logout_url
        else:
            logged_in = False
            login_url = users.create_login_url('/messages')
            params["login_url"] = login_url

        params["logged_in"] = logged_in

        template = jinja_env.get_template(view_filename)
        return self.response.out.write(template.render(params))


class MainHandler(BaseHandler):
    def get(self):

        data = open("zagreb.json", "r").read()
        json_data = json.loads(data)
        return self.render_template("hello.html", params={
            "users": json_data
        })


class MessagesHandler(BaseHandler):
    def get(self):
        messages = Message.query(Message.deleted == False).fetch()
        params = {"messages": messages}
        return self.render_template("messages.html", params=params)

    def post(self):
        user = users.get_current_user()

        if not user:
            return self.write("You are not logged in!")

        author = self.request.get("name")
        email = user.email()
        sendto = self.request.get("to-mail")
        subject = self.request.get("to-subject")
        message = self.request.get("message")

        if not author:
            author = "Anonymous"

        if not sendto:
            sendto = "Write your email"

        if not subject:
            subject = "none"

        if "<script>" in message:
            return self.write("insert non JS")

        msg_object = Message(message=message.replace("<script>", ""))
        msg_object.author_name = author
        msg_object.email = email
        msg_object.sendto = sendto
        msg_object.subject = subject
        msg_object.put()

        return self.redirect_to("message-site")



class WeatherHandler(BaseHandler):
    def get(self):
            url = "http://samples.openweathermap.org/data/2.5/weather?id=2172797&appid=af643f9b41f8c816ac2cb081ac1bbb6c"
            result = urlfetch.fetch(url)
            json_data = json.loads(result.content)
            return self.render_template("weather.html", params={
                "data": json_data
            })






class MessageEditHandler(BaseHandler):
    def get(self, message_id):

        if not users.is_current_user_admin():
            return self.write("You are not admin!")

        message = Message.get_by_id(int(message_id))

        params = {"message": message}

        return self.render_template("message_edit.html", params=params)

    def post(self, message_id):
        if not users.is_current_user_admin():
            return self.write("You are not admin!")

        message = Message.get_by_id(int(message_id))

        text = self.request.get("message")
        message.message = text
        message.put()

        return self.redirect_to("message-site")


class MessageDeleteHandler(BaseHandler):
    def get(self, message_id):
        if not users.is_current_user_admin():
            return self.write("You are not admin!")

        message = Message.get_by_id(int(message_id))

        params = {"message": message}

        return self.render_template("message_delete.html", params=params)

    def post(self, message_id):
        if not users.is_current_user_admin():
            return self.write("You are not admin!")

        message = Message.get_by_id(int(message_id))

        message.deleted = True
        message.put()

        return self.redirect_to("message-site")


class DeletedMessagesHandler(BaseHandler):
    def get(self):
        if not users.is_current_user_admin():
            return self.write("You are not admin!")

        messages = Message.query(Message.deleted == True).fetch()

        params = {"messages": messages}

        return self.render_template("deleted_messages.html", params=params)


class MessageRestoreHandler(BaseHandler):
    def get(self, message_id):
        if not users.is_current_user_admin():
            return self.write("You are not admin!")

        message = Message.get_by_id(int(message_id))

        params = {"message": message}

        return self.render_template("message_restore.html", params=params)

    def post(self, message_id):
        if not users.is_current_user_admin():
            return self.write("You are not admin!")

        message = Message.get_by_id(int(message_id))

        message.deleted = False
        message.put()

        return self.redirect_to("message-site")


class MessageCompleteDeleteHandler(BaseHandler):
    def get(self, message_id):
        if not users.is_current_user_admin():
            return self.write("You are not admin!")

        message = Message.get_by_id(int(message_id))

        params = {"message": message}

        return self.render_template("message_complete_delete.html", params=params)

    def post(self, message_id):
        if not users.is_current_user_admin():
            return self.write("You are not admin!")

        message = Message.get_by_id(int(message_id))

        message.key.delete()

        return self.redirect_to("deleted-messages")




class LogoutHandler(BaseHandler):
    def get(self):
        return self.render_template("logout.html")


app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
    webapp2.Route('/messages', MessagesHandler, name="message-site"),
    webapp2.Route('/message/<message_id:\d+>/edit', MessageEditHandler, name="message-edit"),
    webapp2.Route('/message/<message_id:\d+>/delete', MessageDeleteHandler, name="message-delete"),
    webapp2.Route('/message/<message_id:\d+>/restore', MessageRestoreHandler, name="message-restore"),
    webapp2.Route('/message/<message_id:\d+>/complete-delete', MessageCompleteDeleteHandler, name="message-complete-delete"),
    webapp2.Route('/deleted', DeletedMessagesHandler, name="deleted-messages"),
    webapp2.Route('/logout', LogoutHandler),
    webapp2.Route('/weather', WeatherHandler)
], debug=True)
