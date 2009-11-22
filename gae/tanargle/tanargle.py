from google.appengine.api import users

print 'Content-Type: text/html'
print ''

user = users.get_current_user()
print 'Hello, Google App Engine! "tanargle"<br>'
if not user:
    print '<a href="'+ users.create_login_url("/")+ '">lets login</a>'
else:
    print "Hello, %s!" % user.nickname()



