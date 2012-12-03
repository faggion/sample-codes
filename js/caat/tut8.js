function (){
    //var dbg = { "log":function(mes){} };
    var dbg = {
        "dom":document.getElementById('dbg'),
        "log":function(mes){
            this.dom.innerHTML = (new Date()) + ": " + mes + "\n" + this.dom.innerHTML;
        }
    };

    var director = new CAAT.Director().initialize(
        300,
        300,
        document.getElementById('_c1')
    );

    var scene = director.createScene();
    var bg = new CAAT.ActorContainer().
        setBounds(0,0,director.width,director.height).
        setFillStyle('#eee');// ここで背景色設定
        scene.addChild(bg);

    var flg     = false;
    var timerid = null;
    var clear   = function(event){
        if(flg || timerid) dbg.log("ended");
        //dbg.log("ended");

        if(flg){
            flg = false;
        }
        if(timerid){
            clearTimeout(timerid); timerid = null;
        }
    };

    bg.mouseDown = function(event){
        flg = true;
        dbg.log("started");
        timerid = setTimeout(clear, 3000);
    };
    bg.mouseUp   = clear;
    bg.mouseDrag = function(event){
        if(flg){
            var square = new CAAT.ShapeActor().
                setFillStyle('#ff0000').
                setShape(1).
                setLocation(parseInt(event.x/50)*50, parseInt(event.y/50)*50).
                setSize(50,50).
                setDiscardable(true).
                enableEvents(false).
                addBehavior(
                    new CAAT.AlphaBehavior().
                        setFrameTime(scene.time, 1000).
                        setValues(0.8, 0 ));
            bg.addChild(square);
        }
    };

    // start the animation loop
    CAAT.loop(32);
}