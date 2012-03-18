(function(){
    function Base(opts){
        this.a = 1;
        this.b = 2;
        this.get = function(){
            return this.b;
        };
    }

    function Foo(){
        this.c = 3;
        this.get = function(){
            return this.c;
        };
    }
    Foo.prototype = new Base;
    var foo = new Foo();
    console.debug(foo);
    console.debug(foo.a);
    console.debug("Foo.get:"+ foo.get());

    //function Baz(){
    //}
    //Baz.prototype = new Base;
    function Baz(){
        Base.apply(this,arguments);
        this.c = 3;
    }
    var baz = new Baz();
    console.debug("Baz.get:"+ baz.get());
})();