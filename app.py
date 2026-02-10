import streamlit as st
from config import resources, MENU
from storage import load_resources, save_resources
from machine import ingredients_ok, deduct_ingredients

if "resources" not in st.session_state:
    st.session_state.resources = resources.copy()
    load_resources(st.session_state.resources)

st.title("Kaffeeautomat")
col1, col2 = st.columns(2)
with col1:
    if st.button(label="Laden"):
        ok = load_resources(st.session_state.resources)
        if ok:
            st.toast("Zustand geladen", icon="✅")
        else:
            st.info("Keine 'state.csv'-Datei gefunden (default wird geladen).")
with col2:
    if st.button(label="Speichern"):
        save_resources(st.session_state.resources)
        st.toast("Zustand gespeichert", icon="✅")
        
st.subheader("Ressourcen:")
st.write(st.session_state.resources)

st.divider()
st.subheader("Getränke auswählen")

# Getränkeauswahl:
drink_key = st.selectbox(label="Getränk:", options=MENU)
st.write("Preis: ", MENU[drink_key]["price"])
st.write("Benötigt: ", MENU[drink_key]["needs"])

# Sind alle Zutaten vorhanden?
ok, missing = ingredients_ok(drink_key)
if ok:
    st.toast("Zutaten rechen aus", icon="✅")
else:
    st.error(f"Nicht genug Zutaten: {', '.join(missing).capitalize()}")
    
# Button zum Bestellen:
if st.button("Bestellen"):
    if not ok:
        st.error("Bestellung nicht möglich, bitte Zutaten auffüllen.")
    else:
        deduct_ingredients(drink_key)
        save_resources(st.session_state.resources)
        st.toast("Getränk wird zubereitet", icon="✅")
        st.rerun()
    
    