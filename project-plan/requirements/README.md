# 🧾 Requirements — Version 1  

**Project:** Eternal Elixirs (Online Potion Shop)
**Team:** 03  
**Version:** 1 (Must Have Features)

---

## 🧠 Summary
After a detailed discussion with our customer, we identified the essential functionalities required for a successful first release.  
Version 1 focuses on *user account management, inventory browsing, checkout processing,* and *administrative reporting*.  
The system ensures price accuracy, prevents visibility of sold items, and delivers a clean, high-fidelity user interface.

---

## 📦 T3E-1 — User Account Management  

### 🔹 T3S-1 — Register a New User  
- **Priority:** Must Have  
- **Effort:** 1 day  
- **Type:** Functional  
- **Description:**  
  Users must be able to self-register with a unique username and password (minimum 6 characters). Admins cannot self-register.  

### 🔹 T3S-2 — Log In as a Registered User  
- **Priority:** Must Have  
- **Effort:** 0.5 day  
- **Type:** Functional  
- **Description:**  
  Registered users must be able to log in with validated credentials and be directed to the main inventory page upon success.  

---

## 🛒 T3E-2 — Inventory Browsing and Search  

### 🔹 T3S-3 — View Inventory  
- **Priority:** Must Have  
- **Effort:** 1 day  
- **Type:** Functional  
- **Description:**  
  The system must list all available items sorted from highest to lowest price, each showing a name, at least one image, price, short description, and “Add to Cart” button. Sold items must be excluded.  

### 🔹 T3S-4 — Search Inventory  
- **Priority:** Must Have  
- **Effort:** 1 day  
- **Type:** Functional  
- **Description:**  
  Users must be able to search inventory by keywords matching item names or descriptions.  

---

## 💰 T3E-3 — Shopping Cart and Checkout  

### 🔹 T3S-5 — Add Item to Cart  
- **Priority:** Must Have  
- **Effort:** 0.5 day  
- **Type:** Functional  
- **Description:**  
  Users can add one or more items to their shopping cart from the inventory list.  

### 🔹 T3S-6 — View and Modify Cart  
- **Priority:** Must Have  
- **Effort:** 1 day  
- **Type:** Functional  
- **Description:**  
  Users can view all items in their cart, see the subtotal (USD), and remove items. If all items are removed, the system returns to the main screen automatically.  

### 🔹 T3S-7 — Checkout Process  
- **Priority:** Must Have  
- **Effort:** 2 days  
- **Type:** Functional  
- **Description:**  
  Checkout is available only when the cart is not empty.  
  The page collects shipping address, phone number, credit card info (number, expiration date, CVV), and shipping speed (Overnight $29, 3-Day $19, Ground Free). All fields required.  

### 🔹 T3S-8 — Confirm and Complete Order  
- **Priority:** Must Have  
- **Effort:** 1.5 days  
- **Type:** Functional  
- **Description:**  
  The confirmation page displays the item list, subtotal, 6% tax, shipping cost, and grand total.  
  Clicking **Complete Order** finalizes the purchase, removes items from inventory, and displays the receipt.  

### 🔹 T3S-9 — Display Receipt  
- **Priority:** Must Have  
- **Effort:** 1 day  
- **Type:** Functional  
- **Description:**  
  After order completion, show a receipt including items purchased, subtotal, tax, shipping cost, grand total, last four digits of card, and shipping address. User can click **OK** to return home.  

---

## 🧮 T3E-4 — Administration and Reporting  

### 🔹 T3S-10 — Promote User to Admin  
- **Priority:** Must Have  
- **Effort:** 0.5 day  
- **Type:** Functional  
- **Description:**  
  Admins must be able to promote a registered user to admin status via an internal process.  

### 🔹 T3S-11 — View Sales Report  
- **Priority:** Must Have  
- **Effort:** 1 day  
- **Type:** Functional  
- **Description:**  
  Admins can view a sales report listing all purchases, buyers, and total amounts.  

### 🔹 T3S-12 — Export Sales Report to CSV  
- **Priority:** Must Have  
- **Effort:** 0.5 day  
- **Type:** Functional  
- **Description:**  
  The system must export sales reports to CSV for external analysis (e.g., Excel).  

---

## 🎨 T3E-5 — User Interface and Mockups  

### 🔹 T3S-13 — Create High-Fidelity UI Mockups  
- **Priority:** Must Have  
- **Effort:** 1.5 days  
- **Type:** Non-Functional  
- **Description:**  
  The team must produce a high-fidelity mockup of all key screens (registration, login, inventory, cart, checkout, and admin) to demonstrate final appearance before development.  

---

## 💾 T3E-6 — Data and Formatting  

### 🔹 T3S-14 — Ensure Price Accuracy  
- **Priority:** Must Have  
- **Effort:** 0.5 day  
- **Type:** Non-Functional  
- **Description:**  
  All prices must be stored in base-10 decimal/currency format (not floating point) and displayed in USD (e.g., `$1,234.56`).  

---

## 📊 Documentation Links  

- **Use-Case Diagram:** 
- **Decision Table:**  
- **Requirements Presentation (Loom):** 
