::
   
   % ffmpeg -i mymovie.mov mymovie.mp4
   % ffmpeg -i mymovie.mp4 -vf scale=640:-1 -vb 500k mymovie_640.mp4
   % ffmpeg -i mymovie_640.mp4 -ss 0 -vframes 1 -f image2 poster.jpg
