# Assignment 6 - FCB 2020
### Deadline: 13/11/2020 - 23:59

This assignment has been developed in collaboration with Dr. Jordi Mestres,
head of the [Systems Pharmacology Research Group](http://syspharm.imim.cat)
at the Hospital del Mar Research Institute ([IMIM](https://www.imim.cat)).

## Submission procedure

This assignment has to be submitted using GitHub Classroom. This
means that you should have cloned the GitHub repo of this assignment from
the organization account for FCB in the academic year 2020-21 at
[https://github.com/funcompbio2020](https://github.com/funcompbio2020)
using the submission link provided at the FCB Moodle site.

Once you have cloned the GitHub repo which has `assignment-5` and your
GitHub username as repo name, then you can work on it in your local disk
and _push_ your changes whenever you like, but make sure that you have pushed
the last version of your assignment before the deadline. There is no
_submit_ button or any other specific submission procedure or action than
just pushing your changes to you GitHub assignment repo. When correcting the
assignment, the version available at the deadline will be retrieved. If the
first version available is posterior to the deadline, then the mark of the
assignment will have a penalty.

## Description

The goal of this assignment is to **implement in Python a parser of
[SMILES](https://en.wikipedia.org/wiki/Simplified_molecular-input_line-entry_system) strings**,
similar to the one developed during Practical 7 but developing a more compact
code by **using** the [`index()` method](https://docs.python.org/3/tutorial/datastructures.html)
of _list_ objects in Python.

The `index()` method returns the position at the first occurrence of the
specified value.

**Syntax:** `list.index(element)`, where `element` is the element of the
list to search for.

**Example:** Let's say we want to extract the index of month `apr` (April)
in a list object `months` containing the months of the year. We illustrate
how the `index()` method works from the Python command-line interpreter:

```
>>> months = ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct"]
>>> print(months.index("apr"))
3
```

**Example:** Given a vector of months stored in list object `months` and a vector of
number of COVID19 deaths per month in Spain, stored in a list object `ncoviddeaths`,
extract the number of deaths from April, by relating both list objects using the
`index()` method:

```
>>> months = ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct"]
>>> ncoviddeaths = [0, 0, 13918, 11644, 2592, 411, 106, 1218, 2857, 3502]
>>> print(ncoviddeaths[months.index("apr")])
11644
```

Using the `index()` method, optimize the SMILES parser that you have written in
Python in Practical 7, which takes a SMILES string as input and returns the
molecular formula as output in the right format. **The final code should have
less than 35 lines**, excluding blank and comment lines, and it should provide
the correct molecular formula given the corresponding input SMILES string,
at least for the following drugs: _aspirine_, _ibuprofen_, _caffeine_ and _nevirapine_.
Please use the [DrugBank](https://drugbank.com) to figure out their corresponding
SMILES strings and expected molecular formulas.

This assignment incorporates [GitHub Classroom Autograding](https://mspoweruser.com/github-classroom-autograding-feature),
which will help you to automatically test whether your Python program is
correctly working after every _push_. To work with this feature you
need to edit your program in the existing file `src/smilesparser.py`,
and leave the rest of the files and directory structure
intact. The file `src/smilesparser.py` is a template that
contains instructions written as comments, indicating where should you
edit your code. Note that part of the template already defines some of
the variables that you **have to** use. Their meaning should be clear
to your from having done Practical 7.


Your assignment repo should have the following files:

  1. This `README.md` file.
  2. The `src` directory with the initial files of the assignment repo.
  3. The `test` directory with the initial files of the assignment repo.

Eventually, you may encounter that Python automatically creates a directory called
`__pycache__`, you may ignore that directory since this template is already
prepared to ignore that directory by including it into a `.gitignore` file that
informs Git to avoid putting certain files under version control. In any case,
**you should only be editing the file `src/smilesparser.py`**.

## Evaluation rubric

The rubric to evaluate this assignment consists of the following items:

  * Does the assignment contain the required files?
  * Does the Python program `src/smilesparser.py` runs without errors?
  * Does the Python program `src/smilesparser.py` calculates the molecular formula from a given SMILES string correctly?
  * Does the Python program `src/smilesparser.py` passes all autograding tests?
  * Does the Python program `src/smilesparser.py` has fewer than 35 lines of code, excluding blank and comment lines?
  * Does the Python program `src/smilesparser.py` use the `index()` method for _list_ objects?
