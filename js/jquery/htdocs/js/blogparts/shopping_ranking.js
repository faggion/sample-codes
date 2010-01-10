if(typeof BLOGPARTS == 'undefined'){
  var BLOGPARTS = {};
}
BLOGPARTS.template = '<div>{#foreach $T.items as i}<a href="{$T.i.url}"><img src="{$T.i.img}"/></a>{#/for}</div>';
BLOGPARTS.showRanking = function (params){
    var url  = 'http://shopping.yahooapis.jp/ShoppingWebService/V1/json/categoryRanking';
    $.ajax({
        url:url,
        dataType:'jsonp',
        data:{
            affiliate_type: params.affiliate_type,
            affiliate_id: params.affiliate_id,
            category_id: params.category_id,
            appid: params.appid,
        },
        success:function(r){
            var vars = {
                items: []
            };
            for(var i=0;i<r.ResultSet.totalResultsReturned;i++){
                var e = r.ResultSet[0].Result[i];
                var item = {
                    url: e.Url + "#ItemInfo",
                    img: e.Image.Medium,
                    title: e.Name.substr(0, 20),
                    rank: i+1
                }
                vars.items.push(item);
                if(params.max == vars.items.length) break;
            }
            $(params.tag).setTemplate(BLOGPARTS.template);
            $(params.tag).processTemplate(vars);
        },
    });
};
BLOGPARTS.show = function (type, params){
    var name = 'show' + type;
    if(typeof this[name] == 'function'){
        this[name](params);
    }
};
