#include <string.h>
#include <sstream>
#include <iostream>
#include <stdlib.h>
 
#include "Cassandra.h"
 
#include <protocol/TBinaryProtocol.h>
#include <transport/TSocket.h>
#include <transport/TTransportUtils.h>
 
using namespace std;
using namespace apache::thrift;
using namespace apache::thrift::protocol;
using namespace apache::thrift::transport;
using namespace org::apache::cassandra;
using namespace boost;
 
static string host("127.0.0.1");
static int port= 9160;
 
int main()
{
    shared_ptr<TTransport> socket(new TSocket(host, port));
    shared_ptr<TTransport> transport(new TBufferedTransport(socket));
    shared_ptr<TProtocol> protocol(new TBinaryProtocol(transport));
    CassandraClient client(protocol);
 
  try
      {
          transport->open();
 
          ColumnPath new_col;
          new_col.__isset.column = true; /* this is required! */
          new_col.column_family.assign("Standard1");
          new_col.super_column.assign("");
          new_col.column.assign("title");

          ColumnOrSuperColumn ret_val;
          client.get(ret_val,
                     "Keyspace1",
                     "book1",
                     new_col,
                     ONE);
          printf("Column name retrieved is: %s\n", ret_val.column.name.c_str());
          printf("Value in column retrieved is: %s\n", ret_val.column.value.c_str());
 
          transport->close();
      }
  catch (InvalidRequestException &re)
      {
          printf("ERROR: %s\n", re.why.c_str());
      }
  catch (TException &tx)
      {
          printf("ERROR: %s\n", tx.what());
      }
}

