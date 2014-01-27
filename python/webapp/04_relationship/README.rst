Todo
--------------------------------------------------

- API化とangularjsに載せ替え
- カスタムフィールド


Babelとpytzをinstall
--------------------------------------------------

.. code-block:: none
  
  % cd /tmp/
  % wget http://pypi.python.org/packages/source/g/gaepytz/gaepytz-2011h.zip#md5=0f130ef491509775b5ed8c5f62bf66fb
  % unzip gaepytz-2011h.zip
  % cd gaepytz-2011h
  % zip -r /tmp/pytz.zip pytz
  % cd /tmp/
  % wget http://ftp.edgewall.com/pub/babel/Babel-0.9.6.zip
  % unzip Babel-0.9.6.zip
  % cd Babel-0.9.6
  % zip -r /tmp/babel.zip babel
  % mv /tmp/babel.zip /path/to/project
  % mv /tmp/pytz.zip /path/to/project


翻訳ファイル作成手順 (更新)
--------------------------------------------------

.. code-block:: none
  
  % pybabel extract -F ./babel.cfg -o ./locale/messages.pot .
  % pybabel update -i locale/messages.pot -d locale -l ja_JP
  % pybabel update -i locale/messages.pot -d locale -l en_US
  % pybabel compile -d locale


翻訳ファイル作成手順 (初期化)
--------------------------------------------------

.. code-block:: none
  
  % pybabel extract -F ./babel.cfg -o ./locale/messages.pot .
  % pybabel init -i locale/messages.pot -d locale -l ja_JP
  % pybabel init -i locale/messages.pot -d locale -l en_US
  % pybabel compile -d locale
