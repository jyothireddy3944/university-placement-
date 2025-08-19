# 🎓 University Placement – Power BI Suite (ETL-ready data + Power BI build kit + Live Streamlit preview)

This repo gives you:
1) **Processed analytic dataset** for placements (`data/processed/students_placements_fact.csv`)
2) **Power BI build kit** (theme, DAX, and step-by-step instructions) to create a dashboard like the screenshot you shared
3) **Streamlit dashboard** that mirrors the layout so you have a working interactive preview immediately

---

## 🧠 What’s in the dataset
**File:** `data/processed/students_placements_fact.csv`  
**Fields:**
- `student_id`, `student_name`
- `year`, `batch` (text), `branch`, `cgpa`
- `placement_status` (Selected, Rejected, In Process, Interview, Shortlisted)
- `is_placed` (0/1)
- `company` (only when placed), `placed_type` (T&P Placed, BP Placed, Self Placed, Off Campus Placed)
- `ppc_verification` (Verified, Pending, Not Verified, Not Joined)
- `package_lpa` (0 if not placed)

This single fact table keeps Power BI modeling simple.

---

## 📊 Power BI – Build the Dashboard (matches your screenshot)
> Folder: `powerbi/` contains a theme file, DAX cheatsheet, and build steps.

### 1) Import data
- Home → **Get Data → Text/CSV** → pick `data/processed/students_placements_fact.csv`
- Set data types:
  - year → Whole number
  - batch, branch, company, placed_type, placement_status, ppc_verification → Text
  - cgpa, package_lpa → Decimal number
  - is_placed → Whole number

### 2) Create DAX measures (Model view → New measure)
Copy from `powerbi/DAX_Measures.md`:
- **Total Students**  
  `Total Students = DISTINCTCOUNT( placements[student_id] )`
- **Total Company**  
  `Total Company = DISTINCTCOUNT( placements[company] )`
- **Highest Salary**  
  `Highest Salary = MAX( placements[package_lpa] )`
- **Average Salary**  
  `Average Salary = AVERAGE( placements[package_lpa] )`
- **Minimum Salary**  
  `Minimum Salary = MIN( placements[package_lpa] )`
- **Placement Rate %**  
  `Placement Rate % = DIVIDE( SUM(placements[is_placed]), [Total Students] )`

### 3) Build visuals (Report view)
- **Year slicer (left)** → add `year` as a Slicer (vertical), enable Multi-select and Select-all
- KPI **Cards (top row)** → add measures: Total Batch, Total Company, Total Students, Highest Salary, Average Salary, Minimum Salary  
  - *Total Batch* = `DISTINCTCOUNT(placements[batch])` (also in DAX file)
- **Pie chart** (Placed Students Type) → `placed_type` as Legend, `student_id` count/distinct as Values
- **Status of Placement** (line/area chart) → Axis = `year`; Legend = `placement_status`; Values = Count of `student_id`
- **Status of PPC Verification** (line/area chart) → Axis = `year`; Legend = `ppc_verification`; Values = Count of `student_id`
- **Batch table** → Rows: `batch`; Values: Count of `student_id`
- **Company table** → Rows: `company`; Columns: `placement_status` (optional); Values: Count of `student_id`  
  Sort by Total desc

### 4) Apply theme (optional)
- View → **Browse for themes** → choose `powerbi/placement_theme.json`

### 5) Save
- Save as `dashboard/Students_Placement_Dashboard.pbix` (keep folder structure tidy).

---

## ⚡ Live preview with Streamlit (optional, runs now)
If you want an immediate interactive preview without opening Power BI, run:
```bash
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r dashboard_streamlit/requirements.txt
streamlit run dashboard_streamlit/app.py
```
This mirrors the same KPIs and visuals so you can take screenshots for your README while your PBIX is being built.

---

## 📁 Structure
```
university-placement-powerbi-suite/
├─ data/
│  └─ processed/
│     └─ students_placements_fact.csv
├─ powerbi/
│  ├─ DAX_Measures.md
│  ├─ Build_Steps.md
│  └─ placement_theme.json
├─ dashboard_streamlit/
│  ├─ app.py
│  └─ requirements.txt
├─ assets/
│  └─ screenshot_placeholder.png
└─ README.md
```

---

## 📸 Tip for GitHub
Once you build the PBIX, export a PNG of the dashboard to `assets/` and reference it in your README:
```markdown
![Students Placement Dashboard](assets/screenshot.png)
```
