todo
-------------------------

- situation

  - 1つの記事から、その記事が持つタグを全て取り出す
  - 1つのタグから、そのタグを持つ記事を全て取り出す
  - 1つの記事から、同じタグを持つ記事を全て取り出す
  - 1つのタグから、その子タグを持つ記事を全て取り出す

setup
-------------------------

::
  
  pip install MySQL-python
  migrate create tag_relation "tag relation study"
  cd tag_relation
  python manage.py version_control mysql://root@localhost/tag_relation .
  migrate manage manage.py --repository=. --url=mysql://root@localhost/tag_relation


migration
-------------------------

::
  
  python manage.py downgrade 0
  python manage.py test
  python manage.py upgrade
