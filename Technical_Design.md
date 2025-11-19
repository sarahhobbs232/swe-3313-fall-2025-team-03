# Technical Design

## Table of Contents
- [Implementation Languages](#implementation-languages) 
- [Implementation Frameworks](#implementation-frameworks) 
- [Data Storage Plan](#data-storage-plan)
- [Entity Relationship Diagram](#entity-relationship-diagram)
- [Entity/Field Descriptions](#entityfield-descriptions)
- [Data Examples](#data-examples)
- [Database Seed Data](#database-seed-data)
- [Authentication and Authorization Plan](#authentication-and-authorization-plan) 
- [Coding Conventions](#coding-conventions) 

---

# Implementation Languages

Eternal Elixirs will be implemented using **Python 3**, **HTML5**, **CSS3**, and **JavaScript**.

### Python 3
- Main backend language responsible for routes, logic, authentication, and data writing.
- Lightweight, readable, and ideal for small e-commerce applications.
- Strong ecosystem (Flask, Werkzeug, JSON, Decimal).
- Docs: https://docs.python.org/3/

### HTML5
- Used to structure the pages rendered through Jinja2 templates.

### CSS3
- Controls layout, visuals, spacing, typography, and responsive design.
- Styled alongside Bootstrap 5 for consistency.

### JavaScript (Vanilla)
- Minimal usage for dynamic UI behavior such as form validation or disabling actions.
- MDN Docs: https://developer.mozilla.org/en-US/docs/Web/JavaScript

---

# Implementation Frameworks

Eternal Elixirs uses the following frameworks and libraries:

### Flask
- Lightweight web framework designed for clean routing and quick development.
- Ideal for a small-scale e-commerce system.
- Supports modular blueprints.
- Docs: https://flask.palletsprojects.com/

### Jinja2
- Templating engine used to generate HTML using dynamic variables, loops, and conditions.
- Enables clean separation between backend logic and UI.

### Bootstrap 5
- Provides responsive UI components that reduce the need for heavy custom CSS.
- Used to match the Marvel mockups.
- Docs: https://getbootstrap.com/

### Werkzeug Security
- Handles password hashing and secure password checks.

### Python Decimal Module
- Handles currency operations with proper precision.
- Prevents floating-point rounding errors during checkout.

---

# Data Storage Plan



---

# Entity Relationship Diagram

<img width="468" height="214" alt="image" src="https://github.com/user-attachments/assets/3b9d8326-e391-4c72-9eb6-dbe08559d826" />


---

# Entity/Field Descriptions

<!-- User Entity -->
<img width="468" height="116" alt="image" src="https://github.com/user-attachments/assets/7dde957e-d532-4220-9fd3-ad88ef34e42a" />

<!-- Bill Entity -->
<img width="469" height="106" alt="image" src="https://github.com/user-attachments/assets/99a68c40-e9cf-43b3-a948-f525e82581a1" />

<!-- Bill Inventory Item Entity -->
<img width="468" height="51" alt="image" src="https://github.com/user-attachments/assets/14323355-e00c-43e0-bfac-c6001efd3249" />

<!-- Inventory Entity -->
<img width="468" height="71" alt="image" src="https://github.com/user-attachments/assets/1823b380-3ebb-48fc-b852-ade87132adbf" />

<!-- Shopping Cart Entity -->
<img width="468" height="62" alt="image" src="https://github.com/user-attachments/assets/8cfc60d9-5d4b-414e-a0e1-73d7c4158838" />

<!-- Shipping Entity -->
<img width="468" height="50" alt="image" src="https://github.com/user-attachments/assets/9d0b49f5-b299-4ce1-8ec1-699d3a6eeefa" />






---

# Data Examples

### User Table:

<img width="468" height="35" alt="image" src="https://github.com/user-attachments/assets/ef0a3f08-acd8-473b-84ff-49d762bd0257" />

### Shopping Cart Table:

<img width="468" height="64" alt="image" src="https://github.com/user-attachments/assets/932e34c4-cf6b-458d-bb04-3611b79bed49" />

### Bill Table

<img width="468" height="68" alt="image" src="https://github.com/user-attachments/assets/3827d1e2-bf14-4254-952a-f49a3a46192f" />
<img width="468" height="69" alt="image" src="https://github.com/user-attachments/assets/b46cf2bc-c5fb-443f-9e47-042cd7fd8f4e" />

### Bill Inventory Item:

<img width="468" height="80" alt="image" src="https://github.com/user-attachments/assets/aceb858f-dfef-4986-a14c-16a3613c6517" />


---

# Database Seed Data

### Inventory Table:
<img width="468" height="40" alt="image" src="https://github.com/user-attachments/assets/bd222902-833d-4700-bbc6-221edefac437" />

### Shipping Table:

<img width="468" height="78" alt="image" src="https://github.com/user-attachments/assets/9ad88fbd-9f50-4cd8-ba93-1703131ffb51" />

### Admin Table:

<img width="468" height="28" alt="image" src="https://github.com/user-attachments/assets/cd077999-e672-4304-ab21-f86adcb7e86c" />


---

# Authentication and Authorization Plan

Authentication = verifying identity.  
Authorization = determining permissions.

### Authentication Flow
1. User submits username and password.
2. System searches for username (case-insensitive).
3. Password hashed and verified via:
   ```python
   check_password_hash(stored_hash, submitted_password)
   ```
4. If valid, the following values are stored in `session`:
   ```python
   session["user_id"]
   session["username"]
   session["is_admin"]
   ```
5. User is redirected to the inventory screen.

### Admin Account Rules
- Admins **cannot** self-register.
- Admins must be **promoted manually** by another admin.

---

### Authorization Logic

#### Decorators
```python
def login_required(view):
    @wraps(view)
    def wrapper(*args, **kwargs):
        if "user_id" not in session:
            return redirect(url_for("auth.login"))
        return view(*args, **kwargs)
    return wrapper

def admin_required(view):
    @wraps(view)
    @login_required
    def wrapper(*args, **kwargs):
        if not session.get("is_admin"):
            abort(403)
        return view(*args, **kwargs)
    return wrapper
```

### User Permissions
Regular users can:
- Browse inventory
- Search inventory
- Add items to cart
- Checkout
- View receipts

### Admin Permissions
Admins can:
- Add/edit inventory
- Generate sales reports
- Export reports to CSV
- Promote users to admin

### Admin Promotion Flow
1. Admin selects a user.
2. Backend sets `is_admin = True`.
3. Event is logged in `promotion_requests.json`.

---

# Coding Conventions

### Python Style
- Follow **PEP 8** (https://peps.python.org/pep-0008/).
- Use `snake_case` for variables/functions.
- Use `PascalCase` for class names.
- Provide docstrings for all public functions.
- No commented-out code left behind.

### Project Folder Structure
```
app.py
/auth/                 # login, register, logout
/shop/                 # inventory, search, cart, checkout
/admin/                # reports, export, add inventory
/data/                 # JSON files + repository logic
/templates/            # HTML templates (Jinja2)
static/                # CSS, JS, images
```

### Git Workflow
- `main` is protected.
- Work is done in:
  - `feature/<name>`
  - `fix/<name>`
  - `docs/<name>`
- All PRs must:
  - Include description
  - Pass tests
  - Be reviewed by a teammate

### Commenting & Documentation
- Use descriptive variable names (`shipping_usd`, `total_price`, etc.).
- Add inline comments for complex logic (money calculations, file locking).
- Keep logic inside views small by separating it into helper functions.

---

