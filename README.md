# AI-Assisted Diary & Habit Tracker

**Workshop Certificate:** [![Certificate](https://img.shields.io/badge/Verified-Google_Drive-blue?style=flat&logo=googledrive)](https://drive.google.com/file/d/13Pc-IeH0LEnpyVX-HQYNq7pMQ0DmlQ4V/view?usp=sharing)

A Python-based diary application built as a final project assignment to demonstrate and compare modern AI-assisted workflows. This repository directly contrasts structured **Spec-Driven Development (SDD)** with rapid, LLM-forward **"Vibe Coding"**, developed as part of the *Future of Software Development with LLMs* workshop.

> **Note:** You are currently viewing the **`sdd_submission`** branch, which contains the pristine, core application built strictly using upfront Spec-Driven Development (SDD) architectural planning.

---

## Overview & Methodology

This project showcases two distinct software engineering paradigms across different Git branches:

1. **Spec-Driven Development (SDD):** The core application structure (diary entries, habit tracking, and UI layout) was built by strictly following upfront markdown specifications to ensure explicit architectural planning and clear state management.
2. **Vibe Coding:** A separate security layer (password encryption gateway) was iteratively implemented on an alternative branch using high-level prompting and rapid AI-assisted execution.

---

## Features

* **Secure Diary Entries:** Create, view, and organize daily thoughts with local persistent storage.
* **Habit Tracking:** Log and track daily habits seamlessly alongside your journal entries to monitor personal growth.
* **Modern UI:** A clean, intuitive web interface powered by Streamlit, matching upfront wireframe specifications.
* **Local Storage:** Fast and lightweight data persistence using a structured JSON file.

---

## Project Structure

The project's architectural backbone is split between structured specs and functional python modules:

```text
├── openspec/               # Specification folder containing initial prompts/guidelines
├── app.py                  # Streamlit UI configuration and page setup
├── diary.py                # Core application functionalities & journal logic
├── diary.json              # Persistent local data store
├── design.md               # Core architecture and data model specs
├── tasks.md                # Step-by-step implementation checklist
├── streamlit_spec.md       # UI wireframe and state management specs
├── proposal.md             # Project proposal documentation
├── apply.md                # Updated specifications and tab layouts
└── README.md               # Project documentation

```

---

## Quick Start

### 1. Prerequisites

Ensure you have Python 3.8+ installed on your system.

### 2. Installation

Clone the repository and navigate to the project directory:

```bash
git clone [https://github.com/anweshasingh-dev/sdd-vs-vibe-coding-assignment.git](https://github.com/anweshasingh-dev/sdd-vs-vibe-coding-assignment.git)
cd sdd-vs-vibe-coding-assignment

```

Install the required dependencies:

```bash
pip install streamlit

```

### 3. Running the App

To run this branch's pure, spec-driven core application, ensure you checkout the correct branch and run the entry script:

```bash
git checkout sdd_submission
streamlit run app.py

```

---

## Workshop Takeaways

* Successfully translated abstract requirements into concrete markdown specification files (`design.md`, `tasks.md`, `streamlit_spec.md`) before writing code.
* Mastered the balance between rigid architectural planning (SDD) and rapid, LLM-driven feature iteration (Vibe Coding).
* Leveraged Git branching strategies to cleanly isolate and document different software engineering methodologies.

```
