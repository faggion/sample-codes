display.setStatusBar( display.HiddenStatusBar )

local bg = display.newRect(0,0,480,320)
bg:setFillColor(255,255,255)

local blockx = 80
local blocky = 80
local myObject = display.newRect( 0, 0, blockx, blocky )
myObject:setFillColor( 255,0,0,80 )
 
-- touch listener function
function myObject:touch( event )
   if event.phase == "began" then
      self:setFillColor(255,0,0)
      self.markX = self.x -- store x location of object
      self.markY = self.y -- store y location of object
   elseif event.phase == "moved" then
      local x = (event.x - event.xStart) + self.markX
      local y = (event.y - event.yStart) + self.markY
      self.x, self.y = x, y -- move object based on calculations above

   -- ended phaseが呼ばれない場合があるので、この実装は良くない
   elseif event.phase == "ended" then
      self:setFillColor(255,0,0,80)
      print(self.x)
      print(self.y)
      local x = math.floor(self.x / blockx) * blockx + 40
      local y = math.floor(self.y / blocky) * blocky + 40 
      print(x)
      print(y)
      self.x, self.y = x, y -- move object based on calculations above
   end
   return true
end
 
-- make 'myObject' listen for touch events
myObject:addEventListener( "touch", myObject )
