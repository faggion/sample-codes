function (){
    var imgfiles = [
        {id:'cafe',    url:'./img/cafe.png'},
        {id:'office',  url:'./img/office.png'},
        {id:'factory', url:'./img/factory.png'}
    ];
    var callback_imgloaded = function( counter, images ) {
        // ブラウザURLバー消す
        window.scrollTo(0,1);

        // create a director object
        var director = new CAAT.Director().initialize(
            320,
            //568, // 88px分スペースがある、広告を出すとか
            480,
            document.getElementById('_c1')
        );
        director.setImagesCache(images);

        var scene = director.createScene();

        //var bg = new CAAT.ActorContainer().
        var bg = new CAAT.ShapeActor().
            setShape(1).
            setBounds(0,0,director.width,director.height).
            setStrokeStyle('#0000ff').
            setLineWidth(10).
            setFillStyle('#fff');

        scene.addChild(bg);

        var cafe = new CAAT.Actor().
            setBounds(0, 0, 128, 128).
            setBackgroundImage(director.getImage('cafe'), true ).
            enableDrag().
            //mouseClick(function(){ alert('clicked'); }).
            setLocation(0, 0);
        scene.addChild(cafe);

        var office = new CAAT.ActorContainer().
            setBounds(128, 128, 128, 128).
            //setRotation( Math.PI*2*Math.random() ).
            setBackgroundImage(director.getImage('office'), false ).
            setFillStyle('#ff3fff').
            enableDrag();
        office.name = "actor_office";
        scene.addChild(office);

        var factory = new CAAT.Actor().
            setBackgroundImage(director.getImage('factory'), false ).
            setLocation(128, 256);
        scene.addChild(factory);

    };

    var img = new CAAT.ImagePreloader().loadImages(imgfiles,callback_imgloaded);

    // start the animation loop
    CAAT.loop(20);
}