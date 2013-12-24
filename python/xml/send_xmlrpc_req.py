# coding: utf-8
import logging,sys,os,traceback
import xmlrpclib

def main():
    cli = xmlrpclib.ServerProxy('http://localhost:5000/api')
    #print cli.ping({'name':'foo', 'test':True})
    print cli.ping({'name':'foo'}, 'or')

if __name__ == '__main__':
    main()
