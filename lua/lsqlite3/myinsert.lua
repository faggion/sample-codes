
local sqlite3 = require("lsqlite3")

local db = sqlite3.open_memory()

print(db:isopen())

db:exec("CREATE TABLE test (id INTEGER PRIMARY KEY autoincrement, content);")

db:exec("begin")
db:exec("INSERT INTO test VALUES (NULL, 'Hello World');")
print(db:last_insert_rowid())
db:exec("INSERT INTO test VALUES (NULL, 'Hello Lua');")
print(db:last_insert_rowid())
db:exec("INSERT INTO test VALUES (NULL, 'Hello Sqlite3')")
print(db:last_insert_rowid())
--db:exec("commit")
db:exec("rollback")

db:exec[[
      INSERT INTO test VALUES (NULL, 'Hello tanarky');
      INSERT INTO test VALUES (NULL, 'Hello satoshi'); /* foo bar */
      INSERT INTO test VALUES (NULL, 'Hello tanaka');  /* foo bar */
]]

for row in db:nrows("SELECT * FROM test") do
  print(row.id, row.content)
end
