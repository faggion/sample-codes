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

        var locX  = 32;
        var locY  = 48;
        var dir   = 2;
        var tiles = new CAAT.Actor().
            setBackgroundImage(sprite.getRef(), true ).
            setAnimationImageIndex( [2,1,0,1] ).
            setChangeFPS( 200 ).
            setLocation(locX, locY);
        scene.addChild(tiles);

        CAAT.registerKeyListener( function(key) {
            console.debug(key);
            if(key.action !== 'down') return;
            // up
            if ( key.keyCode==40) {
                if(dir !== 1){
                    dir = 1;
                    tiles.setAnimationImageIndex( [2,1,0,1] );
                }
                locY += 48/2;
                tiles.setLocation(locX, locY);
            }
            // down
            else if ( key.keyCode==38) {
                if(dir !== 2){
                    dir = 2;
                    tiles.setAnimationImageIndex([38,37,36,37]);
                }
                locY -= 48/2;
                tiles.setLocation(locX, locY);
            }
            // right
            else if ( key.keyCode==39 ) {
                if(dir !== 3){
                    dir = 3;
                    tiles.setAnimationImageIndex([26,25,24,25]);
                }
                locX += 32/2;
                tiles.setLocation(locX, locY);
            }
            // left
            else if ( key.keyCode==37 ) {
                if(dir !== 4){
                    dir = 4;
                    tiles.setAnimationImageIndex([14,13,12,13]);
                }
                locX -= 32/2;
                tiles.setLocation(locX, locY);
            }
        });
    };

    var img = new CAAT.ImagePreloader().loadImages(imgfiles,callback_imgloaded);

    // start the animation loop
    CAAT.loop(32);
}