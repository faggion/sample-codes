--do

local storyboard = require( "storyboard" )
local Tab = {
   left    = 0,
   top     = display.contentHeight - 50,
   buttons = {
      { label="Home", defaultFile="imgs/1.png", overFile="imgs/1.png",
        width=32, height=32, size=12,
        labelColor = { default={255, 255, 255, 80}, over={255, 255, 255} },
        onPress=function() storyboard.gotoScene( "scene1" ); end },
      { label="Execute", defaultFile="imgs/execute.png", overFile="imgs/execute.png",
        width=32, height=32, size=12,
        labelColor = { default={255, 255, 255, 80}, over={255, 255, 255} },
        onPress=function() storyboard.gotoScene( "scene2" ); end },
      { label="Config", defaultFile="imgs/53.png", overFile="imgs/53.png",
        width=38, height=38, size=12,
        labelColor = { default={255, 255, 255, 80}, over={255, 255, 255} },
        onPress=function() storyboard.gotoScene( "scene3" ); end },
   }
}
return Tab

--end

