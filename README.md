# AI-Assisted Diary & Habit Tracker

A Python-based diary application built as a final project assignment to demonstrate and compare modern AI-assisted workflows. This repository directly contrasts structured **Spec-Driven Development (SDD)** with rapid, LLM-forward **"Vibe Coding"**, developed as part of the *Future of Software Development with LLMs* workshop.

> **Navigation Guide:** This repository is a comparative study split across branches.
> * To view the pristine, spec-compliant core, switch to the [sdd_submission](https://github.com/anweshasingh-dev/sdd-vs-vibe-coding-assignment/tree/sdd_submission) branch.
> * To view the final version featuring the vibe-coded password encryption gateway, switch to the [vibe_coded_submission](https://github.com/anweshasingh-dev/sdd-vs-vibe-coding-assignment/tree/vibe_coded_submission) branch.

---

## Overview & Methodology

This project showcases two distinct software engineering paradigms across different Git branches to evaluate development efficiency and software robustness:

1. **Spec-Driven Development (SDD):** The core application structure (diary entries, habit tracking, and UI layout) was built by strictly following upfront markdown specifications to ensure explicit architectural planning and clear state management.
2. **Vibe Coding:** A separate security layer (password encryption gateway) was iteratively implemented using high-level prompting and rapid AI-assisted execution to quickly prototype and deploy the feature.

---

## Features Across Branches

* **Secure Diary Entries:** Create, view, and organize daily thoughts with local persistent storage *(Available on all branches)*.
* **Habit Tracking:** Log and track daily habits seamlessly alongside your journal entries to monitor personal growth *(Available on all branches)*.
* **Password Encryption Gateway:** A secure login layer implemented during the vibe-coding phase to restrict unauthorized diary access *(Available on `vibe_coded_submission` branch)*.
* **Modern UI:** A clean, intuitive web interface powered by Streamlit *(Available on all branches)*.
* **Local Storage:** Fast and lightweight data persistence using a structured JSON file *(Available on all branches)*.

---

## Project Structure

The project's architectural backbone is split between structured specs and functional python modules:

```text
├── openspec/               # Specification folder containing initial prompts/guidelines
├── app.py                  # Streamlit UI configuration and entry point
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

To explore the complete feature set (including the password encryption gateway), checkout the vibe-coded branch and run the application:

```bash
git checkout vibe_coded_submission
streamlit run app.py

```

---

## Workshop Takeaways

* Successfully translated abstract requirements into concrete markdown specification files (`design.md`, `tasks.md`, `streamlit_spec.md`) before writing code.
* Mastered the balance between rigid architectural planning (SDD) and rapid, LLM-driven feature iteration (Vibe Coding).
* Leveraged Git branching strategies to cleanly isolate and document different software engineering methodologies.
