package {
    import flash.display.*;
    import flash.text.*;
    import flash.net.*;
    import flash.events.*;

    [SWF(width="256", height="40", backgroundColor="0xffffff", frameRate="24")]

    public class ShowImg extends Sprite {
        public var urlImage:URLRequest;
        public var img:Loader;

        public function ShowImg() {
            urlImage = new URLRequest("http://i.yimg.jp/images/mh/shopping.gif");
            img      = new Loader();

            img.contentLoaderInfo.addEventListener(Event.COMPLETE, this.setSize);
            img.addEventListener(MouseEvent.CLICK, this.gotoLink);
            img.load(urlImage);
        }

        public function setSize(event:Event):void {
            img.width  = 256;
            img.height = 40;
            this.addChild( img );
        };

        public function gotoLink(event:Event):void {
            var goURL:URLRequest = new URLRequest("http://atq.ck.valuecommerce.com/servlet/atq/referral?sid=2219441&pid=877935733&vcptn=shpg%2Fp%2FNqNP7flCUN49xU3KOQg-&vc_url=http%3A%2F%2Fshopping.yahoo.co.jp%2F");
            navigateToURL(goURL, "_new");
        };
    }
}