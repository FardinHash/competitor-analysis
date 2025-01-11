# Competitor Analysis

This repository contains a system for analyzing competitors using data from various sources like Google, Wikipedia, and Reddit. It dynamically generates SWOT analyses and PDF reports using advanced AI-driven techniques.

## Features

- **Multi-Source Data Integration**:
  Aggregates data from Google Search, Wikipedia, and Reddit.
- **AI-Driven SWOT Analysis**:
  Uses state-of-the-art LLMs (e.g., [Llama-2](https://github.com/FardinHash/competitor-analysis/tree/llama2), [Gemma 2](https://github.com/FardinHash/competitor-analysis/tree/gemma-27b)) to extract insights and generate SWOT analyses.
- **Automated PDF Reporting**:
  Produces professional reports summarizing the analysis.
- **Modular Multi-Agent System**:
  Designed for scalability and easy extensibility.

---

## Setup

### 1. Clone the Repository
```bash
git clone git@github.com:FardinHash/competitor-analysis.git
cd competitor-analysis
```

### 2. Create a Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```
---

## Usage

### Running the System
To run the system, execute the following command:
```bash
python src/main.py
```

### Example
1. Enter a company name or product query (e.g., `Tesla`).
2. The system retrieves and processes data, generates a SWOT analysis, and creates a PDF report.
3. The report is saved in the `outputs/reports/` directory.

---

## Test Cases

To ensure the system works as expected, use the following example test cases:

### 1. **Data Retrieval**
- **Test Input**: Query for a company like `OpenAI`.
- **Expected Output**: Retrieved summaries from Google, Wikipedia, and Reddit in structured format.

### 2. **NLP Processing**
- **Test Input**: Raw data from multiple sources.
- **Expected Output**: Normalized and cleaned data ready for SWOT analysis.

### 3. **SWOT Analysis Generation**
- **Test Input**: Normalized data for `Tesla`.
- **Expected Output**: A coherent SWOT analysis with structured Strengths, Weaknesses, Opportunities, and Threats.

### 4. **PDF Report Generation**
- **Test Input**: SWOT analysis for `SpaceX`.
- **Expected Output**: A PDF file saved in `outputs/reports/SpaceX_analysis_report.pdf`.

### 5. **End-to-End Workflow**
- **Test Input**: Query for `NVIDIA`.
- **Expected Output**: Complete analysis with a generated PDF report containing SWOT insights.

### Running Tests
To run the test scripts, use:
```bash
pytest tests/
```
---

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.