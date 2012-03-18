(function(){
    var Foo = function(){
        this.hoge = "HOGE";
    };
    var objF = new Foo();
    console.debug(objF);
    console.debug(objF.hoge);

    var objF2 = new Foo();
    objF2.hoge = "FUGA";

    console.debug(objF.hoge);
    console.debug(objF2.hoge);
})();