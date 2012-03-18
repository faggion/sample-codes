(function(){
    function Base(opts){
        this.a = 1;
        this.b = 2;
        this.get = function(){
            return this.c;
        };
    }

    function Foo(){
        this.c = 3;
    }
    Foo.prototype = new Base;

    var f = new Foo();
    console.debug(f);
    console.debug(f.a);
    console.debug(f.get());
})();