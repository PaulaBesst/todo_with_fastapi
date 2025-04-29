import streamlit as st
import requests

API_URL = "http://localhost:8000/api"

st.title("📝 Todo App")

# --- Add Todo ---
st.header("➕ Add a Todo")
task = st.text_input("Enter Task")
done = st.checkbox("Mark as Done")

if st.button("Add Todo"):
    if task.strip() == "":
        st.warning("⚠️ Task cannot be empty.")
    else:
        payload = {"task": task, "done": done}
        response = requests.post(f"{API_URL}/", json=payload)
        if response.status_code == 200:
            st.success("✅ Todo added successfully!")
        else:
            st.error("❌ Failed to add todo.")
            st.write(response.text)

# --- View Todos ---
st.header("📋 My Todos")
response = requests.get(f"{API_URL}/")
if response.status_code == 200:
    todos = response.json()
    for todo in todos:
        col1, col2, col3 = st.columns([6, 1, 1])
        with col1:
            st.write(todo["task"])
        with col2:
            checked = st.checkbox("Done", value=todo["done"], key=todo["id"])
            if checked != todo["done"]:  # Only call PUT if changed
                update_payload = {"done": checked}
                requests.put(f"{API_URL}/{todo['id']}", json=update_payload)
        with col3:
            if st.button("🗑️", key=f"delete_{todo['id']}"):
                requests.delete(f"{API_URL}/{todo['id']}")
                st.rerun()
else:
    st.error("⚠️ Failed to fetch todos.")
