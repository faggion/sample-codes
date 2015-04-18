var News;
(function (News) {
    var Infra;
    (function (Infra) {
        var Storage = (function () {
            function Storage() {
                this.browserSupport = false;
                if (window.localStorage) {
                    this.browserSupport = true;
                }
            }
            Storage.prototype.getItem = function (key) {
                if (this.browserSupport) {
                    return window.localStorage.getItem(key);
                }
            };
            Storage.prototype.setItem = function (key, data) {
                if (this.browserSupport) {
                    return window.localStorage.setItem(key, data);
                }
            };
            Storage.prototype.removeItem = function (key) {
                if (this.browserSupport) {
                    return window.localStorage.removeItem(key);
                }
            };
            return Storage;
        })();
        Infra.Storage = Storage;
    })(Infra || (Infra = {}));
})(News || (News = {}));
/// <reference path="Storage.ts"/>
var NEWS;
(function (NEWS) {
    var Infra;
    (function (Infra) {
        var Kvs = (function () {
            function Kvs(prefix) {
                if (prefix === void 0) { prefix = 'news-'; }
                this.storage = new Storage();
                this.prefix = prefix;
            }
            Kvs.prototype.generateKey = function (key) {
                return this.prefix + key;
            };
            Kvs.prototype.setItem = function (key, data, expireTime) {
                if (expireTime === void 0) { expireTime = 0; }
                if (expireTime !== 0 && expireTime < (new Date()).getTime() / 1000) {
                    return;
                }
                var stringifyObject = {
                    'expireTime': expireTime,
                    'data': data
                };
                this.storage.setItem(this.generateKey(key), JSON.stringify(stringifyObject));
            };
            Kvs.prototype.getItem = function (key) {
                var retrievedObject = this.storage.getItem(this.generateKey(key));
                var data = JSON.parse(retrievedObject);
                var expireTime = data.expireTime;
                if (expireTime > (new Date()).getTime() / 1000) {
                    return data.data;
                }
            };
            Kvs.prototype.removeItem = function (key) {
                this.storage.removeItem(this.generateKey(key));
            };
            return Kvs;
        })();
        Infra.Kvs = Kvs;
    })(Infra = NEWS.Infra || (NEWS.Infra = {}));
})(NEWS || (NEWS = {}));
/// <reference path="Kvs.ts"/>
var NEWS;
(function (NEWS) {
    var Infra;
    (function (Infra) {
        /**
         * @todo とりあえずドメイン指定などはサポートせずに実装
         * @todo 格納するdataには"="の仕様はとりあえずNGでSimpleなKeyValueのみ許可する
         */
        var Cookie = (function () {
            function Cookie() {
            }
            /**
             *
             * @returns {boolean}
             */
            Cookie.enabled = function () {
                return navigator.cookieEnabled;
            };
            /**
             * Cookieに値を保存する
             * @todo 有効期限を設定する処理を追加する
             * @param key
             * @param data
             * @param expireTime unsupported
             */
            Cookie.prototype.setItem = function (key, data, expireTime) {
                //                document.cookie = key + "=" + data;
                this.cookies[key] = data;
                this.save();
            };
            /**
             * Cookieに保存された指定keyの値を取り出す
             * @todo 有効期限が切れている場合の処理
             * @param key
             * @returns {any} 値が見つからんかったらundefined or null or ''
             */
            Cookie.prototype.getItem = function (key) {
                var cookies = this.getCookies();
                return cookies[key];
            };
            Cookie.prototype.hasKey = function (key) {
                var cookies = this.getCookies();
                var result = cookies[key];
                // @todo 値ごとの有効期限に対応したら検証処理を追加
                return !result;
            };
            Cookie.prototype.getCookies = function () {
                if (undefined === this.cookies) {
                    this.cookies = Cookie.parseCookie();
                }
                return this.cookies;
            };
            /**
             * @todo 実装
             */
            Cookie.prototype.save = function () {
                // 保存処理
                //                document.cookie =
            };
            /**
             *
             * @param key
             */
            Cookie.prototype.removeItem = function (key) {
                // cookieにkeyが定義去れている場合、有効期限と設定値をクリアする
                if (this.hasKey(key)) {
                    // @todo 有効期限が実装されたら検証処理を追加する
                    this.setItem(key, '');
                }
            };
            /**
             * cookieに格納されている値を連想配列に展開する
             * @todo parseの処理コストを抑えるためにできればcache挟みたい
             * @returns {Array}
             */
            Cookie.parseCookie = function () {
                var result = [];
                var cookie_string = document.cookie;
                if (cookie_string != '') {
                    var cookies = cookie_string.split('; ');
                    for (var i = 0; i < cookies.length; i++) {
                        var cookie = cookies[i].split('=');
                        // クッキーの名前をキーとして 配列に追加する
                        result[cookie[0]] = decodeURIComponent(cookie[1]);
                    }
                }
                return result;
            };
            return Cookie;
        })();
        Infra.Cookie = Cookie;
    })(Infra = NEWS.Infra || (NEWS.Infra = {}));
})(NEWS || (NEWS = {}));
/// <reference path="../../d.ts/gree/proton.d.ts"/>
/// <reference path="../../d.ts/gree/gree_news.d.ts"/>
/// <reference path="Cookie.ts"/>
var NEWS;
(function (NEWS) {
    /**
     * Gree特有の実装はここにまとめる
     */
    var Gree = (function () {
        function Gree() {
            var cookie = new NEWS.Infra.Cookie();
            this.uaType = cookie.getItem('uatype');
            this.urlScheme = cookie.getItem('URLScheme');
        }
        /**
         * SNSアプリで起動されているかどうか
         * @returns {boolean}
         */
        Gree.prototype.isApp = function () {
            return !!this.urlScheme;
        };
        /**
         * urlを展開する
         * @param url
         * @param external 外部
         */
        Gree.prototype.openUrl = function (url, external) {
            if (external === void 0) { external = false; }
            if (this.isApp()) {
                if (external) {
                    // 外部ブラウザで開く
                    //                    if (0 === url.indexOf('/')) {
                    // ios snsアプリで相対パスがサポートされないので追加する(sns appはproductionのみサポート)
                    //                        url = 'http://jp.news.gree.net' + url;
                    //                    }
                    // browserのanchorクリック次の動作を止める
                    //                    e.preventDefault();
                    //                    proton.app.launchNativeBrowser(url, function () {
                    //                    });
                    //                    gree_news.app.openExternalView(url);
                    gree_games.app.launchNativeBrowser(url);
                }
                else {
                    // pushViewで開く
                    // browserのanchorクリック次の動作を止める
                    gree_games.app.moveToURL(url);
                }
            }
            else {
                if (external) {
                    // 別タブのときは何もしない
                    window.open(url, null);
                }
                else {
                    // 現在のタブ
                    // browserのanchorクリックの動作を止める
                    location.href = url;
                }
            }
        };
        return Gree;
    })();
    NEWS.Gree = Gree;
})(NEWS || (NEWS = {}));
// <reference path="../../d.ts/jquery/jquery.d.ts"/>
var NEWS;
(function (NEWS) {
    var UserComment = (function () {
        function UserComment(user_id, list, load_more) {
            var _this = this;
            this.user_id = user_id;
            this.list = list;
            this.limit = 20;
            this.load_more_button = load_more;
            this.load_process = false;
            $(this.load_more_button).bind('click', function () { return _this.loadMore(); });
        }
        UserComment.prototype.buttonBind = function () {
            var _this = this;
            // @todo 全て読み込んだ時にload-moreを閉じる
            $(this.load_more_button).bind('click', function () { return _this.loadMore(); });
        };
        UserComment.prototype.loadMore = function () {
            var _this = this;
            if (this.load_process) {
                return;
            }
            $.ajax({
                type: "GET",
                url: "/?action=api_user_comment" + '&user_id=' + this.user_id + '&offset=' + this.list.length + '&limit=' + this.limit,
                beforeSend: function () { return _this.sendStart(); },
                success: function (data) { return _this.success(data); },
                error: function () { return _this.error(); }
            });
        };
        UserComment.prototype.sendStart = function () {
            $(this.load_more_button).unbind();
            this.load_process = true;
        };
        UserComment.prototype.error = function () {
            alert('error');
            this.load_process = false;
            this.buttonBind();
        };
        UserComment.prototype.success = function (data) {
            var _this = this;
            [].forEach.call(data.result.comments, function (comment) {
                _this.addComment(comment);
            }, false);
            this.load_process = false;
            if (this.next(data.result.comments)) {
                this.buttonBind();
            }
            else {
                this.buttonHide();
            }
        };
        UserComment.prototype.buttonHide = function () {
            this.load_more_button.style.visibility = "hidden";
            // UserComment の一番下は線がないので hr を追加する
            var hr = document.createElement('hr');
            hr.className = 'hr';
            hr.style.borderBottom = '0'; // 白い線がでるので消す
            document.getElementById('owner-comment-list').appendChild(hr);
        };
        UserComment.prototype.next = function (comments) {
            return this.limit <= comments.length;
        };
        UserComment.prototype.addComment = function (data) {
            var date = new Date(data.comment.post_date);
            var month_s = ("0" + (date.getMonth() + 1)).slice(-2);
            var dd_s = ("0" + date.getDate()).slice(-2);
            var hh_s = ("0" + date.getHours()).slice(-2);
            var mm_s = ("0" + date.getMinutes()).slice(-2);
            var news_link = '/news/entry/' + data.article.news_id;
            var title = data.article.title;
            var comment_count = data.article.comment_count;
            var nickname = data.user.nickname;
            var post_date = month_s + '/' + dd_s + ' ' + hh_s + ':' + mm_s;
            var text = data.comment.data;
            var ele = document.createElement("li");
            // @see frontend/ggpnews/template/ja_JP/user/comment.tpl
            ele.className = "owner-comment";
            // 一番最初の <div></div> は上の角丸化 (.cptn:first-child) を抑止するための空要素
            ele.innerHTML = '<div></div><div class="cptn skGray"><div class="flex"><a class="tap" onclick="location.href=\'' + news_link + '\'"><div class="itm vaM"><h2>' + title + '</h2></div></a><div class="wrapBtnL vaM taR"><span class="spr s18_sns_comment vaM"></span><span class="minorL fwN vaM comment-count">' + comment_count + '</span></div></div></div><div class="cst"><div class="in newsBox"><div class="flex"><div class="itm"><p class="lead space"><a href="http://sns.gree.net/?p#user_id=' + data.user.user_id + '&view=profile_info" class="lnk">' + nickname + '</a></p><p class="minor space6">' + post_date + '</p></div><div class="itmCaret delete-button"><span class="spr ia18_close_form"></span></div></div><div class="flex"><p class="lineM space6 text-comment">' + text + '</p></div></div></div><div class="cst" style="display: none;"></div>';
            document.getElementById('owner-comment-list').appendChild(ele);
            new NEWS.UserCommentDelete(data.article.news_id, data.comment.comment_id, ele.getElementsByClassName("delete-button")[0], ele);
            // もっと見るは未実装 (?)
            //            var self = this;
            //            ele.getElementsByClassName("seemore-handler")[0].addEventListener("click", function () {
            //                self.seeMore(ele)
            //            }, false);
        };
        // @todo 機能重複なのでリファクタリングする
        // もっと見るは未実装 (?)
        UserComment.prototype.seeMore = function (obj) {
            var newstextBox = obj.getElementsByClassName("text-comment")[0];
            var newstextBoxCls = newstextBox.className;
            var seeMoreButton = obj.getElementsByClassName("seemore-handler")[0];
            if (newstextBoxCls.indexOf("open") < 0) {
                newstextBox.className += " open";
                seeMoreButton.innerHTML = '閉じる<span class="sprite interactive18-3_5 top"></span>';
            }
            else {
                newstextBox.className = newstextBoxCls.replace(/ open/, "");
                seeMoreButton.innerHTML = 'もっと見る<span class="sprite interactive18-3_4 top"></span>';
            }
        };
        return UserComment;
    })();
    NEWS.UserComment = UserComment;
    var UserCommentDelete = (function () {
        function UserCommentDelete(news_id, comment_id, deleteButton, comment) {
            var _this = this;
            this.news_id = news_id;
            this.comment_id = comment_id;
            this.deleteButton = deleteButton;
            this.commentElement = comment;
            this.send_process = false;
            deleteButton.addEventListener('click', function () { return _this.send(); }, false);
        }
        UserCommentDelete.prototype.send = function () {
            var _this = this;
            if (this.send_process) {
                return;
            }
            if (true === confirm("このコメントを削除しますか？")) {
                $.ajax({
                    type: "POST",
                    url: "/?action=api_news_entry_comment_delete",
                    data: this.sendData(),
                    success: function (data) { return _this.success(data); },
                    error: function () { return _this.error(); }
                });
            }
        };
        UserCommentDelete.prototype.sendData = function () {
            return { news_id: this.news_id, comment_id: this.comment_id };
        };
        UserCommentDelete.prototype.success = function (data) {
            this.deleteComment();
            this.send_process = false;
        };
        UserCommentDelete.prototype.error = function () {
            this.send_process = false;
        };
        UserCommentDelete.prototype.deleteComment = function () {
            this.commentElement.parentNode.removeChild(this.commentElement);
        };
        return UserCommentDelete;
    })();
    NEWS.UserCommentDelete = UserCommentDelete;
})(NEWS || (NEWS = {}));
/// <reference path="../../d.ts/jquery/jquery.d.ts"/>
var Infrastructure;
(function (Infrastructure) {
    var Application = (function () {
        function Application() {
            var path = location.pathname;
            switch (true) {
                case /news\/entry/.test(path):
                    this.action_name = 'news_entry';
                    break;
                case /user\/comments/.test(path):
                    this.action_name = 'news_comments';
                    break;
                case /^\/$/.test(path):
                    this.action_name = location.search;
                    break;
                default:
                    this.action_name = path;
            }
        }
        Application.prototype.getAction = function () {
            return this.action_name;
        };
        return Application;
    })();
    Infrastructure.Application = Application;
})(Infrastructure || (Infrastructure = {}));
/// <reference path="../../d.ts/jquery/jquery.d.ts"/>
/// <reference path="UserComment.ts"/>
/// <reference path="../../d.ts/google.analytics/ga.d.ts"/>
/// <reference path="../infrastructure/application.ts"/>
var NEWS;
(function (NEWS) {
    /**
     * Commentの投稿処理
     */
    var CommentForm = (function () {
        function CommentForm(news_id, sendButton, textarea, textCounter, textLengthLimit, comment_list) {
            var _this = this;
            this.news_id = news_id;
            this.textLengthLimit = parseInt(textLengthLimit.innerText);
            this.sendButton = sendButton;
            this.textCounter = textCounter;
            this.textarea = textarea;
            this.send_process = false;
            this.comment_list = comment_list;
            $(sendButton).bind('click', function (event) {
                // browserのform動作を止める
                event.preventDefault();
                ga('send', {
                    "hitType": "event",
                    "eventCategory": "CommentPost",
                    "eventAction": (new Infrastructure.Application()).getAction(),
                    "eventLabel": location.href,
                    "eventValue": 1,
                    'nonInteraction': 1
                });
                _this.send();
            });
            var self = this;
            var timer = null;
            // textareaにイベント登録
            $(textarea).bind('touchstart touchend mouseup mousedown click keyup keydown keypress change paste cut focus', function () {
                window.clearInterval(timer);
                timer = window.setInterval(function () {
                    setTimeout(function () {
                        self.textCount(textarea, textCounter, self.textLengthLimit);
                    }, 10);
                }, 10);
            }, false);
            // textareaのカウントアップ用タイマー外す
            $(textarea).bind("blur", function () {
                window.clearInterval(timer);
            }, false);
            this.textarea.onfocus = function () {
                $("#greeCommonFooter").hide();
            };
            this.textarea.onblur = function () {
                $("#greeCommonFooter").show();
            };
        }
        CommentForm.prototype.send = function () {
            var _this = this;
            if (!this.validate()) {
                return;
            }
            if (this.send_process) {
                return;
            }
            $.ajax({
                type: "POST",
                url: "/?action=api_news_entry_comment_commit",
                data: this.sendData(),
                beforeSend: function () { return _this.sendStart(); },
                success: function (data) { return _this.success(data); },
                error: function (xhr, status, err) { return _this.error(xhr, status, err); }
            });
        };
        CommentForm.prototype.sendStart = function () {
            $(this.sendButton).unbind();
            this.send_process = true;
        };
        /**
         * エラー処理
         * @param xhr
         * @param status
         * @param err
         */
        CommentForm.prototype.error = function (xhr, status, err) {
            var _this = this;
            var response_body = JSON.parse(xhr.responseText);
            var response_status = response_body['status'];
            switch (response_status['code']) {
                case 1003:
                    alert('再度ログインを実行して下さい');
                    // login buttonの表示
                    var ele = document.createElement('button');
                    ele.id = "require-login";
                    $(ele).addClass("btn lrg prim");
                    ele.innerText = "ログインしてコメントする";
                    $('#comment-form-area').empty().append(ele);
                    $("#require-login").click(function () {
                        ga('send', {
                            "hitType": "event",
                            "eventCategory": "Login",
                            "eventAction": (new Infrastructure.Application()).getAction(),
                            "eventLabel": location.href,
                            "eventValue": 1,
                            'nonInteraction': 1
                        });
                        (new NEWS.Login).apply();
                    });
                    // 後片付け
                    this.send_process = false;
                    break;
                default:
                    alert('送信に失敗しました');
                    // 再送処理？
                    $(this.sendButton).bind('click', function () { return _this.send(); });
                    this.send_process = false;
            }
        };
        // localStorageが有効な場合formの値を保存しておく
        CommentForm.prototype.saveForm = function () {
            if (window.localStorage) {
                window.localStorage.setItem("draft" + this.getNewsId(), this.getMessage());
            }
        };
        CommentForm.prototype.loadForm = function () {
            if (window.localStorage) {
                var message = window.localStorage.getItem("draft" + this.getNewsId());
            }
        };
        // 送信成功
        CommentForm.prototype.success = function (data) {
            var _this = this;
            $(this.textarea).val("");
            $(this.textCounter).html("0");
            [].forEach.call(document.getElementsByClassName("comment-count"), function (countEle) {
                countEle.innerText = parseInt(countEle.innerText) + 1;
            });
            this.addComment(data.result.comment);
            alert('コメントの投稿が完了しました');
            this.send_process = false;
            $(this.sendButton).bind('click', function () { return _this.send(); });
        };
        /**
         * 文字数カウントの制御
         * @param textarea
         * @param counter
         * @param inputLimit
         */
        CommentForm.prototype.textCount = function (textarea, counter, inputLimit) {
            // 入力文字数
            var inputLength = this.stringCount($(textarea).val());
            $(counter).html(inputLength.toString());
            if (inputLimit < inputLength) {
                // 制限を超えている場合
                $(counter).css({
                    'color': ' #ff0000',
                    'font-weight': 'bold'
                });
            }
            else {
                // 制限を超えていない場合
                $(counter).css({
                    'color': '#789',
                    'font-weight': 'normal'
                });
            }
        };
        CommentForm.prototype.sendData = function () {
            return { news_id: this.getNewsId(), comment: this.getMessage() };
        };
        CommentForm.prototype.getMessage = function () {
            return $(this.textarea).val();
        };
        CommentForm.prototype.getNewsId = function () {
            return this.news_id;
        };
        /**
         * 入力値のバリデーションチェックを実施する
         * @returns {boolean}
         */
        CommentForm.prototype.validate = function () {
            if (1 > this.stringCount(this.getMessage())) {
                alert('コメントを入力して下さい');
                return false;
            }
            if (this.textLengthLimit < this.stringCount(this.getMessage())) {
                alert('コメントの文字数が制限を超えています');
                return false;
            }
            return true;
        };
        /**
         * サロゲートペアを考慮して文字数をカウントする
         * @param str
         * @returns {number}
         */
        CommentForm.prototype.stringCount = function (str) {
            var length = 0;
            for (var index = 0; index < str.length; index += 1) {
                var high = str.charCodeAt(index);
                var low = str.charCodeAt(index + 1);
                if ((0xD800 <= high && high <= 0xDBFF) && (0xDC00 <= low && low <= 0xDFFF)) {
                    index += 1;
                }
                length += 1;
            }
            return length;
        };
        /**
         * 投稿コメントをコメントリストへ追加
         * @param data
         */
        CommentForm.prototype.addComment = function (data) {
            var date = new Date(Date.parse(data.post_date));
            var month_s = ("0" + (date.getMonth() + 1)).slice(-2);
            var dd_s = ("0" + date.getDate()).slice(-2);
            var hh_s = ("0" + date.getHours()).slice(-2);
            var mm_s = ("0" + date.getMinutes()).slice(-2);
            var ele = document.createElement("li");
            ele.className = 'cst';
            var commentBoxHtml;
            if (!document.getElementById('comment-list')) {
                // @see frontend/ggpnews/template/ja_JP/inc/entry/comment.inc.tpl
                var headHTML = '<div class="cptn skGray"><div class="flex"><div class="itm vaM"><h2>この記事のみんなのコメント</h2></div><div class="wrapBtnL vaM taR"><span class="spr s18_sns_comment vaM"></span><span class="minorL fwN vaM comment-count">1</span></div></div></div>';
                var commentListEle = document.createElement("ul");
                commentListEle.id = "comment-list";
                commentListEle.className = "unstyl patty";
                ele.innerHTML = '<div class="in newsBox comment-box"><div class="flex"><div class="itm"><p class="lead space"><a href="http://sns.gree.net/?p#user_id=' + data.user_id + '&view=profile_info" class="lnk">' + data.nickname + '</a></p><p class="minor space6">' + month_s + '/' + dd_s + ' ' + hh_s + ':' + mm_s + '</p></div><div class="itmCaret delete-button"><span class="spr ia18_close_form"></span></div></div><div class="flex"><p class="lineM space6 textHideShowArea text-comment">' + data.text + '</p></div></div></div>';
                commentListEle.appendChild(ele);
                // @todo 依存排除する(後で)
                $("#news-entry").append(headHTML);
                $("#news-entry").append(commentListEle);
            }
            else {
                // @todo 分離する
                // @see frontend/ggpnews/template/ja_JP/inc/entry/comment.inc.tpl
                ele.innerHTML = '<div class="in newsBox comment-box"><div class="flex"><div class="itm"><p class="lead space"><a href="http://sns.gree.net/?p#user_id=' + data.user_id + '&view=profile_info" class="lnk">' + data.nickname + '</a></p><p class="minor space6">' + month_s + '/' + dd_s + ' ' + hh_s + ':' + mm_s + '</p></div><div class="itmCaret delete-button"><span class="spr ia18_close_form"></span></div></div><div class="flex"><p class="lineM space6 textHideShowArea text-comment">' + data.text + '</p></div></div></div>';
                var commentList = document.getElementById('comment-list');
                commentList.insertBefore(ele, commentList.firstChild);
            }
            // もっと見るは未実装 (?)
            //            [].forEach.call(document.getElementsByClassName('comment-box'), (commentBox) => {
            //                var self = this;
            //                commentBox.getElementsByClassName("seemore-handler")[0].addEventListener("click", function () {
            //                    self.seeMore(<HTMLElement>commentBox)
            //                }, false);
            //            });
            // 動的に追加した要素に対して削除イベントを割り当てる
            new NEWS.UserCommentDelete(parseInt(data.news_id), parseInt(data.comment_id), ele.getElementsByClassName("delete-button")[0], ele);
        };
        /**
         * 利用してなさそう?
         * @param obj
         */
        CommentForm.prototype.seeMore = function (obj) {
            var newstextBox = obj.getElementsByClassName("text-comment")[0];
            var newstextBoxCls = newstextBox.className;
            var seeMoreButton = obj.getElementsByClassName("seemore-handler")[0];
            if (newstextBoxCls.indexOf("open") < 0) {
                newstextBox.className += " open";
                seeMoreButton.innerHTML = '閉じる<span class="sprite interactive18-3_5 top"></span>';
            }
            else {
                newstextBox.className = newstextBoxCls.replace(/ open/, "");
                seeMoreButton.innerHTML = 'もっと見る<span class="sprite interactive18-3_4 top"></span>';
            }
        };
        return CommentForm;
    })();
    NEWS.CommentForm = CommentForm;
    var CommentList = (function () {
        function CommentList(news_id, list, load_more) {
            var _this = this;
            this.news_id = news_id;
            this.list = list;
            this.limit = 20;
            this.load_more_button = load_more;
            this.load_process = false;
            $(this.load_more_button).bind('click', function () { return _this.loadMore(); });
        }
        CommentList.prototype.buttonBind = function () {
            var _this = this;
            $(this.load_more_button).bind('click', function () { return _this.loadMore(); });
        };
        CommentList.prototype.loadMore = function () {
            var _this = this;
            if (this.load_process) {
                return;
            }
            $.ajax({
                type: "GET",
                url: "/?action=api_news_entry_comment" + '&news_id=' + this.news_id + '&offset=' + this.list.length + '&limit=' + this.limit,
                beforeSend: function () { return _this.sendStart(); },
                success: function (data) { return _this.success(data); },
                error: function () { return _this.error(); }
            });
        };
        CommentList.prototype.sendStart = function () {
            $(this.load_more_button).unbind();
            this.load_process = true;
        };
        CommentList.prototype.error = function () {
            this.load_process = false;
            this.buttonBind();
        };
        CommentList.prototype.success = function (data) {
            var _this = this;
            [].forEach.call(data.result.comments, function (comment) {
                _this.add(comment);
            }, false);
            this.load_process = false;
            if (this.next(data.result.comments)) {
                this.buttonBind();
            }
            else {
                this.buttonHide();
            }
        };
        CommentList.prototype.buttonHide = function () {
            this.load_more_button.style.visibility = "hidden";
        };
        CommentList.prototype.next = function (comments) {
            return this.limit <= comments.length;
        };
        CommentList.prototype.add = function (data) {
            var date = new Date(data.post_date);
            var month_s = ("0" + (date.getMonth() + 1)).slice(-2);
            var dd_s = ("0" + date.getDate()).slice(-2);
            var hh_s = ("0" + date.getHours()).slice(-2);
            var mm_s = ("0" + date.getMinutes()).slice(-2);
            var ele = document.createElement("li");
            ele.className = 'cst';
            ele.innerHTML = '<div class="in newsBox comment-box"><div class="flex"><div class="itm"><p class="lead space"><a href="http://sns.gree.net/?p#user_id=' + data.user_id + '&view=profile_info" class="lnk">' + data.nickname + '</a></p><p class="minor space6">' + month_s + '/' + dd_s + ' ' + hh_s + ':' + mm_s + '</p></div>' + (data.is_delete ? '<div class="itmCaret delete-button"><span class="spr ia18_close_form"></span></div>' : '') + '</div><div class="flex"><p class="lineM space6 textHideShowArea text-comment">' + data.text + '</p></div></div></div>';
            var commentList = document.getElementById('comment-list');
            commentList.appendChild(ele);
            // もっと見るは未実装 (?)
            //            var self = this;
            //            ele.getElementsByClassName("seemore-handler")[0].addEventListener("click", function () {
            //                self.seeMore(ele)
            //            }, false);
            if (data.is_delete) {
                new NEWS.UserCommentDelete(parseInt(data.news_id), parseInt(data.comment_id), ele.getElementsByClassName("delete-button")[0], ele);
            }
        };
        // @todo 機能重複なのでリファクタリングする
        // もっと見るは未実装 (?)
        CommentList.prototype.seeMore = function (obj) {
            var newsTextBox = obj.getElementsByClassName("text-comment")[0];
            var newsTextBoxCls = newsTextBox.className;
            var seeMoreButton = obj.getElementsByClassName("seemore-handler")[0];
            if (newsTextBoxCls.indexOf("open") < 0) {
                newsTextBox.className += " open";
                seeMoreButton.innerHTML = '閉じる<span class="sprite interactive18-3_5 top"></span>';
            }
            else {
                newsTextBox.className = newsTextBoxCls.replace(/ open/, "");
                seeMoreButton.innerHTML = 'もっと見る<span class="sprite interactive18-3_4 top"></span>';
            }
        };
        return CommentList;
    })();
    NEWS.CommentList = CommentList;
})(NEWS || (NEWS = {}));
var NEWS;
(function (NEWS) {
    var Login = (function () {
        function Login() {
        }
        Login.prototype.apply = function () {
            location.href = this.getLoginUrl(location.href);
        };
        Login.prototype.getLoginUrl = function (callback) {
            return 'http://' + location.host + '/login/web?callback=' + callback;
        };
        return Login;
    })();
    NEWS.Login = Login;
})(NEWS || (NEWS = {}));
/// <reference path="../d.ts/jquery/jquery.d.ts"/>
/// <reference path="domain/Comment.ts"/>
/// <reference path="domain/Login.ts"/>
/// <reference path="../d.ts/google.analytics/ga.d.ts"/>
/// <reference path="domain/UserComment.ts"/>
/// <reference path="infrastructure/application.ts"/>
/// <reference path="infra/Gree.ts"/>
/// <reference path="../d.ts/lab/lab.d.ts"/>
/// <reference path="../d.ts/twitter/twitter.d.ts"/>
/// <reference path="../d.ts/facebook.d.ts"/>
// もっと簡略な表記にしたいけど思いつかないのでとりあえず
var NEWS;
(function (NEWS) {
    var News = (function () {
        function News() {
        }
        /**
         * イベントの設定前に実施するべき初期化処理
         * bindでもいいんだけど便宜上分けておきたい場合に記述
         * @returns {NEWS.News}
         */
        News.prototype.initialize = function () {
            return this;
        };
        /**
         * HTMLのDOMに対してイベントを設定する
         * @returns {NEWS.News}
         */
        News.prototype.bind = function () {
            $("#require-login").click(function () {
                ga('send', {
                    "hitType": "event",
                    "eventCategory": "Login",
                    "eventAction": (new Infrastructure.Application()).getAction(),
                    "eventLabel": location.href,
                    "eventValue": 1,
                    'nonInteraction': 1
                });
                (new NEWS.Login).apply();
            });
            NEWS.News.bindComment();
            this.bindCommentList();
            this.bindUserComment();
            this.newsBoxHandler();
            NEWS.News.tweetButton();
            this.facebookButton();
            this.lineButton();
            this.openCommentForm();
            return this;
        };
        /**
         * commentのbind処理
         */
        News.bindComment = function () {
            // routingの実装に合わせて消す
            var form = $("#comment-form");
            if (!form[0]) {
                return;
            }
            new NEWS.CommentForm(parseInt(location.pathname.split('/')[3]), form.find(".inline-comment-done").get(0), form.find(".inline-comment-textarea").get(0), form.find(".inline-comment-count").get(0), form.find(".inline-comment-limit").get(0), $(".news-box").get(0));
        };
        // Comment List
        News.prototype.bindCommentList = function () {
            // comment delete
            [].forEach.call(document.getElementsByClassName("comment-box"), function (commentBox) {
                if (0 === commentBox.getElementsByClassName("delete-button").length) {
                    return;
                }
                var newsIdEle = commentBox.getElementsByClassName("news_id")[0];
                var commentIdEle = commentBox.getElementsByClassName("comment_id")[0];
                var deleteButtonEle = commentBox.getElementsByClassName("delete-button")[0];
                new NEWS.UserCommentDelete(parseInt(newsIdEle.innerHTML), parseInt(commentIdEle.innerHTML), deleteButtonEle, commentBox);
            });
            // setup comment list
            var comment_list = $("#comment-list");
            var news_id = $("#news_id");
            if (!comment_list[0] || !news_id[0]) {
                return;
            }
            new NEWS.CommentList(parseInt(document.getElementById("news_id").innerHTML), document.getElementsByClassName("comment-box"), document.getElementById("comment-more"));
        };
        News.prototype.bindUserComment = function () {
            if (0 === document.getElementsByClassName("owner-comment").length) {
                return;
            }
            new NEWS.UserComment(parseInt(document.getElementById("user_id").innerHTML), document.getElementsByClassName("owner-comment"), document.getElementById("comment-more"));
            [].forEach.call(document.getElementsByClassName("owner-comment"), function (commentBox) {
                var newsIdEle = commentBox.getElementsByClassName("news_id")[0];
                var commentIdEle = commentBox.getElementsByClassName("comment_id")[0];
                var deleteButtonEle = commentBox.getElementsByClassName("delete-button")[0];
                new NEWS.UserCommentDelete(parseInt(newsIdEle.innerHTML), parseInt(commentIdEle.innerHTML), deleteButtonEle, commentBox);
            });
        };
        News.prototype.newsBoxHandler = function () {
            return;
            var self = this;
            [].forEach.call(document.getElementsByClassName("comment-box"), function (commentBox) {
                //                self.viewSeeMore(commentBox);
                var Handler = commentBox.getElementsByClassName("seemore-handler")[0];
                Handler.addEventListener("click", function () {
                    self.seeMore(commentBox);
                }, false);
            });
        };
        News.prototype.openCommentForm = function () {
            var comment_form = $(".inline-comment");
            if (!comment_form[0]) {
                return;
            }
            document.getElementsByClassName("inline-comment")[0].addEventListener('click', function () {
                this.className = "inline-comment-open";
            }, false);
        };
        // @todo 非表示領域の高さを取得できないのでまだ使えない
        News.prototype.viewSeeMore = function (obj) {
            var textArea = obj.getElementsByClassName("text-comment")[0];
            var clientHeight = textArea.clientHeight; // Browserで表示される領域
            var scrollHeight = textArea.scrollHeight; // 実際の領域
            //            alert(clientHeight + ' ' + scrollHeight);
            if (scrollHeight <= clientHeight) {
                var seeMoreButton = obj.getElementsByClassName("seemore-handler")[0];
                //                alert('hidden');
                seeMoreButton.style.setProperty("visibility", "hidden");
            }
        };
        News.prototype.seeMore = function (obj) {
            var newstextBox = obj.getElementsByClassName("text-comment")[0];
            var newstextBoxCls = newstextBox.className;
            var seeMoreButton = obj.getElementsByClassName("seemore-handler")[0];
            if (newstextBoxCls.indexOf("open") < 0) {
                newstextBox.className += " open";
                seeMoreButton.innerHTML = '閉じる<span class="sprite interactive18-3_5 top"></span>';
            }
            else {
                newstextBox.className = newstextBoxCls.replace(/ open/, "");
                seeMoreButton.innerHTML = 'もっと見る<span class="sprite interactive18-3_4 top"></span>';
            }
        };
        News.prototype.facebookButton = function () {
            window.fbAsyncInit = function () {
                if (FB && FB.Event && FB.Event.subscribe) {
                    FB.Event.subscribe('edge.create', function (opt_target) {
                        ga('send', {
                            'hitType': 'social',
                            'socialNetwork': 'facebook',
                            'socialAction': 'like',
                            'socialTarget': opt_target,
                            'page': ''
                        });
                    });
                    FB.Event.subscribe('edge.remove', function (opt_target) {
                        ga('send', {
                            'hitType': 'social',
                            'socialNetwork': 'facebook',
                            'socialAction': 'unlike',
                            'socialTarget': opt_target,
                            'page': ''
                        });
                    });
                    FB.Event.subscribe('message.send', function (opt_target) {
                        ga('send', {
                            'hitType': 'social',
                            'socialNetwork': 'facebook',
                            'socialAction': 'send',
                            'socialTarget': opt_target,
                            'page': ''
                        });
                    });
                }
            };
            var js;
            var fjs = document.getElementsByTagName('script')[0];
            if (document.getElementById('facebook-jssdk'))
                return;
            js = document.createElement('script');
            js.id = 'facebook-jssdk';
            js.src = "//connect.facebook.net/ja_JP/all.js#xfbml=1&appId=445928005542178";
            fjs.parentNode.insertBefore(js, fjs);
        };
        News.tweetButton = function () {
            //// official twitter button script
            //twttr.widgets.createShareButton("https://dev.twitter.com/", document.getElementById("new-button"), {
            //    count: "none",
            //    text: "Sharing a URL using the Tweet Button"
            //}).then(function (el) {
            //    console.log("Button created.");
            //});
            //if (typeof twttr != 'undefined') {
            //    twttr.ready(function (twttr) {
            //        twttr.events.bind('click', function (event) {
            //            ga('send', {
            //                'hitType': 'social',
            //                'socialNetwork': 'twitter',
            //                'socialAction': 'send',
            //                'socialTarget': window.location.href,
            //                'page': ''
            //            });
            //        });
            //    });
            //}
        };
        News.prototype.lineButton = function () {
            [].forEach.call(document.getElementsByClassName("line"), function (Button) {
                Button.addEventListener('click', function () {
                    ga('send', {
                        "hitType": "event",
                        "eventCategory": "Line",
                        "eventAction": "news_entry",
                        "eventLabel": location.href.toString(),
                        "eventValue": 1,
                        'nonInteraction': 1
                    });
                }, false);
            });
        };
        return News;
    })();
    NEWS.News = News;
})(NEWS || (NEWS = {}));
(new NEWS.News).initialize().bind();
// @todo 後で調整する
var NEWS;
(function (NEWS) {
    var GA;
    (function (GA) {
        /**
         * tapを外す
         * @param element
         * @param callback
         */
        function unbindTap(element, callback) {
            if ("ontouchstart" in window) {
                if ("undefined" === typeof callback) {
                    $(element).off('touchstart touchmove touchend');
                }
                else {
                    $(element).off('touchstart touchmove touchend', callback);
                }
            }
            else {
                if ("undefined" === typeof callback) {
                    $(element).off('mousedown mousemove mouseup mouseout');
                }
                else {
                    $(element).off('mousedown mousemove mouseup mouseout', callback);
                }
            }
        }
        /**
         * tapイベントを付与する
         * @param element
         * @param callback
         */
        function bindTap(element, callback) {
            if ("ontouchstart" in window) {
                $(element).on('touchstart touchmove touchend', callback);
            }
            else {
                $(element).on('mousedown mousemove mouseup mouseout', callback);
            }
        }
        /**
         * イベント制御
         * @param e
         * @param element
         * @param callback
         */
        function handleButton(e, element, callback) {
            switch (e.type) {
                case 'touchstart':
                case 'mousedown':
                    $(element).addClass('tapped');
                    break;
                case 'touchmove':
                case 'mousemove':
                    if ($(element).hasClass('tapped')) {
                        $(element).removeClass('tapped');
                    }
                    break;
                case 'touchend':
                case 'mouseup':
                    e.preventDefault();
                    if ($(element).hasClass('tapped')) {
                        $(element).removeClass('tapped');
                        callback(e);
                    }
                    break;
                case 'mouseout':
                    if ($(element).hasClass('tapped')) {
                        $(element).removeClass('tapped');
                    }
                    break;
            }
        }
        /**
         * Google AnalyticsにEventTrackingを送信する
         * moduleにまとめたい。
         * @param linkEle
         */
        function clickEvent(linkEle) {
            var category = $(linkEle).attr('data-category');
            var action = $(linkEle).attr('data-action');
            var label = $(linkEle).attr('data-label');
            var value = $(linkEle).attr('data-value');
            if (!category || !action)
                return; // category or action is empty.
            ga('send', {
                "hitType": "event",
                "eventCategory": category,
                "eventAction": action,
                "eventLabel": label,
                "eventValue": value
            });
        }
        function anchor(e, anchorEle) {
            // href属性を持つ要素を探す
            var linkEle = undefined;
            if (anchorEle.hasAttribute('href')) {
                linkEle = anchorEle;
            }
            else {
                linkEle = $(anchorEle).find('[href]').get(0);
            }
            // href属性を持つ要素が見つかった場合の処理
            if (linkEle.hasAttribute('href')) {
                // event trackingを送信する
                clickEvent(linkEle);
                // anchor tagのhref用をを参照してbrowserがevent tracking送信前に遷移してしまうので、遷移を止める
                // preventDefault辺りで制御したほうがいいかも
                var gree = new NEWS.Gree();
                e.preventDefault();
                gree.openUrl($(linkEle).attr('href'), "_blank" === $(linkEle).attr('target'));
            }
        }
        /**
         * EventTrackingを設定する
         */
        function bindEventTracking() {
            $('a[href]').each(function (index, tapEle) {
                // anchor要素のすべてのclickイベントを無効にする
                $(tapEle).click(function () {
                    return false;
                });
                bindTap(tapEle, function (event) {
                    handleButton(event, tapEle, function (e) {
                        anchor(e, tapEle);
                    });
                });
            });
        }
        GA.bindEventTracking = bindEventTracking;
    })(GA = NEWS.GA || (NEWS.GA = {}));
})(NEWS || (NEWS = {}));
// google analytics
$(document).ready(function () {
    NEWS.GA.bindEventTracking();
});
