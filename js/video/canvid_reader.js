var canvidControl = canvid({
    selector : '.video',
    videos: {
        clip1: { src: 'mymovie.jpg',
                 frames: 208,
                 cols: 8,
                 loops: 1,
                 fps: 15,
                 onEnd: function(){
                     //console.log('clip1 ended.');
                     //canvidControl.play('clip2');
                 }
               },
        //clip2: { src: 'clip2.jpg', frames: 43, cols: 6, fps: 24 }
    },
    width: 320,
    height: 180,
    loaded: function() {
        canvidControl.play('clip1');
        // reverse playback
        //canvidControl.play('clip1', true);
    }
});
