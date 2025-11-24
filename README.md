# Imperative ETL Pipeline

A complete **data processing pipeline** using the **imperative programming paradigm in Python**.  
It follows a **step-by-step, state-changing workflow**, including:

- Loading data from CSV, JSON, or SQL.
- Handling missing values (removing, filling, auto-detect strategy).
- Cleaning and transforming data.
- Performing basic statistical analysis.
- Optional visualization.
- Saving processed outputs.

The goal is to **demonstrate the imperative approach** for data pipelines, where each step updates program state explicitly and sequentially.

---

## Project Structure

imperative-data-processing-pipeline/
│
├── data/
│ ├── raw/ # Original datasets (CSV/JSON/SQL)
│ └── processed/ # Cleaned/transformed datasets saved here
│
├── src/
│ ├── loader.py # Load CSV/JSON/SQL datasets imperatively
│ ├── cleaning.py # Handle missing values (remove/fill/auto)
│ ├── transform.py # Filter, add columns, aggregate data
│ ├── analysis.py # Statistical summaries, correlations, dataset overview
│ ├── visualize.py # Optional charts (bar, line, histogram)
│ ├── output.py # Save cleaned datasets, reports, plots
│ ├── utils.py # Helper functions (logging, type checking, validation)
│ └── pipeline.py # Main pipeline controller (calls all steps sequentially)
│
├── tests/ # Unit tests for each module
├── main.py # Entry point to run the pipeline
├── requirements.txt # Python dependencies
└── README.md # Project documentation



## 🚀 Setup Guide

### 1. Clone the repository

```bash
git clone https://github.com/FatmaAMR/Imperative-ETL-Pipeline
cd Imperative-ETL-Pipeline
```

### 2. Install dependencies
```bash
pip install -r requirements.txt 
```

If you don’t have requirements.txt, create it by:

```bash
pip freeze > requirements.txt 
```

### 3. Place your datasets

Put raw datasets in `data/raw/.`

Processed datasets will be saved to `data/processed/.`

### 4. Run the pipeline
```bash
python main.py
```

This will execute the full imperative workflow: 
> load → clean → transform → analyze → save.
