.PHONY: all

ECHO = /bin/echo

all:
# 文字列として一致するか
ifeq ($(ECHO),/bin/echo)
	echo 'ifeq ECHO == /bin/echo'
else
	echo 'ifeq ECHO != /bin/echo'
endif

# 空白文字列が混入しやすいので
# 以下のように書くと堅牢
ifeq "$(ECHO)" "/bin/echo"
	echo 'ifeq ECHO == /bin/echo'
endif
