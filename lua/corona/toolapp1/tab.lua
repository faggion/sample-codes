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
      { label="Browse", defaultFile="imgs/34.png", overFile="imgs/34.png",
        width=32, height=32, size=12,
        labelColor = { default={255, 255, 255, 80}, over={255, 255, 255} },
        onPress=function() storyboard.gotoScene( "scene2" ); end },
      { label="Config", defaultFile="imgs/53.png", overFile="imgs/53.png",
        width=38, height=38, size=12,
        labelColor = { default={255, 255, 255, 80}, over={255, 255, 255} },
        onPress=function() storyboard.gotoScene( "scene3" ); end },
   }
}

function Tab:setSelectedButton(tabnum)
   for i=1, #self.buttons do
      if i == tabnum then
         self.buttons[i].selected = true
      else
         self.buttons[i].selected = false
      end
   end
end

return Tab

--end

