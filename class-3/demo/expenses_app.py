"""Expenses review — a Streamlit demonstration for Level 3 Class 3.
"""

import os

import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

HERE = os.path.dirname(os.path.abspath(__file__))
CSV_PATH = os.path.join(HERE, "datasets", "expenses.csv")

st.set_page_config(page_title="Expenses review", layout="wide")


# --- the same cleaning as Level 1 Class 3, unchanged -------------------------
@st.cache_data
def load_expenses(path):
    """Load and clean the expenses file."""
    frame = pd.read_csv(path).drop_duplicates()
    frame["department"] = frame["department"].str.lower()
    frame = frame.drop(columns=["notes"]).dropna(subset=["actual"])
    frame["difference"] = (frame["actual"] - frame["budget"]).round(2)
    return frame


expenses = load_expenses(CSV_PATH)

# --- the page ----------------------------------------------------------------
st.title("Expenses review")
st.caption("The same data, the same pandas — shown as a page instead of a notebook.")

# A dropdown. Changing it re-runs this whole script with the new value.
departments = ["All"] + sorted(expenses["department"].unique())
chosen = st.sidebar.selectbox("Department", departments)
months = st.sidebar.slider("How many months", 1, 6, 6)

shown = expenses
if chosen != "All":
    shown = shown[shown["department"] == chosen]
shown = shown[shown["month"].isin(sorted(expenses["month"].unique())[:months])]

# Three numbers across the top
budget = shown["budget"].sum()
actual = shown["actual"].sum()
used = round(actual / budget * 100, 1)

left, middle, right = st.columns(3)
left.metric("Budget", f"{budget:,.0f} EUR")
middle.metric("Actual", f"{actual:,.0f} EUR")
right.metric("Budget used", f"{used}%", delta=f"{round(used - 100, 1)}%")

# A chart, drawn with the matplotlib they already know
by_month = shown.groupby("month")["actual"].sum().round(2)

figure, axes = plt.subplots(figsize=(9, 3.5))
axes.plot(by_month.index, by_month.values, marker="o", color="#5C4270")
axes.set_ylabel("EUR")
axes.set_title(f"Actual spend by month — {chosen}")
axes.grid(True)
st.pyplot(figure)

# A table, and the underlying rows behind a fold
st.subheader("By category")
by_category = shown.groupby("category")[["budget", "actual"]].sum().round(2)
by_category["difference"] = (by_category["actual"] - by_category["budget"]).round(2)
st.dataframe(by_category.sort_values("difference", ascending=False), use_container_width=True)


with st.expander(f"Show the {len(shown)} rows behind this"):
    st.dataframe(shown, use_container_width=True)

st.sidebar.info(
    "Every control on this page is one line of Python. "
    "Changing one re-runs the whole script."
)
