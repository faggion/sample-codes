module("message", package.seeall)

function show(text)
   local bg = display.newRoundedRect(display.contentWidth/2,
                                     display.contentHeight-200/2,
                                     display.contentWidth-10,
                                     200-10,
                                     5)
   bg:setFillColor(0.2, 0.2, 0.2)
   bg.setStrokeColor = {0.3,0,0}
   bg.strokeWidth = 3

   local title = display.newText(text,
                                 display.contentWidth/2,
                                 display.contentHeight-200/2,
                                 display.contentWidth - 20,
                                 200 - 20,
                                 "PixelMplus10-Regular",
                                 20)
   title:setFillColor(0.8,0.8,0.8)

   Runtime:addEventListener( "touch", _show_next_message )
   --storyboard.gotoScene(next)
end

function _show_next_message(event)
   if ( event.phase == "ended" ) then
      native.showAlert( "Corona",
                        "Dream. Build. Ship.",
                        { "OK", "Learn More" },
                        nil)
   end
end