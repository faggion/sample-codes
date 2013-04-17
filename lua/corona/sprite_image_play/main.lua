--display.setStatusBar( display.HiddenStatusBar )

local bg = display.newRect(0,0,320,480)
bg:setFillColor(255,255,255)

local sheet_data = {
   width=280,
   height=385,
   numFrames=10,
   sheetContentWidth=1400, sheetContentHeight=770
}
local imgsheet1 = graphics.newImageSheet( "imgs/run.png", sheet_data )
local sequence = {
   name="run",
   start=1,
   --frames= { 1,2,3,4,5,6,7,8,9,10 },
   count=10,
   time=300,
   loopCount=0,
   loopDirection="forward"
}
local imgs1 = display.newSprite(imgsheet1, sequence)
imgs1.x = display.contentWidth/2
imgs1.y = display.contentHeight/2
imgs1:play()



