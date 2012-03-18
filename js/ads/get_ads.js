(function(){
     var name = "adlantis";
     var parse_class = function(str){
         var s = str.split(/\s/);
         var r = {
             "zid": undefined,
             "type": undefined
         };
         //console.debug(s);
         for(var j=0;j<s.length;j++){
             // $(NAME)_zid_***
             if(s[j].substring(0,name.length+5) == name + "_zid_"){
                 r.zid = s[j].substring(name.length+5);
             }
             else if(s[j].substring(0,name.length+6) == name + "_type_"){
                 r.type = s[j].substring(name.length+6);
             }
         }
         //console.debug(r);
         return r;
     };
     var e = document.getElementsByClassName("adlantis");
     var req = [];
     for(var i=0;i<e.length;i++){
         req.push(parse_class(e[i].className));
     }
     console.debug(req);
})();