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
