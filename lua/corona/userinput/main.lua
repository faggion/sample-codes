local usernameField, passwordField, submitButton

local widget = require( "widget" )

local function onUsername( self, event )
   print(event.phase)
   if ( "began" == event.phase ) then
        -- Note: this is the "keyboard appearing" event
        -- In some cases you may want to adjust the interface while the keyboard is open.

   elseif ( "submitted" == event.phase ) then
      -- Automatically tab to password field if user clicks "Return" on iPhone keyboard (convenient!)
      native.setKeyboardFocus( passwordField )
   end
end

local function onPassword( self, event )
    -- Hide keyboard when the user clicks "Return" in this field
   if ( "submitted" == event.phase ) then
      native.setKeyboardFocus( nil )
   end
end

usernameField = native.newTextField( 50, 150, 220, 36 )
usernameField.userInput = onUsername
usernameField.font = native.newFont( native.systemFontBold, 24 )
usernameField.text = ""
usernameField:addEventListener("userInput")
--usernameField:setTextColor( 51, 51, 122, 255 )

passwordField = native.newTextField( 50, 210, 220, 36 )
passwordField.userInput = onPassword
passwordField.font = native.newFont( native.systemFontBold, 24 )
passwordField.text = ""
passwordField.isSecure = true
passwordField:addEventListener("userInput")
passwordField:setTextColor( 51, 51, 122, 255 )

local onSubmit = function()
   if usernameField.text == "" then
      print("empty username")
      native.setKeyboardFocus( usernameField )
   elseif passwordField.text == "" then
      print("empty password")
      native.setKeyboardFocus( passwordField )
   else
      print("[OK] username: " .. usernameField.text .. " , password: " .. passwordField.text)
   end
end
local myButton = widget.newButton
{
    left = 50,
    top = 270,
    width = 220,
    height = 36,
    id = "button_1",
    label = "Submit",
    onRelease = onSubmit,
}
