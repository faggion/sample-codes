import argparse

parser = argparse.ArgumentParser(description='Process some integers.')

parser.add_argument('--foo', '-f', action="store_true", help="foo is True/False option")
parser.add_argument('-b', '--bar', required=True, help="bar is any string option")
parser.add_argument('-c', required=False, help="c is not required option", dest="NAME")
parser.add_argument('baz')
parser.add_argument('-V', '--version', action="version", version="%(prog)s 2.0")

args = parser.parse_args()

print args
print "foo is '%s'" % args.foo
print "c is '%s'" % args.c
print "bar is '%s'" % args.bar
#print args.foo[0]
#print args.integers

