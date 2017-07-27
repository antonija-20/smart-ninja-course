from google.appengine.ext import ndb

class Todo(ndb.Model):
    task = ndb.StringProperty()
    done = ndb.BooleanProperty(default=False)

class Message(ndb.Model):
    author_name = ndb.StringProperty()
    email = ndb.StringProperty()
    subject = ndb.StringProperty()
    sendto = ndb.StringProperty()
    message = ndb.TextProperty()
    created = ndb.DateTimeProperty(auto_now_add=True)
    deleted = ndb.BooleanProperty(default=False)