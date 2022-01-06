#!/usr/bin/env python3
import argparse 
import os
from sqlalchemy import create_engine
from models import Base

def with_args(f):
    def with_args_(*args, **kwargs):
        ap = argparse.ArgumentParser(description="Initialize the Wawa gas price database.")
        ap.add_argument("-e", "--engine-string", default=os.getenv("pg_engine"), help="PostgreSQL engine string.", type=str)
        ap.add_argument("--echo", action="store_true", default=False, help="If specified, will turn echo=True for the database engine.")
        return f(ap.parse_args(), *args, **kwargs)
    return with_args_

@with_args
def main(cmd_line):
    engine = create_engine(cmd_line.engine_string, echo=cmd_line.echo)
    engine.execute("CREATE SCHEMA IF NOT EXISTS wawamgr")
    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    main()
