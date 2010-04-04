package {
    import flash.display.*;
    import flash.text.*;
    import flash.net.*;
    import flash.events.Event;

    [SWF(width="200", height="50", backgroundColor="0xFFCC00", frameRate="24")]

    public class ApiRequest extends Sprite {
        public function ApiRequest() {
            var url:String = "http://shopping.yahooapis.jp/ShoppingWebService/V1/getModule?appid=tanarky_devel&position=hotitem";
            var myLoader:URLLoader   = new URLLoader();
            var myRequest:URLRequest = new URLRequest(url);
            myLoader.addEventListener(Event.COMPLETE, this.onComplete);
            myLoader.load(myRequest);
        }

        public function onComplete (eventObject:Event):void {
            var my_str:String = eventObject.target.data
            this.showMessage(my_str);
        }

        public function showMessage(str:String):void {
            var textField:TextField = new TextField();
            textField.text = str;
            addChild(textField);
        }
    }
}