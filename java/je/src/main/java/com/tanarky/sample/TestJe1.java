package com.tanarky.sample;

import java.io.File;
import java.io.FileNotFoundException;

import com.sleepycat.bind.tuple.IntegerBinding;
import com.sleepycat.je.Cursor;
import com.sleepycat.je.Database;
import com.sleepycat.je.DatabaseConfig;
import com.sleepycat.je.DatabaseEntry;
import com.sleepycat.je.DatabaseException;
import com.sleepycat.je.Environment;
import com.sleepycat.je.EnvironmentConfig;
import com.sleepycat.je.LockMode;
import com.sleepycat.je.OperationStatus;
import com.sleepycat.je.Transaction;

public class TestJe1 {
    private static final int EXIT_SUCCESS = 0;
    private static final int EXIT_FAILURE = 1;

    public static void main(String argv[]) {
        try {
            File envDir = new File("/tmp");
            EnvironmentConfig envConfig = new EnvironmentConfig();
            envConfig.setTransactional(true);
            envConfig.setAllowCreate(true);
            Environment exampleEnv = new Environment(envDir, envConfig);

            Transaction txn = exampleEnv.beginTransaction(null, null);
            DatabaseConfig dbConfig = new DatabaseConfig();
            dbConfig.setTransactional(true);
            dbConfig.setAllowCreate(true);
            dbConfig.setSortedDuplicates(true);
            Database exampleDb = exampleEnv.openDatabase(txn,
                                                         "testDb",
                                                         dbConfig);
            txn.commit();

            DatabaseEntry keyEntry = new DatabaseEntry();
            DatabaseEntry dataEntry = new DatabaseEntry();

            // put data
            for (int i = 0; i < 10; i++) {
                txn = exampleEnv.beginTransaction(null, null);
                IntegerBinding.intToEntry(i, keyEntry);
                IntegerBinding.intToEntry(i+1, dataEntry);
                OperationStatus status = exampleDb.put(txn, keyEntry, dataEntry);
                if (status != OperationStatus.SUCCESS) {
                    throw new RuntimeException("Data insertion got status " + status);
                }
                txn.commit();
            }

            // get

            Cursor cursor = exampleDb.openCursor(null, null);
            while (cursor.getNext(keyEntry, dataEntry, LockMode.DEFAULT) == OperationStatus.SUCCESS) {
                System.out.println("key=" +
                                   IntegerBinding.entryToInt(keyEntry) +
                                   ", data=" +
                                   IntegerBinding.entryToInt(dataEntry));

            }
            cursor.close();
            exampleDb.close();
            exampleEnv.close();

        } catch (DatabaseException e) {
            e.printStackTrace();
            return;
        }
        return;
    }
}
