package com.tanarky.sample;

import junit.framework.Test;
import junit.framework.TestCase;
import junit.framework.TestSuite;

import java.io.*;
import java.util.regex.*;

import com.tanarky.sample.TestJe1;
import com.tanarky.sample.TestJe2;

/**
 * Unit test for simple App.
 */
public class AppTest 
    extends TestCase
{
    /**
     * Create the test case
     *
     * @param testName name of the test case
     */
    public AppTest( String testName )
    {
        super( testName );
    }

    /**
     * @return the suite of tests being tested
     */
    public static Test suite()
    {
        return new TestSuite( AppTest.class );
    }

    /**
     * Rigourous Test :-)
     */
    public void testJe()
    {
        String argv[] = {"/tmp/tree",};
        TestJe1.main(argv);
        TestJe2.main(argv);
        return;
    }
}
