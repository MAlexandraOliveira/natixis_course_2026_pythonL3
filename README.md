# 🐍 Natixis Python Level 3

## 📚 Course Overview

This advanced course is designed for students who can already write functions and analyse data with Pandas, and who now want to organise code the way a real project does. Students will learn to store data in a database and query it with SQL, model the world with classes and inheritance, and split their work into reusable modules. The course closes with a project that uses all three at once. Every class is taught from a Google Colab notebook, so there is nothing to install.

> 📅 **Materials are published as the course progresses.** Each class appears here on the day it is taught, and its solutions afterwards.

# 📋 Course Structure (Advanced Python - Level 3)

## 🚀 Class 1: Databases with SQLite
### 🗄️ Why a Database
- What a database gives you that a CSV does not
- Connecting with `sqlite3`, and where the file actually lives

### 🏗️ Creating & Filling a Table
- `CREATE TABLE IF NOT EXISTS`, and column types
- Inserting rows, and `executemany` with `?` placeholders
- `commit()` — why nothing is saved until you call it

### 🔍 Querying
- `SELECT`, `WHERE`, `ORDER BY` and `LIMIT`
- Changing rows with `UPDATE`, removing them with `DELETE`

### 📊 Summarising in SQL
- `COUNT`, `SUM`, `AVG`, `MIN`, `MAX`
- `GROUP BY`, and naming a result with `AS`

### 🐼 SQL and Pandas Together
- `pd.read_sql_query()` — from a query straight to a DataFrame
- Choosing which tool does the work

### 📝 Exercises
- Class 1 Exercises — *published on the day of the class*
- Class 1 Solutions — *published after the class*

---

## 📊 Class 2: Object-Oriented Programming
### 🧱 Why Objects
- The problem objects solve
- Why you already use them every day, without noticing

### 🏛️ Classes & Objects
- Class and object — the blueprint and the thing
- `__init__`, attributes, and what `self` actually means
- Creating several objects from one class

### ⚙️ Methods
- Giving an object something to do
- Methods that use the object's own attributes

### 🔒 Shared Data & Encapsulation
- Instance variables against class variables
- The `_private` naming convention, and keeping the inside inside

### 🧬 Inheritance
- Building on a class you already have
- `super().__init__()`, and overriding a method
- `isinstance`, and why a subclass *is* its parent

### 📝 Exercises
- Class 2 Exercises — *published on the day of the class*
- Class 2 Solutions — *published after the class*

---

## 📈 Class 3: Modules & Packages
### 📦 What a Module Is
- Reusable code, kept somewhere else
- Why `import pandas as pd` was a module all along

### 🔋 The Standard Library
- `math`, `random`, `datetime` and `statistics`
- `random.seed()`, and making randomness repeatable

### 📥 Installing More
- `pip`, PyPI, and what an install actually does
- Why a Colab install lasts only for the session

### ✍️ Writing Your Own Module
- Keeping your definitions in a separate notebook
- Importing it with `import_ipynb`
- `if __name__ == "__main__":`, so a module stays quiet when imported

### 🔀 The Three Ways to Import
- `import x`, `from x import y`, `import x as z`
- Why `from x import *` is best avoided

### 🗂️ Packages
- A folder of modules, and what `__init__.py` is for

### 📎 Version Control & Streamlit — *for information*
- Git and GitHub: repository, commit, push, pull, branch, merge
- Streamlit: turning a script into a shareable web page
- Presented from slides with a live demonstration. Both need a local editor such as VS Code, so there is nothing to install and nothing in the exercises about them.

### 📝 Exercises
- Class 3 Exercises — *published on the day of the class*
- Class 3 Solutions — *published after the class*

---

## 🚀 Class 4: Mini-Project
### 💡 Project — Supplier Payments Monitor
- Write a module holding every rule: the classes, the conversion fee, the formatting
- Model payments with a class, and foreign payments with a subclass that overrides the total
- Store them in an SQLite database with `executemany`
- Answer three questions in SQL, using `GROUP BY` and a `?` placeholder
- Read the table back into Pandas and summarise it
- Produce two charts side by side, saved as a PNG
- Finish with a report that contains no rules at all — only data, a loop, and calls into the module

---

## 🎯 Learning Objectives

By the end of this course, students will be able to:
- Explain when a database is a better choice than a CSV file.
- Create a table, insert rows safely with placeholders, and commit the result.
- Query data with `SELECT`, `WHERE`, `ORDER BY`, `GROUP BY` and the aggregate functions.
- Move between SQL and Pandas, and choose which should do the work.
- Design a class with attributes and methods, and explain the role of `self`.
- Use inheritance to extend a class, override a method, and call `super()`.
- Distinguish instance variables from class variables, and apply the `_private` convention.
- Use the standard library instead of rewriting what Python already provides.
- Install a package with `pip`, and understand what that does.
- Split a project into modules and import them three different ways.
- Recognise what version control and Streamlit are, and when they would be useful.
- Combine modules, classes, a database and charts into one working piece of software.

## ✅ Prerequisites

Levels 1 and 2 of this programme, or equivalent experience. Before taking this course, students should be familiar with:

- Python syntax, the core data types, and f-strings
- Control flow: `if` / `elif` / `else`, `for` and `while` loops
- Core data structures: lists, tuples, sets and dictionaries
- Writing functions with parameters, return values and default arguments
- List, dictionary and set comprehensions
- `lambda`, and `sorted()` with a `key`
- Built-in functions such as `map`, `filter`, `zip`, `any` and `all`
- Pandas: reading a CSV, filtering, creating columns, and `groupby`
- Building charts with Matplotlib and Seaborn

## 📁 Course Materials

### 📚 Class Notebooks
- Class 1 — Databases with SQLite *(published on the day of the class)*
- Class 2 — Object-Oriented Programming *(published on the day of the class)*
- Class 3 — Modules & Packages *(published on the day of the class)*
- Class 4 — Mini-Project *(published on the day of the class)*

### 📝 Exercises & Solutions
- **Class 1**: *published on the day of the class*
- **Class 2**: *published on the day of the class*
- **Class 3**: *published on the day of the class*
- **Class 4**: *published on the day of the class*

### 📊 Slides & Demonstrations
- Class 3 — Git, GitHub & Streamlit slides, plus a Streamlit demonstration run by the instructor *(published with Class 3)*

## 🚀 Getting Started

1. **📥 Setup Environment**
   - Sign in to a Google account
   - Open [Google Colab](https://colab.research.google.com) in your browser
   - Nothing to install: Python, Pandas, Matplotlib, Seaborn and `sqlite3` are already there

2. **📚 Start Learning**
   - Open the Class 1 notebook for the theory, and run every cell yourself
   - Practise with the Class 1 exercises
   - Check your work against the solutions, shared after the class

3. **🔄 Progress Through Classes**
   - Follow the same pattern for Classes 2-4
   - From Class 3 onwards, keep a class's module notebooks in the same folder as the notebook that imports them

4. **💡 Apply Your Skills**
   - The final class of this course is dedicated to a project that applies everything covered throughout this advanced course.

---

## ⚠️ Intellectual Property Notice

**Important**: This course material is the intellectual property of the course instructors and should not be distributed, shared, or reproduced without their explicit written consent. All content, exercises, and materials are protected by copyright and are intended solely for enrolled students of this course.

---

*This course completes the programme, with a focus on structuring code the way a working project does: stored data, modelled objects, and reusable modules.*
