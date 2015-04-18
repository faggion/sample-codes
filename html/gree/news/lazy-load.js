var queue = {};
queue._callback = {};
queue._count = 0;
queue._state = 'production';
queue.scriptReady = function (call) {
    queue._callback[queue._count] = call;
    queue._count++;
};
queue.setState = function (state) {
    queue._state = state;
};
queue._executeCallback = function () {
    $(function () {
        for (var i = 0; i < queue._count; i++) {
            queue._callback[i]();
        }
    });
};
queue._getGreeUrl = function (is_ggp) {
    if (is_ggp) {
        return (queue._state == 'dev') ? '/' : 'http://aimg-static.gree.net/ggp/';
    } else {
        return (queue._state == 'dev') ? '/' : 'http://aimg-static.gree.net/';
    }
};
queue._getCdnUrl = function (url) {
    if (queue._state == 'production') {
        var protocol = ("https:" == document.location.protocol) ? "https://" : "http://";
        return protocol + 'gimage-cpf-ssl.gree.jp/px/58548?url=' + encodeURIComponent(url);
    } else {
        return url;
    }
};
queue.lazyLoad = function (param_suffix, url) {
    param_suffix = param_suffix ? param_suffix : '000';
    var param = "?" + param_suffix;
    var gree_url = queue._getGreeUrl(false);
    var gree_ggp_url = queue._getGreeUrl(true);


    $LAB.script(gree_ggp_url + "js/command.min.js" + param).wait()
        .script(queue._getCdnUrl(url + "js/ga_social_tracking.js" + param))
        .script(queue._getCdnUrl(url + 'js/index.min.js' + param))
        .script('./index.js' + param)
        .script(queue._getCdnUrl(url + "js/gree_games.js" + param))
        .script(queue._getCdnUrl(url + "js/gree_news.js" + param)) // -> touch/mousedownイベントを定義
        .script(gree_url + "js/autopagerize.min.js" + param) // -> もっと見るページのauto pagerize
        .script(gree_url + "js/flipsnap.min.js" + param) // -> 記事画像のFlip移動
        .script(queue._getCdnUrl(url + "js/subnavi/news.js" + param))
        .script(queue._getCdnUrl(url + "js/tpl/subnavi.tmpl.min.js" + param))
        .script("http://aimg-notice.gree.net/js/gree.notification.online.min.js").wait(function () {
            queue._executeCallback();
            GreeOnlineNotification.start();
        });
};
queue.loadExtra = function (src, callback) {
    if (typeof(src) === 'object') {
        var q = $LAB;
        $.each(src, function (index, item) {
            q = q.script(item)
        });
        q.wait(function () {
            callback()
        });
    } else {
        $LAB.script(src).wait(function () {
            callback();
        });
    }
};
