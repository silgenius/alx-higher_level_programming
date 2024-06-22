# 0x0F. Python - Object-relational Mapping

## Description

Welcome to the 0x0F. Python - Object-relational Mapping (ORM) project repository! This project is designed to introduce you to the concept of Object-relational Mapping, a programming technique used to convert data between incompatible type systems in object-oriented programming languages. You will learn how to interact with databases in Python using ORM, focusing on the SQLAlchemy library.

## Learning Objectives

By the end of this project, you should be able to:

- Understand the concept of ORM and its advantages over direct SQL queries.
- Use SQLAlchemy to connect to and interact with a MySQL database.
- Create and manage database schemas using SQLAlchemy.
- Perform CRUD (Create, Read, Update, Delete) operations using SQLAlchemy.
- Understand and use SQLAlchemy queries to filter and sort data.
- Work with relationships between tables in SQLAlchemy.
- Understand and use SQLAlchemy sessions to manage transactions.

## Project Files

- **0-select_states.py**: Script that lists all states from the database `hbtn_0e_0_usa`.
- **1-filter_states.py**: Script that lists all states with a name starting with `N` from the database `hbtn_0e_0_usa`.
- **2-my_filter_states.py**: Script that takes in an argument and displays all values in the `states` table where `name` matches the argument.
- **3-my_safe_filter_states.py**: Script that takes in an argument and displays all values in the `states` table where `name` matches the argument (safe from SQL injection).
- **4-cities_by_state.py**: Script that lists all cities from the database `hbtn_0e_4_usa`.
- **5-filter_cities.py**: Script that takes in the name of a state as an argument and lists all cities of that state.
- **model_state.py**: Python file that contains the class definition of a `State` and an instance `Base` using SQLAlchemy.
- **6-model_state.py**: Script that adds the `State` object “Louisiana” to the database `hbtn_0e_6_usa`.
- **7-model_state_fetch_all.py**: Script that lists all `State` objects from the database `hbtn_0e_6_usa`.
- **8-model_state_fetch_first.py**: Script that prints the first `State` object from the database `hbtn_0e_6_usa`.
- **9-model_state_filter_a.py**: Script that lists all `State` objects that contain the letter `a` from the database `hbtn_0e_6_usa`.
- **10-model_state_my_get.py**: Script that prints the `State` object with the `name` passed as an argument from the database `hbtn_0e_6_usa`.
- **11-model_state_insert.py**: Script that adds the `State` object “Louisiana” to the database `hbtn_0e_6_usa`.
- **12-model_state_update_id_2.py**: Script that changes the name of a `State` object from the database `hbtn_0e_6_usa`.
- **13-model_state_delete_a.py**: Script that deletes all `State` objects with a name containing the letter `a` from the database `hbtn_0e_6_usa`.
- **model_city.py**: Python file that contains the class definition of a `City` and an instance `Base` using SQLAlchemy.
- **14-model_city_fetch_by_state.py**: Script that prints all `City` objects from the database `hbtn_0e_14_usa`.

## Author

- [Martin Olutade](https://github.com/silgenius)
