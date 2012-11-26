function (){
    var imgfiles = [
        {id:'sprite', url:'./img/3d_tiles.png'}
    ];
    var callback_imgloaded = function( counter, images ) {
        var map = [
            [  16, 16, 16, 16, 16, 16],
            [  23, 23, 23, 23, 23, 23],
            [  19, 23,  8, 23, 23, 23],
            [  19, 23, 23, 23, 23, 23],
            [  19, 23, 23, 23,  6,  7],
            [   7,  3,  2,  1,  0,  0],
        ];
        var len = 6;

        // create a director object
        var director = new CAAT.Director().initialize(
            len*64,
            len*32+32,
            document.getElementById('_c1')
        );
        director.setImagesCache(images);

        var scene = director.createScene();

        var bg = new CAAT.ActorContainer().
            setBounds(0,0,director.width,director.height).
            setFillStyle('#aaa');// ここで背景色設定
        scene.addChild(bg);

        var sprite = new CAAT.SpriteImage().
            initialize(director.getImage('sprite'), 6, 4);

        for(var y=0; y<len; y++){
            for(var x=0; x<len; x++){
                var index = map[y][x];
                //var index = 0;
                var locX  = 32*(x+len-1-y);
                var locY  = 16*(x+y);
                if(index < 0){
                    locY += 5;
                }

                var tiles = new CAAT.Actor().
                    setBackgroundImage(sprite.getRef(), true ).
                    setSpriteIndex(index).
                    setLocation(locX, locY);
                scene.addChild(tiles);
            }
        }
    };

    var img = new CAAT.ImagePreloader().loadImages(imgfiles,callback_imgloaded);

    // start the animation loop
    CAAT.loop(1);
}