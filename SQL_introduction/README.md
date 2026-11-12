# SQL - Introduction

This project covers the basics of SQL and relational databases with MySQL:
creating and dropping databases and tables, inserting, selecting, updating and
deleting records, ordering, filtering and aggregating.

## Usage

Each script is fed to the `mysql` client, and the database name is passed as an
argument when the script works on a table:

```
cat 0-list_databases.sql | mysql -hlocalhost -uroot -p
cat 4-first_table.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
```

## Files

| File | Description |
|------|-------------|
| `0-list_databases.sql` | Lists all databases |
| `1-create_database_if_missing.sql` | Creates `hbtn_0c_0` if missing |
| `2-remove_database.sql` | Drops `hbtn_0c_0` if it exists |
| `3-list_tables.sql` | Lists the tables of a database |
| `4-first_table.sql` | Creates `first_table` if missing |
| `5-full_table.sql` | Prints the full description of `first_table` |
| `6-list_values.sql` | Lists all rows of `first_table` |
| `7-insert_value.sql` | Inserts a row in `first_table` |
| `8-count_89.sql` | Counts records with `id = 89` |
| `9-full_creation.sql` | Creates `second_table` and adds rows |
| `10-top_score.sql` | Lists score and name, top score first |
| `11-best_score.sql` | Lists records with a score of at least 10 |
| `12-no_cheating.sql` | Updates Bob's score to 10 by name |
| `13-change_class.sql` | Removes records with a score of 5 or less |
| `14-average.sql` | Computes the average score |
| `15-groups.sql` | Counts records per score |
| `16-no_link.sql` | Lists records that have a name |

## Author

ilatonia
