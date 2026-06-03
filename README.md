# AI-Assisted Diary & Habit Tracker

A Python-based diary application built as a final project for the workshop: **"Future of Software Development: Spec-Driven Development"**. This project serves as a practical exploration of modern development workflows, contrasting structured **Spec-Driven Development (SDD)** with rapid, LLM-forward **"Vibe Coding"**.

---

## Overview & Methodology

This repository showcases two distinct development paradigms used to build and extend the application:

1. **Spec-Driven Development (SDD):** The core application (diary entries, habit tracking, and Streamlit UI) was built strictly following upfront technical specifications. This ensured high code quality, architectural clarity, and structured progress.
2. **Vibe Coding:** The security layer (password protection) was iteratively implemented using high-level prompting and rapid AI-assisted execution to quickly prototype and deploy a critical feature.

To clearly demonstrate both approaches, the repository is split into two primary Git branches:

* `sdd_submission`: The pristine, spec-compliant core application.
* `vibe_coded_submission`: The final version featuring the vibe-coded password integration.

---

## Features

* **Secure Diary Entries:** Create, view, and organize daily thoughts with local persistent storage.
* **Habit Tracking:** Log and track daily habits alongside your journal entries to monitor personal growth.
* **Password Protection:** A secure login layer implemented during the vibe-coding phase to restrict unauthorized access.
* **Modern UI:** A clean, intuitive, and responsive web interface powered by Streamlit.
* **Local Storage:** Fast and lightweight data persistence using structured JSON files.

---

## Project Structure

The project's architectural backbone is defined by its SDD documentation files:

```text
├── specs/
│   ├── design.md           # Core architecture and data model specifications
│   ├── tasks.md            # Step-by-step implementation checklist
│   └── streamlit_spec.md   # UI wireframe and state management specs
├── diary.py                  # Main Streamlit application entry point
├── storage.json            # Persistent local data store (Diary & Habits)
└── README.md               # Project documentation

```

---

## Quick Start

### 1. Prerequisites

Ensure you have Python 3.8+ installed on your system.

### 2. Installation

Clone the repository and navigate to the project directory:

```bash
git clone https://github.com/your-username/diary-sdd-project.git
cd diary-sdd-project

```

Install the required dependencies:

```bash
pip install streamlit

```

### 3. Running the App

To view the final version including the password protection feature, ensure you are on the vibe-coded branch:

```bash
git checkout vibe_coded_submission
streamlit run diary.py

```

---

## Workshop Takeaways

* Successfully translated abstract requirements into concrete `markdown` specification documents before writing a single line of code.
* Mastered the balance between rigid architectural planning (SDD) and fast-paced feature iteration (Vibe Coding).
* Leveraged Git branching strategies to cleanly isolate and document different software engineering methodologies.

---

**Workshop Certificate:** [![Certificate](https://img.shields.io/badge/Verified-Google_Drive-blue?style=flat&logo=googledrive)](https://drive.google.com/file/d/13Pc-IeH0LEnpyVX-HQYNq7pMQ0DmlQ4V/view?usp=sharing)
