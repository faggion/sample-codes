package com.tanarky.sample;

import java.io.File;
import java.io.FileNotFoundException;

import com.tanarky.sample.Cdb;

public class TestJe1 {
    public static void main(String argv[]) {
        try {
            //Cdb cdb = new Cdb("/tmp/t.cdb");
            Cdb cdb = new Cdb("/tmp/my.tcdb");

            System.out.println(new String(cdb.find("key1".getBytes("utf-8")), "utf-8"));
            System.out.println(new String(cdb.find("key2".getBytes("utf-8")), "utf-8"));
            System.out.println(new String(cdb.find("key3".getBytes("utf-8")), "utf-8"));

            cdb.close();
            System.out.println("Finished normally.");
        }
        catch(Exception e) {
            e.printStackTrace();
        }
        finally {
        }
        return;
    }
}
