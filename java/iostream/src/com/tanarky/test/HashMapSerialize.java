package com.tanarky.test;

import java.io.FileOutputStream;
import java.io.FileInputStream;
import java.io.ObjectOutputStream;
import java.io.ObjectInputStream;
import java.io.IOException;
import java.lang.Exception;
import java.lang.ClassNotFoundException;
import java.util.HashMap;

public class HashMapSerialize {
    // compile時のcast警告を回避するための策
    // http://www.velocityreviews.com/forums/t499693-how-do-you-prevent-unchecked-cast-warning-when-reading-from-objectinputstream.html
    // 結局、uncheckedにしてるだけなので、あまり意味なし？
    @SuppressWarnings("unchecked")
    public static <T> T readObject(
        java.io.ObjectInputStream in
        ) throws java.io.IOException, java.lang.ClassNotFoundException {
        return (T)in.readObject();
    }
    public static void main(String[] args) {
        try {
            FileOutputStream outFile = new FileOutputStream("/tmp/test.hashmap");
            ObjectOutputStream outObject = new ObjectOutputStream(outFile);
            // データ作成
            HashMap<String,String> mapw = new HashMap<String,String>();
            mapw.put("ringo", "Apple");
            mapw.put("budou", "Grape");
            // データ保存
            outObject.writeObject(mapw);
            outObject.close();
            outFile.close();

            FileInputStream inFile = new FileInputStream("/tmp/test.hashmap");
            ObjectInputStream inObject = new ObjectInputStream(inFile);
            //// 以下だと単純だが、compile時にwarningが出る
            //HashMap<String,String> mapr = (HashMap)inObject.readObject();
            HashMap<String,String> mapr = readObject(inObject);

            // 値取得
            System.out.println(mapr.get("budou"));

            inObject.close();
            inFile.close();
        }
        catch (IOException e) {}
        catch (ClassNotFoundException e) {}
        catch (Exception e) {}
    }
}
