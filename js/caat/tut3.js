function (){
    var imgfiles = [
        {id:'cafe',    url:'./img/cafe.png'},
        {id:'office',  url:'./img/office.png'},
        {id:'factory', url:'./img/factory.png'}
    ];
    var callback_imgloaded = function( counter, images ) {
        // create a director object
        var director = new CAAT.Director().initialize(
            800,
            600,
            document.getElementById('_c1')
        );
        director.setImagesCache(images);

        var scene = director.createScene();

        var bg = new CAAT.ActorContainer().
            setBounds(0,0,director.width,director.height).
            setFillStyle('#eee');// ここで背景色設定
        scene.addChild(bg);

        var cafe = new CAAT.Actor().
            setBackgroundImage(director.getImage('cafe'), true ).
            setLocation(0, 0);
        scene.addChild(cafe);

        var office = new CAAT.Actor().
            setBackgroundImage(director.getImage('office'), false ).
            setAlpha(0.5).
            setRotation(Math.PI * 2).
            setLocation(128, 128);
        scene.addChild(office);

        var factory = new CAAT.Actor().
            setBackgroundImage(director.getImage('factory'), false ).
            setLocation(128, 256);
        scene.addChild(factory);

    };

    var img = new CAAT.ImagePreloader().loadImages(imgfiles,callback_imgloaded);

    // start the animation loop
    CAAT.loop(1);
}
  
