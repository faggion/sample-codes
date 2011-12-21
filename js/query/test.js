(function (){
     default_query = {
         foo : 'bar',
         hoge : "あいう"
     };
     url = 'http://www.yahoo.co.jp/';

     $('.bind').change(function(){
                           q = {};
                           q["myinput1"]  = $("#input1").val();
                           q["myinput2"]  = $("#input2").val();
                           q["mychk1"]    = $("input[name=mychk1]").is(":checked") ? 1 : 0;
                           q["mychk2"]    = $("input[name=mychk2]").is(":checked") ? 1 : 0;
                           q["myradio1"]  = $("input[name=myradio1]:checked").val();
                           q["myselect1"] = $("#myselect1").val();
                           alert(build_query(url, q));
                       });
     function build_query(u, qq){
         q = [];
         var c = encodeURIComponent;
         for (var k in qq){
             q.push(c(k) + '=' + c(qq[k]));
         }
         return u + '?' + q.join('&');
     }
})();

