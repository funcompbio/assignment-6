[![FCB-R-autograding](../../actions/workflows/fcb_autograding.yml/badge.svg)](../../actions?query=workflow%3AFCB-R-autograding)

# Assignment 6 - FCB 2022
### Deadline: 11/11/2022 - 23:59

## Submission procedure

This assignment has to be submitted using GitHub Classroom. This
means that you should have cloned the GitHub repo of this assignment from
the organization account for FCB in the academic year 2022-23 at
[https://github.com/funcompbio2022](https://github.com/funcompbio2022)
using the submission link provided at the FCB Moodle site.

Once you have cloned the GitHub repo which has `assignment-6` and your
GitHub username as repo name, then you can work on it in your local disk
and _push_ your changes whenever you like, but make sure that you have pushed
the last version of your assignment before the deadline. There is no
_submit_ button or any other specific submission procedure or action than
just pushing your changes to you GitHub assignment repo. When correcting the
assignment, the version available at the deadline will be retrieved. If the
first version available is posterior to the deadline, then the mark of the
assignment will have a penalty.

To complete your submission (see rubric below) please **agree to the following
academic integrity statement** by editing this README file and placing the
letter `X` between the squared brackets preceding the statement:

- [] The work here submitted has been entirely developed by myself and is the
  result of my own work.

## Description

The goal of this assignment is to **create an R script that produces a CSV file
called `COVID19CATlast6months.csv` with COVID19 data for Catalonia derived from
the general population, starting on June 1st, 2021, with older data at the
beginning of the file and more recent data at the end of the file**. To achieve
this goal you should follow these 2 steps:

  1. Create an R script called `analysis.R` with the R commands that
  read the CSV file `catalunya_setmanal.csv` **provided in the repo
  of the assignment** and make the necesssary transformations and
  calculations to obtain a `data.frame` object with the columns
  `DATA_INI`, `R0_CONFIRMAT_M`, `IA14` and `PERC_PCRTAR_POSITIVES`,
  whose first lines look like this:

  ```
      DATA_INI R0_CONFIRMAT_M     IA14 PERC_PCRTAR_POSITIVES
1 2021-06-01       0.937658 102.9883                3.5296
2 2021-06-02       0.952521  99.3055                3.5322
3 2021-06-03       0.965133  96.5175                3.5561
4 2021-06-04       0.973635  94.3649                3.6365
5 2021-06-05       0.972995  92.0826                3.5797
6 2021-06-06       0.965863  91.2267                3.5496
  ```

  2. Let the `data.frame` object of the resulting data be called `dtf`,
  the last line of your script should write to disk that object
  into a CSV file called `COVID19CATlast6months.csv` with the
  following R command:

  ```
  write.csv(dtf, "COVID19CATlast6months.csv", row.names=FALSE)
  ```

Your assignment repo should have the following files:

  1. This `README.md` file.
  2. The COVID19 data CSV file `catalunya_setmanal.csv`.
  3. The R script file `analysis.R`.
  4. The resulting CSV file `COVID19CATlast6months.csv`.

The file `COVID19CATlast6months.csv` should have the following
characteristics:

  1. It should be a CSV file using the comma (`,`) as column separator and
     non-numeric values should be quoted with double quotes (`"`).
  2. It should have the following line as first (column header) line:
     ```
     "DATA_INI","R0_CONFIRMAT_M","IA14","PERC_PCRTAR_POSITIVES"
     ```
  3. The second and following lines should contain the values corresponding
     to the columns specified above, ordered by date with the oldest date in
     the first row and the most recent in the last one. The data should be
     derived from the general population, that is, **excluding the data
     from geriatric residences**. For instance, the first line should look
     like this one:
     ```
     "2021-06-01",0.937658,102.9883,3.5296
     ```

This assignment incorporates an autograding feature using a so-called
[GitHub Actions Worflow](https://github.com/features/actions), which will
help you to automatically test whether your R script is
correctly working after every _push_. More concretely, a few minutes after
you _pushed_ your changes to your remote GitHub repo, the badge labeled
`FCB-Python-autograding` on top of this README file will be red and display
the message `failing` if the autograding has not been successful, and
green with the message `passing` otherwise. You may click on badge to
look at output of the autograding tests to understand why it has failed,
if that was the case. This feature provides you with
[formative assessment](https://en.wikipedia.org/wiki/Formative_assessment)
and to work with it you need to edit your R script in a file called
`analysis.R` at the root of your GitHub repo and **leave intact the file
`catalunya_setmanal.csv`**.

## Evaluation rubric

The rubric to evaluate this assignment consists of the following items:

  * Did you agree to the academic integrity statement?
  * Does the assignment contain the required files?
  * Does the file `COVID19CATlast6months.csv` contain the four required columns?
  * Is the file `COVID19CATlast6months.csv` ordered chronologically starting
    on June 1st, 2021 and does it contain the COVID19 data derived from the
    general population for the four required columns?
  * Does the R code run without errors?
  * Does the R code produce the expected result?
