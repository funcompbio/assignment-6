[![FCB-R-autograding](../../actions/workflows/fcb_autograding.yml/badge.svg)](../../actions?query=workflow%3AFCB-R-autograding)

# Assignment 6 - FCB 2023
### Deadline: 7/11/2023 - 23:59

## Submission procedure

This assignment has to be submitted using GitHub Classroom. This
means that you should have cloned the GitHub repo of this assignment from
the organization account for FCB in the academic year 2023-24 at
[https://github.com/funcompbio2023](https://github.com/funcompbio2023)
using the submission link provided at the FCB Moodle site.

Once you have cloned the GitHub repo which has `assignment-6` and your
GitHub username as repo name, then you can work on it in your local disk
and _push_ your changes whenever you like, but make sure that you have pushed
the last version of your assignment before the deadline. There is no
_submit_ button or any other specific submission procedure or action than
just pushing your changes to you GitHub assignment repo. When correcting the
assignment, the latest version available will be retrieved. If that latest
version available is posterior to the deadline, then the mark of the assignment
will have a penalty.

To complete your submission (see rubric below) please **agree to the following
academic integrity statement** by editing this README file and placing the
letter `X` between the squared brackets preceding the statement:

- [] The work here submitted has been entirely developed by myself and is the
  result of my own work.

## Description

The goal of this assignment is to **create an R script that produces a CSV file
called `infeccions_catalunya_2023.csv` with data from the analysed samples
of the primary care microbiological sentinel surveillance system, aggregated
and ordered by month for the year 2023.** To achieve this goal you should
follow these 2 steps:

  1. Create an R script called `analysis.R` with the R commands that
  read the CSV file `mostres_analitzades.csv` **provided in the repo
  of the assignment** and make the necessary transformations and
  calculations on the input data from `mostres_analitzades.csv` to obtain a
  `data.frame` object with the columns `MES`, `POSITIUS`, `TOTAL` and
  `PERCENTAGE`, corresponding respectively to the month on which values
  of `TOTAL` and `POSITIUS` have been aggregated, the columns `positiu` and
  `total` from the CSV file `mostres_analitzades.csv` aggregated by month,
  and the percentage of positives cases over the corresponding total of the
  month, calculated up to one decimal digit. To round the calculation to one
  decimal digit use the R function `round()`; consult its help page to figure
  out how it works. The contents of this `data.frame` object should look
  exactly like this:

  ```
     MES POSITIUS TOTAL PERCENTATGE
1  Jan     1406  2046        68.7
2  Feb     1233  1656        74.5
3  Mar      971  1440        67.4
4  Apr      588   918        64.1
5  May      778  1224        63.6
6  Jun      394   724        54.4
7  Jul      374   649        57.6
8  Aug      269   482        55.8
9  Sep      506   850        59.5
10 Oct      481   794        60.6
  ```

  2. Let the `data.frame` object of the resulting data be called `res`,
  the last line of your script should write to disk that object
  into a CSV file called `infeccions_catalunya_2023.csv` with the
  following R command:

  ```
  write.csv(res, "infeccions_catalunya_2023.csv", row.names=FALSE)
  ```

Your assignment repo should have the following files:

  1. This `README.md` file.
  2. The SIVIC data CSV file `mostres_analitzades.csv`.
  3. The R script file `analysis.R`.
  4. The resulting CSV file `infeccions_catalunya_2023.csv`.

The file `infeccions_catalunya_2023.csv` should have the following
characteristics:

  1. It should be a CSV file using the comma (`,`) as column separator and
     non-numeric values should be quoted with double quotes (`"`).
  2. It should have the following line as first (column header) line:
     ```
     "MES","POSITIUS","TOTAL","PERCENTATGE"
     ```
  3. The second and following lines should contain the values corresponding
     to the columns specified above. For instance, the second line in the file
     should look like this:
     ```
     "Jan",1406,2046,68.7
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
`analysis.R` at the root of your GitHub repo and **leave intact the rest of
the files, except for editing `README.md` to agree to the academic integrity
statement**.

## Evaluation rubric

The rubric to evaluate this assignment consists of the following items:

  * Did you use the GitHub user profile you provided in the first assignment?
  * Did you properly agree to the academic integrity statement?
  * Does the assignment contain the required files?
  * Does the file `COVID19CATlast6months.csv` contain the four required columns?
  * Is the file `COVID19CATlast6months.csv` ordered chronologically starting
    on June 1st, 2021 and does it contain the COVID19 data derived from the
    general population for the four required columns?
  * Does the R code run without errors?
  * Does the R code produce the expected result?
