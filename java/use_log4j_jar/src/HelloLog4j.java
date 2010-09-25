import org.apache.log4j.*;

public class HelloLog4j {
    public static void main(String[] args) {
        // インスタンスの生成
        Logger logger = Logger.getLogger(HelloLog4j.class);
        PropertyConfigurator.configure("./conf/log4j.properties");

        //ログ出力
        logger.info("This is info.");
        logger.warn("This is warn.");
        logger.error("This is error.");
    }
}
