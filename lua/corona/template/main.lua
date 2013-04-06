display.setStatusBar( display.HiddenStatusBar )

local storyboard = require "storyboard"
local widget = require "widget"

storyboard.gotoScene( "scene1" )

local tabButtons =
{
   { label="Home", defaultFile="1.png", overFile="1.png",
     width=32, height=32, size=12, selected=true,
     labelColor = { default={255, 255, 255, 80}, over={255, 255, 255} },
     onPress=function() storyboard.gotoScene( "scene2" ); end },

   { label="Browse", defaultFile="34.png", overFile="34.png",
     width=32, height=32, size=12, selected=false,
     labelColor = { default={255, 255, 255, 80}, over={255, 255, 255} },
     onPress=function() storyboard.gotoScene( "scene1" ); end },

   { label="Config", defaultFile="53.png", overFile="53.png",
     width=38, height=38, size=12, selected=false,
     labelColor = { default={255, 255, 255, 80}, over={255, 255, 255} },
     onPress=function() storyboard.gotoScene( "scene2" ); end },
}
local tabBar = widget.newTabBar {
   left = 0,
   top = display.contentHeight - 50,
   buttons = tabButtons
}
