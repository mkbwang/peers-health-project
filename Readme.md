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

## Other general questions

* What does PEERS want from us? A report? A bunch of codes that fulfill their ML tasks of their data?
* I believe we need to make some form of presentation on Feb 15th for PEERS. What are we planning to present?
* How large is the dataset?
* How long will the project be? On the [PEERS WEBSITE](https://www.peershealth.com/university-of-michigan-rtw-intelligent-learning-research/), they say it is going to be 2 years. Will it be that long? 