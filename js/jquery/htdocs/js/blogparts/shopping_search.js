function do_remote(){
    if(typeof custom == 'undefined'){
        return;
    }
    var format_price = function(p){
        var num = new String(p);
        while(num != (num = num.replace(/^(-?\d+)(\d{3})/, "$1,$2")));
        return (num == "") ? "" : num + " 円";
    }

    var tmpl = 
        '<div style="margin:0;padding:0;text-align:left;width:{$T.width}px;border:1px solid {$T.color.border}">'+
        '<h2 style="margin:0;padding:5px 0 5px 3px;color:{$T.color.font};border-bottom:1px solid {$T.color.border};font-size:100%;background-color:{$T.color.title}">'+
        '<b>{$T.title}</b></h2>'+
        '<div style="padding:0 5px 5px 5px;">'+
        '{#foreach $T.items as i}'+
        '<div style="width:100%;margin-top:5px">'+
        '<p style="text-align:center;margin:0;padding:0"><a href="{$T.i.url}"><img border="0" src="{$T.i.img}" alt=""></a></p>'+
        '<table style="font-size:12px;width=100%"><tr>'+
        '<td rowspan="2" style="width:5%;vertical-align:top;font-weight:bold">{$T.i.rank}.</td>'+
        '<td style="padding-left:5px;width:94%"><a href="{$T.i.url}">{$T.i.title}</a></td>'+
        '</tr><tr><td><span style="padding-left:5px;text-decoration:line-through">{$T.i.price.fixed}</span>'+
        '<span style="padding-left:5px;font-size:110%;font-weight:bold;color:#900">{$T.i.price.sale}</span></td></tr></table></div>'+
        '{#/for}<p style="font-size:small;float:right;margin:10px 0 0 0;color:#555">随時更新</p><div style="clear:both"></div></div>';

    $.ajax({
        url : "http://shopping.yahooapis.jp/ShoppingWebService/V1/json/itemSearch",
        dataType : "jsonp",
        data : {
            appid : custom.appid,
            brand_id : custom.brand_id,
            affiliate_type : custom.affiliate_type,
            affiliate_id : custom.affiliate_id,
            sort: custom.sort,
            hits: custom.max_items
        },
        success : function(json){
            var tmpl_vars = {
                title: custom.title,
                width: custom.width,
                color: {
                    title: custom.title_color,
                    font: custom.font_color,
                    border: custom.border_color
                },
                items:[]
            }
            for(var i=0;i<json.ResultSet.totalResultsReturned;i++){
                var e = json.ResultSet[0].Result[i];
                if(e.Image.Original == "") continue;
                var item = {
                    url: e.Url + "#ItemInfo",
                    img: e.Image.Small,
                    title: e.Name.substr(0, 20),
                    desc: e.Description.substr(0, 20),
                    price:{
                        fixed: format_price(e.PriceLabel.FixedPrice),
                        sale: format_price(e.Price._value)
                    },
                    rank: i+1
                };
                tmpl_vars.items.push(item);
                if(custom.max_items == tmpl_vars.items.length) break;
            }
            $(custom.tag_id).setTemplate(tmpl);
            $(custom.tag_id).processTemplate(tmpl_vars);
        },
        error : function(){
            //console.log("ajax jsonp FAILED");
        }
    });
};
