package com.tanarky.sample;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.regex.*;

public class TestJe1 {
    public static void main(String argv[]) {
        try {
            Pattern cookieFormat = Pattern.compile("([0-9a-z_]*)=([^;]*)");
            String raw = new String("dspuid_4=KsAsPrIBkQnuyVJs; dspuid_3=fa3d9251-0e06-4378-9d54-9bdbfc59fa15; dspuid_5=UOsB.LTWMEwAATYzSE4AAAAA; adlantis_pc_uuid=9c720259-6e39-4d3d-8bf7-45730feb3d73; adlantis_sp_uuid=m13rwgld13");
            Matcher m = cookieFormat.matcher(raw);
            while(m.find()){
                //System.out.println(m.groupCount());
                System.out.println(m.group(1) + " -> " + m.group(2));
            }
        }
        catch(Exception e) {
            e.printStackTrace();
        }
        finally {
        }
        return;
    }
}
