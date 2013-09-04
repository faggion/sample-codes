# coding: utf8
import logging, ols, numpy, sys, re, traceback

#data = numpy.random.randn(100,5)
#print data

def main():
    r = re.compile(r'\s{1,}')
    data  = []
    label = []
    for line in sys.stdin:
        d = map(float, r.split(line.rstrip()))
        if not label:
            for i in range(len(d) - 1):
                label.append('x%d' % (i + 1))
        elif 1 < len(d) and len(label) != len(d) - 1:
            raise BaseException
        data.append(d)

    ary = numpy.array(data)
    y = ary[:,0]
    #x = ary[:,1:3]
    #x = ary[:,1:]
    #x = ary[:,1:6]
    #x = ary[:,1:4]
    x = ary[:,1:]
    model = ols.ols(y, x, 'y', label)
    model.summary()

if __name__ == '__main__':
    logging.getLogger().setLevel(logging.DEBUG)
    logging.debug("OK")
    try:
        main()
    except:
        logging.error(traceback.format_exc())
