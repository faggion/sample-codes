function (){
    var imgfiles = [
        {id:'sprite', url:'./img/chars.png'}
    ];
    var callback_imgloaded = function( counter, images ) {
        //var len = map[0].length;
        // create a director object
        var director = new CAAT.Director().initialize(
            300,
            300,
            document.getElementById('_c1')
        );
        director.setImagesCache(images);

        var scene = director.createScene();
        var bg = new CAAT.ActorContainer().
            setBounds(0,0,director.width,director.height).
            setFillStyle('#eee');// ここで背景色設定
        scene.addChild(bg);

        var sprite= new CAAT.SpriteImage().
            initialize(director.getImage('sprite'), 8, 12);

        var tiles = new CAAT.Actor().
            setBackgroundImage(sprite.getRef(), true ).
            setAnimationImageIndex( [2,1,0,1] ).
            setChangeFPS( 200 ).
            setLocation(30, 30);
        scene.addChild(tiles);
    };

    var img = new CAAT.ImagePreloader().loadImages(imgfiles,callback_imgloaded);

    // start the animation loop
    CAAT.loop(20);
}