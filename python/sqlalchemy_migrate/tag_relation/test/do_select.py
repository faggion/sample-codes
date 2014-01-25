# coding: utf-8

import logging, sys, os
import models
from sqlalchemy.orm import sessionmaker, relationship

def main():
    Session = sessionmaker(bind=models.engine)
    session = Session()

    a = session.query(models.Article).filter(models.Article.id == 1).one()
    #logging.info(a.tag_sets)
    for ts in a.tag_sets:
        logging.info(ts.value)

    session.close()

if __name__ == '__main__':
    logging.getLogger().setLevel(logging.INFO)
    main()
