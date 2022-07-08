psql meretry -c "GRANT ALL ON ALL TABLES IN SCHEMA public to meretryuser;"
psql meretry -c "GRANT ALL ON ALL SEQUENCES IN SCHEMA public to meretryuser;"
psql meretry -c "GRANT ALL ON ALL FUNCTIONS IN SCHEMA public to meretryuser;"