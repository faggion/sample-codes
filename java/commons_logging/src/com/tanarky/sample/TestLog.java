package com.tanarky.sample;

import org.apache.commons.logging.Log;
import org.apache.commons.logging.LogFactory;

public class TestLog {
    public static void main(String[] args){
        Log log = LogFactory.getLog(TestLog.class);
        
        log.debug("It's debug log");
        log.info("It's info log");
        log.warn("It's warn log");
        log.error("It's error log");
        log.fatal("It's fatal log");
    }
}