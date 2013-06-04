(function(){
    var query = [];
    // START: 端末情報
    var navigator_keys = {
        // ブラウザ共通実装系
        "platform"       : "10",
        //"appCodeName"    : "11", // always 'mozilla'
        "appName"        : "12",
        "appVersion"     : "13",
        "language"       : "14",
        "product"        : "15",
        "productSub"     : "16",
        "cookieEnabled"  : "17",
        "doNotTrack"     : "18",
        //"userAgent"      : "19", // 通常のaccess_logフォーマットなら必要ない+AppNameで十分

        // ブラウザ独自実装系
        "browserLanguage": "21", // IE, Opera
        "systemLanguage" : "22", // IE
        "userLanguage"   : "23", // IE, Opera
        "msDoNotTrack"   : "24", // IE
        "vendor"         : "25", // Chrome
        "buildID"        : "26", // FF
        "oscpu"          : "27", // FF
        "cpuClass"       : "28", // IE
    };
    // END: 端末情報
    // START: 画面系情報
    if(typeof window.innerWidth != "undefined"){
        query.push("31=" + window.innerWidth);
    }
    if(typeof window.innerHeight != "undefined"){
        query.push("32=" + window.innerHeight);
    }
    if(typeof screen != "undefined"){
        if(typeof screen.width != "undefined"){
            query.push("33=" + screen.width);
        }
        if(typeof screen.height != "undefined"){
            query.push("34=" + screen.height);
        }
    }
    if(typeof window.devicePixelRatio != "undefined"){
        query.push("35=" + window.devicePixelRatio);
    }
    if(typeof window.innerHeight != "undefined" && 
       typeof window.innerWidth  != "undefined" &&
       parseInt(window.innerHeight) &&
       parseInt(window.innerWidth)  &&
       parseInt(window.innerHeight) < parseInt(window.innerWidth)){
        query.push("36=1"); // landscape=1, portrait=NaN
    }
    // END: 画面系情報
    // START: その他情報
    var d = new Date();
    query.push("40=" + d.getTime());
    query.push("41=" + d.getTimezoneOffset());
    if(typeof window.localStorage !== 'undefined' && window.localStorage !== null){
        window.localStorage.setItem('test','1');
        if(window.localStorage.getItem('test') === '1'){
            query.push("42=1");
        }
    }
    // END: その他情報

    for(var k in navigator_keys){
        if(typeof navigator[k] == "undefined") continue;
        if(typeof navigator[k] == "boolean"){
            if(navigator[k] == true){
                query.push(navigator_keys[k] + "=1");
            }
            else {
                query.push(navigator_keys[k] + "=0");
            }
        }
        else if(navigator[k] != ""){
            query.push(navigator_keys[k] + "=" + encodeURIComponent(navigator[k].toLowerCase()));
        }
    }

    //console.log(query.join("&"));
    var script_node = document.createElement('script');
    script_node.src = "http://q.tanarky.com/analytics.php?" + query.join("&");
    document.getElementsByTagName('body')[0].appendChild(script_node);

})();
