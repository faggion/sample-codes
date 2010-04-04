package {
    import flash.display.*;
    import flash.text.*;

    [SWF(width="200", height="50", backgroundColor="0xFFCC00", frameRate="24")]
    public class HelloWorld extends Sprite {
        public function HelloWorld() {
            var textField:TextField = new TextField();
            textField.text = "はろー, World!";
            addChild(textField);
        }
    }
}