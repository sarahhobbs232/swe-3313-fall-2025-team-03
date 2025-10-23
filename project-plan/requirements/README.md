## 🧠 Requirements Introduction

**Project:** Eternal Elixirs (Online Potion Shop)  
**Team:** 03  
**Version:** 1 

---

After a thorough conversation with our customer, we identified the essential functionalities, features, and processes required for the success of **Eternal Elixirs**, our online potion shop.

Overall, we deliver a full potion shopping experience with the help of intelligent user account, active inventory browsing, and secure checkout. Users are able to self-register, and use unique credentials to log in, whereas admins are not able to self-register. The inventory shows the available potions in descending order of price and each of them has a name, image, price in USD, a brief description and an add to cart button. The customers are also able to search the catalog based on keywords which are included in item names or descriptions, see and edit their cart and checkout only when they have items in them. At the checkout, the user will type in shipping, payment and desired shipping speed and the system will compute subtotal, 6 percent tax and shipping after which the order is confirmed. After making a purchase, the system will remove the sold products off the shelf, and will produce a comprehensive receipt with the final 4 digits of the card and shipping address, which will be displayed on the browser as an email copy. Administrators are allowed to have users promoted to the role of an administrator, see sales reports, and to export these reports in CSV format. The interface also has all the major screens as high-fidelity mockups, and the prices are recorded in base-10 decimal and are represented in usual USD currency (e.g., $1,234.56).

The detailed requirements that were elicited from the aforementioned conversation are detailed ['here'](project-plan/requirements/elicitation.md)

---
or:

After a thorough conversation with our customer, we identified the essential functionalities, features, and processes required for the success of **Eternal Elixirs**, our online potion shop.

This repository section summarizes the scope and artifacts for **Version 1** of Eternal Elixirs. V1 delivers the core shopping flow and minimal admin features required for launch:

- **User Accounts:** self-registration, login (admins cannot self-register).
- **Inventory:** browse only *available* items, sorted high→low price; each shows name, image, price (USD), short description, and “Add to Cart”.
- **Search:** keyword search over item names and descriptions.
- **Cart & Checkout:** view/modify cart, block empty checkout, collect shipping + payment + shipping speed, compute **subtotal + 6% tax + shipping** before confirmation.
- **Order Completion & Receipt:** remove purchased items from inventory; show receipt with last 4 digits of card and shipping address; render a copy in-browser as the “email”.
- **Admin:** promote user to admin, view sales report, export report to **CSV**.
- **UI & Data Formatting:** high-fidelity mockups for key screens; prices stored as **base-10 decimal** and displayed in USD (e.g., `$1,234.56`).

The detailed requirements that were elicited from the aforementioned conversation are detailed ['here'](project-plan/requirements/elicitation.md)

---

## 📊 Documentation Links 
**Full Requirements:** 
- Click [`here`](project-plan/requirements/REQUIREMENTS.md) for the full outline of the requirements.

**Use Case Diagram:**
- Click [`here`](project-plan/requirements/use-case.md) for a detailed Use-Case Diagram for our project.

**Decision Table:**
- Click [`here`](project-plan/requirements/decision-table.md) for a detailed view of our Decision Table for all processes in Version 1.

**Requirements Presentation (Loom):**
- Click ['here'](loomlink) to view our Requirements presentation in Loom.
