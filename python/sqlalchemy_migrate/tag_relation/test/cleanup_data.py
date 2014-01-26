# coding: utf-8

import logging, sys, os
import models
from sqlalchemy.orm import sessionmaker, relationship

def main():
    Session = sessionmaker(bind=models.engine)
    session = Session()

    for tbl in reversed(models.Base.metadata.sorted_tables):
        models.engine.execute(tbl.delete())

    session.commit()
    session.close()

if __name__ == '__main__':
    logging.getLogger().setLevel(logging.DEBUG)
    main()
