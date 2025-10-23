"""
Decision Table Logic
-----------------------------
Implements the 4 use-cases (split into 5 tables total) with explicit if/elif/else
branches that mirror your decision tables and R1..Rx meanings.
"""
def login_flow(admin_actor, self_register_attempt, username_unique, password_ge6, credentials_valid):
    """
    LOGIN rules (R1..R6)
    Returns list of actions.
    """
    actions = []
    if self_register_attempt and admin_actor:
        actions.append("Error: Admins cannot self-register")  # R2
        return actions
    if self_register_attempt:
        if not username_unique:
            actions.append("Error: Username taken")  # R3
        elif not password_ge6:
            actions.append("Error: Password too short")  # R4
        else:
            actions.append("Register user (standard)")  # R1
        return actions
    if credentials_valid:
        actions.append("Start session")
        if admin_actor:
            actions.append("Admin: dashboard ready")  # R6
        else:
            actions.extend([
                "Show inventory (price desc)",
                "Item UI: name, picture(s), price, desc, Add-to-Cart",
                "Price formatting: $#,###.## (2dp)",
            ])  # R5
        return actions
    return actions

def find_purchase_search_cart(inventory_exists, search_query_entered, query_matches,
                              cart_empty_before_checkout, checkout_clicked, cart_empty_after_removals):
    """
    Search & Cart
    Returns list of actions.
    """
    actions = []
    if inventory_exists and search_query_entered:
        if query_matches:
            actions.append("Show search results")  # R1
        else:
            actions.append("Show empty search state")  # R2
        return actions
    if checkout_clicked and cart_empty_before_checkout:
        actions.append("Disable Checkout")  # R3
        return actions
    if checkout_clicked and not cart_empty_before_checkout:
        if cart_empty_after_removals:
            actions.append("Return to main (cart now empty)")  # R5
        else:
            actions.extend([
                "Show Cart with subtotal (+remove)",
                "Allow return to shopping from cart",
            ])  # R4
        return actions
    return actions

def find_purchase_payment_confirm(pay_now_clicked, address_complete, card_complete,
                                  shipping_selected, confirm_clicked, complete_clicked,
                                  email_service_available):
    """
    Payment & Confirm
    Returns list of actions.
    """
    actions = []
    if pay_now_clicked and not (address_complete or card_complete or shipping_selected or confirm_clicked or complete_clicked):
        actions.append("Open Payment Form")  # R1
        return actions
    details_complete = address_complete and card_complete and shipping_selected
    if confirm_clicked and not details_complete:
        actions.append("Show error: incomplete details (stay on Payment Form)")  # R2
        return actions
    if confirm_clicked and details_complete and not complete_clicked:
        actions.extend([
            "Show Confirm (items, ship, total)",
            "Apply shipping cost ($29/$19/$0)",
        ])  # R3
        return actions
    if complete_clicked and details_complete:
        actions.append("Complete: decrement inventory + add to sales report")
        if email_service_available:
            actions.append("Show receipt + email receipt")  # R4
        else:
            actions.append("Show receipt (no email)")        # R5
        actions.append("Lock back-navigation from checkout")
        actions.append("Refresh main (remove purchased items)")
        return actions
    return actions

def manage_inventory(admin_logged_in, add_item_clicked, update_item_clicked,
                     delete_item_clicked, export_csv_clicked, item_data_valid):
    """
    MANAGE INVENTORY rules (R1..R6)
    Returns list of actions.
    """
    actions = []
    if not admin_logged_in and (add_item_clicked or update_item_clicked or delete_item_clicked or export_csv_clicked):
        actions.append("Error: admin privileges required")  # R6
        return actions
    if admin_logged_in:
        if add_item_clicked:
            if item_data_valid:
                actions.append("Add inventory item")  # R1
            else:
                actions.append("Error: invalid item data")  # R2
            return actions
        if update_item_clicked:
            if item_data_valid:
                actions.append("Update inventory item")  # R3
            else:
                actions.append("Error: invalid item data")
            return actions
        if delete_item_clicked:
            actions.append("Delete inventory item")  # R4
            return actions
        if export_csv_clicked:
            actions.append("Admin: export CSV")  # R5
            return actions
    return actions

def view_sales_report(admin_logged_in, report_data_available, export_csv_clicked, receipt_item_clicked):
    """
    VIEW SALES REPORT rules (R1..R5)
    Returns list of actions.
    """
    actions = []
    if not admin_logged_in and (export_csv_clicked or receipt_item_clicked or report_data_available):
        actions.append("Error: admin privileges required")  # R5
        return actions
    if admin_logged_in and not report_data_available:
        actions.append("Show empty-report state")  # R4
        return actions
    if admin_logged_in and report_data_available:
        if export_csv_clicked:
            actions.append("Admin: export CSV")  # R2
            return actions
        if receipt_item_clicked:
            actions.append("Open receipt detail (click-through)")  # R3
            return actions
        actions.append("Show report (items + purchaser)")  # R1
        return actions
    return actions

if __name__ == "__main__":
    # Simple demos
    print("Login example:", login_flow(False, False, True, True, True))
    print("Search example:", find_purchase_search_cart(True, True, True, True, False, False))
    print("Payment example:", find_purchase_payment_confirm(True, True, True, True, True, True, True))
    print("Manage inv example:", manage_inventory(True, True, False, False, False, True))
    print("Report example:", view_sales_report(True, True, True, False))
