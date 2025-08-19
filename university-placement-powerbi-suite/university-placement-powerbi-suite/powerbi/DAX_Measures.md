> Use table name **placements** for the imported CSV.

Total Students = DISTINCTCOUNT(placements[student_id])
Total Company = DISTINCTCOUNT(placements[company])
Total Batch = DISTINCTCOUNT(placements[batch])

Highest Salary = MAX(placements[package_lpa])
Average Salary = AVERAGE(placements[package_lpa])
Minimum Salary = MIN(placements[package_lpa])

Placed Students = SUM(placements[is_placed])
Placement Rate % = DIVIDE( [Placed Students], [Total Students] )

-- Optional extras
Total Selected = CALCULATE(COUNTROWS(placements), placements[placement_status] = "Selected")
Total Rejected = CALCULATE(COUNTROWS(placements), placements[placement_status] = "Rejected")
Avg CGPA (Placed) = CALCULATE(AVERAGE(placements[cgpa]), placements[is_placed] = 1)
