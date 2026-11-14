# SQL - More queries

This directory contains SQL scripts that cover MySQL user privileges, table constraints (`NOT NULL`, `DEFAULT`, `UNIQUE`, `PRIMARY KEY`, `FOREIGN KEY`), subqueries, and `JOIN`s.

Scripts that take a database name are run like this:

```
cat <script>.sql | mysql -hlocalhost -uroot -p <database>
```

## Files

| File | Description |
| --- | --- |
| `0-privileges.sql` | Lists all privileges of the MySQL users `user_0d_1` and `user_0d_2` on localhost |
| `1-create_user.sql` | Creates the user `user_0d_1` with all privileges and the password `user_0d_1_pwd` |
| `2-create_read_user.sql` | Creates the database `hbtn_0d_2` and the user `user_0d_2` with only `SELECT` on it |
| `3-force_name.sql` | Creates the table `force_name` (`name` can't be null) |
| `4-never_empty.sql` | Creates the table `id_not_null` (`id` defaults to 1) |
| `5-unique_id.sql` | Creates the table `unique_id` (`id` defaults to 1 and is unique) |
| `6-states.sql` | Creates the database `hbtn_0d_usa` and the table `states` |
| `7-cities.sql` | Creates the table `cities` with a foreign key to `states` |
| `8-cities_of_california_subquery.sql` | Lists the cities of California using a subquery (no `JOIN`) |
| `9-cities_by_state_join.sql` | Lists all cities with their state name |
| `10-genre_id_by_show.sql` | Lists shows that have at least one genre linked |
| `11-genre_id_all_shows.sql` | Lists all shows with their genre id (`NULL` if none) |
| `12-no_genre.sql` | Lists shows without a genre linked |
| `13-count_shows_by_genre.sql` | Lists genres with the number of shows linked to each |
| `14-my_genres.sql` | Lists all genres of the show Dexter |
| `15-comedy_only.sql` | Lists all Comedy shows |
| `16-shows_by_genre.sql` | Lists all shows and their genres (`NULL` if none) |
