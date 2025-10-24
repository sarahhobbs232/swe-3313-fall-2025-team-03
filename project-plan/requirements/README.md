# 🧾  Requirements 

**Project:** Eternal Elixirs (Online Potion Shop)
**Team:** 03  
**Version:** 1 (Must Have Features)

## ✅ MUST HAVE

### 🔐 User Authentication
- Users can **log in** and **self-register**
- Admins **cannot self-register**
- **Usernames must be unique**
- **Passwords must be at least 6 characters**

### 🧾 Admin Capabilities
- Admin has elevated privileges:
  - Can **run sales reports**
  - Can **add inventory**
- Admins must be **promoted by another admin** (cannot self-register)

### 🛒 Inventory Display
- Upon login, users see **all available inventory**
  - Sorted **highest to lowest price**
  - Each item includes:
    - Name
    - Picture
    - Price (formatted in USD: `$1,234.56`)
    - Brief description
    - “Add to Cart” button
- Prices stored in **base-10 decimal format**

### 🔍 Search Functionality
- Users can search inventory via **search box**
- Search matches **item name** or **description**

### 💳 Checkout Flow
- Users click **checkout** to begin payment
- **Cannot checkout if cart is empty**
- Checkout page shows:
  - List of items in cart
  - Subtotal
  - Option to **remove items**
    - If cart is emptied, return to **main screen**
- “Pay Now” button starts payment process
  - User enters:
    - Address
    - Credit card number, CVV, Expiration Date
    - Shipping address
  - Shipping speed options:
    - Overnight: `$29`
    - 3-Day: `$19`
    - Ground: `$0` (Free)
- After form completion, user clicks **Confirm Order**
  - Confirm page shows:
    - Item list (name + price only)
    - Shipping cost
    - **Grand total**
- User clicks **Complete Order** to finalize
  - Items are removed from inventory
  - Receipt is shown and **emailed to user**
  - User clicks **Okay** to exit receipt
  - Cannot return to checkout page
  - Purchased items are removed from main inventory
  - Items are added to **sales report**

### 📊 Sales Reporting
- Admin can run **sales report**
  - Shows all purchases and who bought them

### 🖼️ UI Design
- Create **high-fidelity mockups** of:
  - Registration
  - Login
  - Inventory
  - Cart
  - Checkout
  - Admin dashboard

---

## 🧩 NEEDS TO HAVE

### 📤 Exporting Reports
- Admin can **export sales report to CSV**

### 👥 Admin Management
- Admins can **promote registered users** to admin

---

## 💡 WANTS TO HAVE

### 🧑‍💼 Admin Promotion UI
- Simple interface to **transform user into admin**

### 🖼️ Enhanced Inventory
- Support for **multiple pictures per item**

### 📄 Receipt Access
- Admin can **click item in sales report** to view associated receipt

### ➕ Inventory Management
- Admin sees a **pop-up form** to add inventory:
  - Enter item info
  - Upload picture
  - Submit to database
- If too complex, allow **manual database entry**
  - Provide **step-by-step instructions**

