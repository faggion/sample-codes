package my;

import java.io.StringReader;
import java.util.Iterator;

import org.apache.lucene.analysis.*;
import org.apache.lucene.analysis.standard.StandardAnalyzer;
import org.apache.lucene.util.Version;

import org.apache.lucene.analysis.cjk.CJKAnalyzer;

public class TestSA {
    public static void main(String[] args) throws Exception {
        Token t;
        //StandardAnalyzer a = new StandardAnalyzer(Version.LUCENE_CURRENT);
        CJKAnalyzer a = new CJKAnalyzer(Version.LUCENE_CURRENT);
        System.out.println(a.getClass());
        TokenStream ts = a.tokenStream("default",
                                       new StringReader("オプションを指定して再コンパイルしてください。"));

        while(ts.incrementToken()){
            System.out.println(ts.toString());
            //System.out.println(ts.STOP_WORDS);
        }
    }
}
