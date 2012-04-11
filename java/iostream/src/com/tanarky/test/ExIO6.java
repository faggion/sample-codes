package com.tanarky.test;

import java.io.*;

public class ExIO6 {
    public static void main(String[] args) {
        try {
            //(2)FileOutputStreamオブジェクトの生成
            FileOutputStream outFile = new FileOutputStream("/tmp/object.txt");
            //(3)ObjectOutputStreamオブジェクトの生成
            ObjectOutputStream outObject = new ObjectOutputStream(outFile);
            //(4)クラスHelloのオブジェクトの書き込み
            outObject.writeObject(new Hello());

            outObject.close();  //(5)オブジェクト出力ストリームのクローズ
            outFile.close();  //(6)ファイル出力ストリームのクローズ

            //(7)FileInputStreamオブジェクトの生成
            FileInputStream inFile = new FileInputStream("/tmp/object.txt");
            //(8)ObjectInputStreamオブジェクトの生成
            ObjectInputStream inObject = new ObjectInputStream(inFile);
            //(9)オブジェクトの読み込み
            Hello exHello = (Hello)inObject.readObject();

            //(10)オブジェクトの実行
            exHello.sayHello();

            inObject.close();  //(11)オブジェクト入力ストリームのクローズ
            inFile.close();  //(12)ファイル入力ストリームのクローズ
        } catch (IOException e) {
        } catch (ClassNotFoundException e) {
        }
    }
}
