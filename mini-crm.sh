#!/bin/bash

psql $DATABASE_URL < sql/0.sql
psql $DATABASE_URL < sql/1.sql
psql $DATABASE_URL < sql/2.sql
psql $DATABASE_URL < sql/3.sql

python ./mini-crm.py
