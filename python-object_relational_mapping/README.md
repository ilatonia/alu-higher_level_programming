# python-object_relational_mapping

This directory contains scripts that connect Python to a MySQL server. The first part uses the `MySQLdb` module with raw SQL queries, including a demonstration of SQL injection and how to prevent it. The second part uses the `SQLAlchemy` ORM to map Python classes to tables.

## Requirements

- Python 3, interpreted on Ubuntu 20.04 LTS
- MySQL server running on `localhost` at port `3306`
- Modules: `MySQLdb` (mysqlclient) and `SQLAlchemy`
- Code follows the `pycodestyle` (PEP 8) style
- All files are executable and start with `#!/usr/bin/python3`
- Every module has a docstring
- Scripts do not run when imported

## Files

| File | Description |
| --- | --- |
| `0-select_states.py` | Lists all states from `hbtn_0e_0_usa`, sorted by `states.id` |
| `1-filter_states.py` | Lists all states whose name starts with `N` |
| `2-my_filter_states.py` | Displays the states matching the name argument (query built with `format`, vulnerable to SQL injection) |
| `3-my_safe_filter_states.py` | Same as above, but safe from SQL injection |
| `4-cities_by_state.py` | Lists all cities from `hbtn_0e_4_usa` with their state, using a single `execute()` |
| `5-filter_cities.py` | Lists all cities of the state given as argument, using a single `execute()` |
| `model_state.py` | `State` class and `Base` (`declarative_base()`) linked to the `states` table |
| `7-model_state_fetch_all.py` | Lists all `State` objects from `hbtn_0e_6_usa` |
| `8-model_state_fetch_first.py` | Prints the first `State` object, or `Nothing` if the table is empty |
| `9-model_state_filter_a.py` | Lists all `State` objects whose name contains the letter `a` |
| `10-model_state_my_get.py` | Prints the id of the state matching the name argument, or `Not found` |
| `11-model_state_insert.py` | Adds the state `Louisiana` and prints its new id |
| `12-model_state_update_id_2.py` | Changes the name of the state with `id = 2` to `New Mexico` |
| `13-model_state_delete_a.py` | Deletes all states whose name contains the letter `a` |
| `model_city.py` | `City` class linked to the `cities` table, with a foreign key to `states.id` |
| `14-model_city_fetch_by_state.py` | Prints all `City` objects from `hbtn_0e_14_usa` as `<state name>: (<city id>) <city name>` |

## Usage

The `MySQLdb` scripts take the MySQL username, password and database name as arguments. Scripts that filter by name take the name as a fourth argument.

```bash
./0-select_states.py root root hbtn_0e_0_usa
./3-my_safe_filter_states.py root root hbtn_0e_0_usa 'Arizona'
./7-model_state_fetch_all.py root root hbtn_0e_6_usa
./14-model_city_fetch_by_state.py root root hbtn_0e_14_usa
```
