## 👥 Team Assignments — Eternal Elixers

Our team, **Eternal Elixers**, is building a potion-based e-commerce platform that sells one-of-a-kind magical items. Below is a breakdown of our members, their roles, and how responsibilities are distributed throughout the project.

---

### 🧩 Team Members

| Name | KSU Email | Primary Role | Resume |
|------|------------|---------------|--------|
| **Sarah Hobbs** | shobbs17@students.kennesaw.edu | Project Manager / UX Designer | [View Resume](project-plan/team-assignments/project-plan/resumes/resume-sarah.md) |
| **Eric Jones** | ejone254@student.kennesaw.edu | Backend Developer / API Lead | [View Resume](project-plan/resumes/resume-eric.md) |
| **Kyle Kolb** | kkolb3@students.kennesaw.edu | Integration & Testing Lead | [View Resume](project-plan/resumes/resume-kyle.md) |
| **Hazim Mahmood** | hmahmoo2@students.kennesaw.edu | Data & DevOps Engineer | [View Resume](project-plan/resumes/resume-hazim.md) |

Each member contributes to all major project phases while maintaining ownership over specific deliverables.

---

### ⚙️ Roles and Responsibilities

#### **Sarah Hobbs — Project Manager / UX Designer**
- Coordinates meetings, task assignments, and milestone tracking  
- Leads **project documentation**, markdown formatting, and presentation organization  
- Designs the **Marvel high-fidelity mockups** and ensures usability and accessibility  
- Oversees Loom recordings and presentation planning  
- Primary reviewer for repository structure and markdown link consistency  

#### **Eric Jones — Backend Developer / API Lead**
- Develops the **Flask application structure**, blueprints, and routes  
- Handles **user authentication**, registration, and session management  
- Implements **checkout logic**, tax/shipping calculations, and order validation  
- Maintains code quality and implements `pytest` unit tests for backend components  
- Supports JSON data integration and API error handling  

#### **Kyle Kolb — Integration & Testing Lead**
- Manages **feature integration**, ensuring compatibility between backend and frontend  
- Builds and executes the **testing pipeline** using `pytest` and GitHub Actions  
- Verifies UI alignment with Marvel mockups  
- Leads debugging, code reviews, and overall code reliability  
- Assists with UI layout and input validation logic  

#### **Hazim Mahmood — Data & DevOps Engineer**
- Designs and maintains the **JSON data structure** for inventory, users, and sales  
- Implements **data persistence** with atomic write protection and read locks  
- Develops **CSV export** functionality for sales reports  
- Manages Git branching, version control, and environment setup (`virtualenv`)  
- Prepares future migration plan from **JSON → SQLite** if needed  

---

### 📅 Deliverable Ownership by Milestone

| Milestone | Owner | Key Deliverables |
|------------|--------|------------------|
| **Project Plan** | Sarah | Repo setup, team resumes, assignments page, tech selection, Gantt chart, Loom video |
| **Requirements** | Sarah (lead) / Eric (support) | Requirement stories, priorities, use-case diagram, decision table, Loom |
| **UI Design (Marvel)** | Sarah (lead) / Kyle (support) | Interactive mockups, screen flow, user journey diagrams |
| **Technical Design** | Hazim (lead) / Eric (support) | ERD, field descriptions, seed data, storage plan, style guide, Loom |
| **Implementation** | Eric (lead) / Hazim & Kyle (support) | Flask app, user auth, checkout, sales reports, testing, README setup |
| **Final Presentation** | Sarah (lead) / All | Live demo, feature walk-through, Marvel vs Implementation comparison |

---

### 🧭 Collaboration Guidelines

- **Meetings:** Twice per week (30–45 minutes) via GroupMe Calls  
- **Communication:** GroupMe (primary) + GitHub Issues for tasks  
- **Branching Strategy:**  
  - `main` (protected) — stable code only  
  - `feature/*`, `fix/*`, `docs/*` branches for all work  
- **Pull Requests:** At least **one reviewer required**; no self-merges  
- **Definition of Done:** Code compiles, passes tests, matches Marvel mockup for scope, documentation updated  

---

### ⚠️ Key Risk Owners

| Risk | Owner | Mitigation |
|------|--------|------------|
| **Currency precision (USD)** | Eric | Use Python `Decimal` type and enforce formatting to two decimals |
| **Double-sell of unique items** | Hazim | Check inventory before commit; atomic write to JSON |
| **JSON corruption or data loss** | Hazim | File locks and temp-rename write strategy |
| **Markdown link errors** | Kyle | Run link verification before submission |
| **Schedule slip** | Sarah | Monitor Gantt predecessors and deadlines weekly |

---

Together, our team aims to deliver a clean, user-friendly potion marketplace that demonstrates strong software engineering principles and teamwork.
