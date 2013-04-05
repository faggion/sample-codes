display.setStatusBar( display.HiddenStatusBar )

local storyboard = require "storyboard"
local widget = require "widget"

storyboard.gotoScene( "scene1" )

local tabButtons =
{
   { label="First", defaultFile="icon1.png", overFile="icon1.png",
     width=38, height=38, size=12, selected=true,
     labelColor = { default={255, 255, 255, 80}, over={255, 255, 255} },
     onPress=function() storyboard.gotoScene( "scene1" ); end },
   { label="Second", defaultFile="icon2.png", overFile="icon2.png",
     width=38, height=38, size=12, selected=false,
     labelColor = { default={255, 255, 255, 80}, over={255, 255, 255} },
     onPress=function() storyboard.gotoScene( "scene2" ); end },
}
local tabBar = widget.newTabBar {
   left = 0,
   top = display.contentHeight - 50,
   buttons = tabButtons
}
