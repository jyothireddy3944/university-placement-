import streamlit as st, pandas as pd, numpy as np, altair as alt
from pathlib import Path

st.set_page_config(page_title="Students Placement Dashboard", page_icon="🎓", layout="wide")
DATA = Path(__file__).resolve().parents[1] / "data" / "processed" / "students_placements_fact.csv"
df = pd.read_csv(DATA)

st.title("Students Placement Dashboard (Preview)")
st.caption("This Streamlit app mirrors the Power BI layout so you can interact now and take screenshots while you build the PBIX.")

with st.sidebar:
    years = sorted(df["year"].dropna().unique().tolist())
    year_sel = st.multiselect("Year", options=years, default=years)
    branches = sorted(df["branch"].dropna().unique().tolist())
    branch_sel = st.multiselect("Branch", options=branches, default=branches)

mask = (df["year"].isin(year_sel)) & (df["branch"].isin(branch_sel))
d = df.loc[mask].copy()

# KPIs
total_batch = d["batch"].nunique()
total_company = d["company"].nunique()
total_students = d["student_id"].nunique()
highest_salary = d["package_lpa"].max()
avg_salary = d["package_lpa"].mean()
min_salary = d["package_lpa"].replace(0, np.nan).min() or 0.0

c1,c2,c3,c4,c5,c6 = st.columns(6)
c1.metric("Total Batch", f"{total_batch}")
c2.metric("Total Company", f"{total_company}")
c3.metric("Total Students", f"{total_students}")
c4.metric("Highest Salary", f"{highest_salary:.0f}K")
c5.metric("Average Salary", f"{avg_salary:.2f}K")
c6.metric("Minimum Salary", f"{min_salary:.0f}")

st.divider()

lcol, rcol = st.columns(2)

# Pie - Placed Students Type
pie_data = d[d["is_placed"]==1].groupby("placed_type", as_index=False)["student_id"].count().rename(columns={"student_id":"count"})
pie_chart = alt.Chart(pie_data).mark_arc().encode(
    theta="count",
    color=alt.Color("placed_type", legend=alt.Legend(title="T&P Type")),
    tooltip=["placed_type","count"]
).properties(title="Placed Students Type")
lcol.altair_chart(pie_chart, use_container_width=True)

# Status of Placement (line)
status_year = d.groupby(["year","placement_status"], as_index=False)["student_id"].count()
line1 = alt.Chart(status_year).mark_line(point=True).encode(
    x="year:O", y="student_id:Q", color="placement_status:N", tooltip=["year","placement_status","student_id"]
).properties(title="Status of Placement")
rcol.altair_chart(line1, use_container_width=True)

# Status of PPC Verification (line)
st.altair_chart(
    alt.Chart(d.groupby(["year","ppc_verification"], as_index=False)["student_id"].count()).mark_line(point=True).encode(
        x="year:O", y="student_id:Q", color="ppc_verification:N", tooltip=["year","ppc_verification","student_id"]
    ).properties(title="Status of PPC Verification"),
    use_container_width=True
)

# Batch table
st.subheader("Batch")
st.dataframe(d.groupby("batch", as_index=False)["student_id"].count().rename(columns={"student_id":"Count of Enrollment Number"}).sort_values("Count of Enrollment Number", ascending=False))

# Company table
st.subheader("Company")
company_tbl = d.groupby("company", as_index=False)["student_id"].count().rename(columns={"student_id":"Total"}).sort_values("Total", ascending=False)
st.dataframe(company_tbl)
