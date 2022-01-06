# wawa-db

Wawa database and web scraper tools that will back a gas price index API.

## What is in this repo?

This repository will contain ```SQLAlchemy``` models and accomanying web-scraper scripts to build out a Wawa gas price database. These scripts will be used to update the prices as needed.

## Dependencies

- PostgreSQL & PostGIS extension 
- Python 3

```bash
pip3 install -r requirements.txt
```

## Database Initialization

```bash
./db-init.py -e "postgresql://user:password@host:port/database" --echo
```

## Loading/Updating Gas Prices

**UNDER CONSTRUCTION**