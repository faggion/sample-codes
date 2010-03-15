<?php
$GLOBALS['THRIFT_ROOT'] = '/usr/share/php/Thrift';
require_once $GLOBALS['THRIFT_ROOT'].'/packages/cassandra/Cassandra.php';
require_once $GLOBALS['THRIFT_ROOT'].'/packages/cassandra/cassandra_types.php';
require_once $GLOBALS['THRIFT_ROOT'].'/transport/TSocket.php';
require_once $GLOBALS['THRIFT_ROOT'].'/protocol/TBinaryProtocol.php';
require_once $GLOBALS['THRIFT_ROOT'].'/transport/TFramedTransport.php';
require_once $GLOBALS['THRIFT_ROOT'].'/transport/TBufferedTransport.php';

try {
    // Make a connection to the Thrift interface to Cassandra
    $socket    = new TSocket('127.0.0.1', 9160);
    $transport = new TBufferedTransport($socket, 1024, 1024);
    $protocol  = new TBinaryProtocolAccelerated($transport);
    $client    = new CassandraClient($protocol);
    $transport->open();

    // Specify what Column Family to query against.
    $columnParent = new cassandra_ColumnParent();
    $columnParent->column_family = "Super1";
    //$columnParent->super_column = 'fooo';

    $keyRange = new cassandra_KeyRange();
    $keyRange->start_key = "";
    $keyRange->end_key   = "";
    //$keyRange->count   = 1;

    $predicate  = new cassandra_SlicePredicate();
    //$sliceRange = new cassandra_SliceRange();
    //$sliceRange->start  = "";
    //$sliceRange->finish = "";
    //$predicate->slice_range = $sliceRange;
    $predicate->column_names = array('aa'); // 存在しないcolumn_nameを指定するとkeyだけとれる

    $result = $client->get_range_slices('Keyspace1', $columnParent, $predicate, $keyRange, cassandra_ConsistencyLevel::ONE);

    print_r($result);
    $transport->close();
}
catch (TException $tx) {
    print 'TException: '.$tx->why. ' Error: '.$tx->getMessage() . "\n";
}
