Movie section models Features
=============================

Each movie will have the following features

1. Movie (Table in DB)
2. Gener (Table in DB)
3. Actors (Table in DB)
4. Directores (Table in DB)
5. writers (Table in DB)


Relations between our tables
============================
1. A movie can have many Gener and a Gener can have many movies (ManytoMany relatioan)
2. A movie can have many actor and an actor can play in different movies (ManytoMany relation)
3. A movie can have many director and a director can have many movies (ManytoMany relation)
4. A movie can have many writer and a writer can write many movies (ManytoMany relation)

Attributes for tables
=====================
Movie:
- title
- pub_date
- gener
- director
- writer
- actors
- description

Gener:
- gener_name
- gener_desc

Actor:
- name
- lastname
- gender
- date_of_birth
- place_of_birth
- date_of_death
- place_of_death

Director:
- name
- lastname
- gender
- date_of_birth
- place_of_birth
- date_of_death
- place_of_death

Writer:
- name
- lastname
- gender
- date_of_birth
- place_of_birth
- date_of_death
- place_of_death




