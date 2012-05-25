import java.io.File;
import java.io.FileNotFoundException;
import kyotocabinet.DB;

public class TestKc {
    public static void main(String argv[]) {
        try {
            DB db = new DB();

            // データベースを開く
            if(!db.open("/tmp/test.tdb", DB.OWRITER | DB.OCREATE)){
                System.err.println("open error: " + db.error());
            }

            // レコードを格納する
            if(!db.set("foo", "hop")){
                System.err.println("set error: " + db.error());
            }
            
            // レコードを取得する
            String value = db.get("foo");
            if(value != null){
                System.out.println(value);
            } else {
                System.err.println("get error: " + db.error());
            }
            
            // データベースを閉じる
            if(!db.close()){
                System.err.println("close error: " + db.error());
            }
        }
        catch (UnsatisfiedLinkError e) {
            e.printStackTrace();
        }
        return;
    }
}
