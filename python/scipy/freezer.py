# coding: utf8
import logging, ols, numpy, sys, re

#data = numpy.random.randn(100,5)
#print data

def main():
    r = re.compile(r'\s{1,}')
    data = []
    for line in sys.stdin:
        d = map(int, r.split(line.rstrip()))
        if len(d) == 7:
            data.append(d)
    ary = numpy.array(data)
    y = ary[:,0]
    x = ary[:,1:3]
    model = ols.ols(y, x, 'y', ['x1', 'x2'])
    #model = ols.ols(y, x, 'y', ['x1', 'x2', 'x3', 'x4', 'x5', 'x6'])
    model.summary()

if __name__ == '__main__':
    logging.getLogger().setLevel(logging.DEBUG)
    logging.debug("OK")
    main()
