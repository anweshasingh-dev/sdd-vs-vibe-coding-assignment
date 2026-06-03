# AI-Assisted Diary & Habit Tracker

**Workshop Certificate:** [](https://www.google.com/search?q=https://drive.google.com/file/d/13Pc-IeH0LEnpyVX-HQYNq7pMQ0DmlQ4V/view%3Fusp%3Dsharing)

A Python-based diary application built as a final project assignment to demonstrate and compare modern AI-assisted workflows. This repository directly contrasts structured **Spec-Driven Development (SDD)** with rapid, LLM-forward **"Vibe Coding"**, developed as part of the *Future of Software Development with LLMs* workshop.

> **Note:** You are currently viewing the **`vibe_coded_submission`** branch, which contains the final feature set including the vibe-coded password encryption gateway.

---

## Overview & Methodology

This project showcases two distinct software engineering paradigms across different Git branches:

1. **Spec-Driven Development (SDD):** The core application structure was built by strictly following upfront markdown specifications to ensure explicit architectural planning and clear state management.
2. **Vibe Coding:** The security layer (password encryption gateway) was iteratively implemented using high-level prompting and rapid AI-assisted execution to quickly prototype and deploy the feature.

---

## Features

* **Password Encryption Gateway:** A secure login layer implemented during the vibe-coding phase to restrict unauthorized diary access.
* **Secure Diary Entries:** Create, view, and organize daily thoughts with local persistent storage.
* **Habit Tracking:** Log and track daily habits seamlessly alongside your journal entries.
* **Modern UI:** A clean, intuitive web interface powered by Streamlit.
* **Local Storage:** Fast and lightweight data persistence using a structured JSON file.

---

## Project Structure

The project's architectural backbone is split between structured specs and functional python modules:

```text
├── openspec/               # Specification folder containing initial prompts/guidelines
├── app.py                  # Main Streamlit entry point (with Password Encryption Gateway)
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
git clone https://github.com/anweshasingh-dev/sdd-vs-vibe-coding-assignment.git
cd sdd-vs-vibe-coding-assignment

```

Install the required dependencies:

```bash
pip install streamlit

```

### 3. Running the App

To run this branch's final feature-complete build containing the password feature, execute the main `app.py` script:

```bash
git checkout vibe_coded_submission
streamlit run app.py

```

---

## Workshop Takeaways

* Successfully translated abstract requirements into concrete markdown specification files (`design.md`, `tasks.md`, `streamlit_spec.md`) before writing code.
* Mastered the balance between rigid architectural planning (SDD) and rapid, LLM-driven feature iteration (Vibe Coding).
* Leveraged Git branching strategies to cleanly isolate and document different software engineering methodologies.
