# Power BI Build Steps

1) Get Data → Text/CSV → `data/processed/students_placements_fact.csv`
2) Data types:
   - year: Whole number
   - batch/branch/company/placed_type/placement_status/ppc_verification: Text
   - cgpa/package_lpa: Decimal number
   - is_placed: Whole number
3) Model: keep single-table star (no extra relationships needed).
4) Create measures listed in `DAX_Measures.md`.
5) Report visuals:
   - Slicer: `year` (vertical list, multi-select)
   - Cards: Total Batch, Total Company, Total Students, Highest Salary, Average Salary, Minimum Salary
   - Pie: Legend=`placed_type`, Values=`student_id` (Count)
   - Line/Area: Axis=`year`, Legend=`placement_status`, Values=`student_id` (Count)
   - Line/Area: Axis=`year`, Legend=`ppc_verification`, Values=`student_id` (Count)
   - Table: `batch` + Count of `student_id`
   - Matrix/Table: `company` with Count of `student_id` (add `placement_status` to Columns if you want a matrix)
6) View → Themes → Browse → `placement_theme.json`
7) Save as `dashboard/Students_Placement_Dashboard.pbix`.
