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
            // イベントを登録
            myLoader.addEventListener(Event.COMPLETE, this.onComplete);
            myLoader.load(myRequest);
        }

        public function onComplete (eventObject:Event):void {
            // Namespaceの定義
            var ns:Namespace = new Namespace('urn:yahoo:jp:getModule');
            // XMLオブジェクトを作成
            var api:XML      = new XML(eventObject.target.data);
            this.showMessage(api.ns::Result.ns::Hit[0].ns::Title);
        }

        // テキストを表示
        public function showMessage(str:String):void {
            var textFormat:TextFormat = new TextFormat()
            textFormat.size = 10;
            var textField:TextField   = new TextField();
            textField.defaultTextFormat = textFormat;
            textField.text   = str;
            textField.width  = 200;
            textField.height = 50;
            addChild(textField);
        }
    }
}