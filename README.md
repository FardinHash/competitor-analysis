# Competitor Analysis

This repository contains a system for analyzing competitors using data from various sources like Google, Wikipedia, Reddit and LinkedIn. It dynamically generates SWOT analyses and PDF reports using advanced AI-driven techniques.

## Features

- **Multi-Source Data Integration**:
  Aggregates data from Google Search, Wikipedia, and Reddit.
- **AI-Driven SWOT Analysis**:
  Uses state-of-the-art LLMs (e.g., [GPT-4](https://github.com/FardinHash/competitor-analysis/)) to extract insights and generate SWOT analyses.
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

### 4. Set Up API Keys
Create a `.env` file in the root directory and add the following keys:
```
HUGGINGFACE_HUB_TOKEN=<Your Hugging Face Token>
```

For Reddit integration:
```
REDDIT_CLIENT_ID=<Your Reddit App Client ID>
REDDIT_CLIENT_SECRET=<Your Reddit App Client Secret>
REDDIT_USER_AGENT=<Your App Name>
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

## **Test Cases**

To ensure the system works as expected, the following test cases are implemented:

### **1. SWOT Analysis**
- **Test Input**: Processed data from Google, Wikipedia, and LinkedIn.
- **Expected Output**: 
  - Structured SWOT analysis containing:
    - Strengths
    - Weaknesses
    - Opportunities
    - Threats
  - Cleaned and deduplicated results.

### **2. Data Normalization**
- **Test Input**: Raw data from Google, Wikipedia, and LinkedIn.
- **Expected Output**:
  - Normalized summaries for each source.
  - Fallback values for missing or erroneous data.

### **3. End-to-End Workflow**
- **Test Input**: A company query like `OpenAI`.
- **Expected Output**:
  - Complete workflow execution from data retrieval to PDF report generation.
  - A valid PDF file saved in the `outputs/reports/` directory.

### **4. LinkedIn Data Retrieval**
- **Test Input**: Query for a company like `OpenAI`.
- **Expected Output**:
  - Valid LinkedIn data retrieved.
  - Handles missing data gracefully with fallback values.

### **5. Report Generation**
- **Test Input**: SWOT analysis for a company (e.g., `OpenAI`).
- **Expected Output**:
  - A well-formatted PDF report containing the SWOT analysis.
  - The PDF is non-empty and includes relevant insights.

---

### **Running Tests**
To run the test suite, use the following command:
```bash
pytest tests/
```
---

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.