Drawer比較
-----------------------------

- bootstrapで作る（simple-drawer.html） -> menu部分のスクロールに非対応
- sidr -> 端末を縦横にしたときにおかしくなりそう
- drawer.js = http://git.blivesta.com/drawer/responsive-left/ -> iscrollとか使ってて重い
- trunk.js -> 軽いしコード量も少ない、動作は大丈夫か？

必要なJS
-----------------------------

- zepto.js ( 最新版でOK )
- navigation.js

  - global headerとfooter を追加する

navigation_ja.jsの挙動
-----------------------------

1. cookieを使ってログイン判定して、notification数を返す、だめならログインページに飛ばす
   http://notice.gree.net/?action=api_balloon_unreadcount&filter=navigation&_=1429373534925
2. リアルタイムでfooterやheaderに情報を差し込みたいときの追加API
   http://gree.net/?action=api_navigation_announce&names%5B%5D=footer_menu&names%5B%5D=global_menu&os=o&_=1429373681447

cssのminify
-----------------------------

::

   npm install uncss --save-dev
   wget http://aimg-static.gree.net/ggp/css/moz_core.css
   wget http://aimg-static.gree.net/js/navigation_ja.js
   sh ./get_imgs.sh
   e index.html
   e moz_core.css
   uncss 'http://127.0.0.1/' > min.css
   e min.css

1. uncssをinstall
2. index.htmlの中での他のドメインへの外部参照を全部localに向けるようにDLしておく
3. uncss実行、ただしmoz_core.cssのparseエラーを解消する必要あり
4. min.css内のwarningをコメントアウト
