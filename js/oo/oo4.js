(function(){
    function Base(opts){
        console.debug(opts);
    }
    function Foo(){
        Base.apply(this,arguments);
    }
    function Baz(){
        Base.call(this,arguments);
    }
    var foo = new Foo("a", "b", "c");
    var baz = new Baz("a", "b", "c");
})();