package {
    import flash.display.*;
    import flash.text.*;
    import flash.net.*;
    import flash.events.*;

    [SWF(width="200", height="50", backgroundColor="0xFFCC00", frameRate="24")]

    public class LinkUrl extends Sprite {
        public function LinkUrl() {
            var textFormat:TextFormat = new TextFormat()
            textFormat.size = 10;
            var textField:TextField   = new TextField();
            textField.defaultTextFormat = textFormat;
            textField.text   = "Yahoo!ショッピング";
            textField.width  = 200;
            textField.height = 50;

            textField.addEventListener(MouseEvent.CLICK, this.gotolink);
            addChild(textField);
        }

        public function gotolink(event:MouseEvent):void {
            var goURL:URLRequest = new URLRequest("http://atq.ck.valuecommerce.com/servlet/atq/referral?sid=2219441&pid=877935733&vcptn=shpg%2Fp%2FNqNP7flCUN49xU3KOQg-&vc_url=http%3A%2F%2Fshopping.yahoo.co.jp%2F");
            navigateToURL(goURL, "_new");
        }
    }
}