# Notes

## Questions about the ODG_Sample_Raw data set

* Why does ICD-9 has a date column(column G)? What is the point that every patient has multiple ICD-9 dates? 

  Every ICD-9 code has its diagnosis date, and it is reflected on the column next to it.

* What is ICD-9-PC column(column R)? I cannot find it on google.

  It is a column with ICD-9 codes. It basically reflects what each treatment(presented with procedure code) is used for which disease.

* There are 2 columns of _Date of Service_(column O and column T). Which one should I pick? What does _Date of Service_ mean in this context?

  The two columns serve the procedure code column and the other treatment code column respectively.

* There are 2 columns of _Number of Units_ column(column Q and V). What does _Number of Units_ mean? Which column should I pick? 

  Same answer as above.

* There are two columns regarding treatment. One is _Procedure code_(column N), the other is _Other treatment code_(column S). Why are they separated? Do they belong to different coding system?

  Remains to be answered.

* What does the _amount paid_ column (column U) refer to? The sum of all the amount in one cell doesn't equal either the medical cost or the indemnity cost.

  Notice that there are two "amount paid" columns. They correspond to each "procedure code" or "other treatment code" column.

* Does the real dataset has the same structure as this mock dataset?

  Remains to be answered.

## About the files in this repo

* setup.sql is used for setting up the database. It includes all the creating table commands.
* ODGdb is a shell script. It supports _./ODGdb create/destroy/reset/head_ commands. These four commands create the database, destroy the database, reset the database and print out the first three entries of every table in the database.
* prep.py is used for inserting data into the database. Can only be used after database is set up.

## Issues

* The python script is still using sqlite3 api. Should switch to psycopg2.
* The database structure remains to be settled.