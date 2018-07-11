#!/usr/bin/env python
import os
import sys

from Tools.scripts.mailerdaemon import xl

from onlineapp.models import MockTest1, Student, College

def read_from_xl2(workbookName, sheetName):
    '''this function reads data from a specified sheet and returns a 2d list of data'''
    wb = xl.load_workbook(workbookName)
    sheetsrc = wb[sheetName]

    rows = sheetsrc.max_row
    cols = sheetsrc.max_column

    data = []
    for r in range(0, rows):
        data.append([])

    for r in range(rows):
        for c in range(cols):
            cell = sheetsrc.cell(row=r + 1, column=c + 1)
            data[r].append(cell.value)

    return data
def populatedb2():
    marks = read_from_xl2("result1.xlsx", "TableData")[1:]
    colleges = read_from_xl2("students.xlsx", "Colleges")[1:]
    current = read_from_xl2("students.xlsx", "Current")[1:]
    deletions = read_from_xl2("students.xlsx", "Deletions")[1:]

    collegeDict = dict()
    stdFolderDict = dict()

    for college in colleges:
        c = College(name=college[0], location=college[2], acronym=college[1], contact=college[3])
        c.save()
        collegeDict[college[1]] = c

    for student in current:
        try:
            collegeDict[student[1]]
        except Exception:
            print(student[1], "not found")
        else:
            s = Student(name=student[0], dob=None, email=student[2], db_folder=student[3], dropped_out=False,
                        college=collegeDict[student[1]])
            s.save()
            stdFolderDict[str(student[3]).lower()] = s

    for dStudent in deletions:
        s = Student(name=dStudent[0], dob=None, email=dStudent[2], db_folder=dStudent[3], dropped_out=True,
                    college=collegeDict[dStudent[1]])
        s.save()

    for std in marks:
        dbname = str(str(std[0]).split('_')[2]).lower()
        try:
            stdFolderDict[dbname]
        except Exception:
            print(dbname, " not found")
        else:
            m = MockTest1(problem1=str(std[1]), problem2=str(std[2]), problem3=str(std[3]), problem4=str(std[4]),
                          total=str(std[5]), students=stdFolderDict[dbname])
            m.save()


if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "onlineClass.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
    populatedb2()
