(function(){
    function Base(opts){
        this.a = 1;
        this.b = 2;
        this.get = function(){
            return this.c;
        };
    }
    function Foo(){
        Base.apply(this,arguments);
        this.c = 3;
    }
    var f = new Foo();
    console.debug(f);
    console.debug(f.get()); // 3
})();