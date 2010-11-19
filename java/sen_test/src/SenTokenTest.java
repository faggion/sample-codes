//SenTokenTest.java
package my;

import java.io.StringReader;
import org.apache.lucene.analysis.*;
import org.apache.lucene.analysis.ja.JapaneseAnalyzer;
import org.apache.lucene.analysis.standard.StandardAnalyzer;

public class SenTokenTest {
    public static void main(String[] args) throws Exception {
        Token t;
        JapaneseAnalyzer a = new JapaneseAnalyzer();
        TokenStream ts = a.tokenStream("default", new StringReader("すもももももももものうち。"));
        //StandardAnalyzer a = new StandardAnalyzer();
        //TokenStream ts = a.tokenStream("default", new StringReader("I can fly."));
        while((t = ts.next()) != null) {
            System.out.println(t);
        }
    }
}
