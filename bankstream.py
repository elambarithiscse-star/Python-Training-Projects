import streamlit as st
import json
import os

DATA_FILE = "bank_data.json"

# ---------- Helper functions ----------
def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)


def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                st.warning("JSON file was empty or corrupted. Starting fresh.")
                return {}
    else:
        return {}


# ---------- Streamlit UI ----------
st.set_page_config(page_title="Bank Account Manager", page_icon="🏦", layout="centered")

st.title("🏦 Bank Account Manager")
st.write("Manage bank accounts — create, view, update, or delete.")

data = load_data()

# Sidebar Menu
menu = st.sidebar.radio(
    "Navigation",
    ["Create Account", "Display All Accounts", "Update Account", "Delete Account"]
)

# ---------- Create Account ----------
if menu == "Create Account":
    st.subheader("➕ Create New Account")
    name = st.text_input("Account Holder Name").strip()
    pin = st.text_input("Enter 4-digit PIN", type="password", max_chars=4)
    balance = st.number_input("Initial Balance", min_value=0.0, step=100.0)

    if st.button("Create Account"):
        if not name or not pin:
            st.warning("Please fill in all fields.")
        elif name in data:
            st.error(f"Account for '{name}' already exists!")
        else:
            data[name] = {"account_holder": name, "pin": pin, "balance": balance}
            save_data(data)
            st.success(f"✅ Account for {name} added successfully!")


# ---------- Display Accounts ----------
elif menu == "Display All Accounts":
    st.subheader("📋 All Bank Accounts")

    if not data:
        st.info("No accounts found.")
    else:
        for account in data.values():
            st.write(f"**Name:** {account['account_holder']}")
            st.write(f"**PIN:** {account['pin']}")
            st.write(f"**Balance:** ₹{account['balance']}")
            st.divider()


# ---------- Update Account ----------
elif menu == "Update Account":
    st.subheader("✏️ Update Account")

    if not data:
        st.info("No accounts to update.")
    else:
        names = list(data.keys())
        selected_name = st.selectbox("Select account to update", names)
        update_choice = st.radio("What would you like to update?", ["PIN", "Balance"])

        if update_choice == "PIN":
            new_pin = st.text_input("Enter new 4-digit PIN", type="password", max_chars=4)
            if st.button("Update PIN"):
                if not new_pin:
                    st.warning("Please enter a valid PIN.")
                else:
                    data[selected_name]['pin'] = new_pin
                    save_data(data)
                    st.success(f"✅ PIN updated for {selected_name}")

        elif update_choice == "Balance":
            new_balance = st.number_input("Enter new balance", min_value=0.0, step=100.0)
            if st.button("Update Balance"):
                data[selected_name]['balance'] = new_balance
                save_data(data)
                st.success(f"✅ Balance updated for {selected_name}")


# ---------- Delete Account ----------
elif menu == "Delete Account":
    st.subheader("🗑️ Delete Account")

    if not data:
        st.info("No accounts to delete.")
    else:
        names = list(data.keys())
        selected_name = st.selectbox("Select account to delete", names)

        if st.button("Delete Account"):
            del data[selected_name]
            save_data(data)
            st.success(f"🗑️ Account '{selected_name}' deleted successfully!")


# ---------- Footer ----------
st.markdown("---")
st.caption("© 2025 Bank Account Manager — Built with ❤️ using Streamlit")
