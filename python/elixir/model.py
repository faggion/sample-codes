from elixir import *

#metadata.bind = "sqlite:///movies.sqlite"
metadata.bind = "sqlite:////tmp/foo.sqlite"
metadata.bind.echo = True

class Movie(Entity):
    title = Field(Unicode(30))
    year  = Field(Integer)
    description = Field(UnicodeText)
    
    def __repr__(self):
        return '<Movie "%s" (%d)>' % (self.title, self.year)
