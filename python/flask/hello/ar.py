from pyactiveresource.activeresource import ActiveResource, formats
import logging

class Foo(ActiveResource):
    _site = 'http://localhost:10080/'
    #_format = formats.JSONFormat

if __name__ == "__main__":
    #p = Foo.find(1)
    #logging.error(p)
    #logging.error(p.id)
    #logging.error(p.name)

    #p = Foo.create({"id":3, "name":"hoge"})
    #p.name = 'foobar'
    #p.save()

    #p = Foo.find(from_="foos", name="tanarky")
    p = Foo.find(name="is_this_args", order="+title", offset=10)
    logging.error(p)


