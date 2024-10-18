import streamlit as st

# Function to display vehicle registration form
def vehicle_registration():
    st.title("Vehicle Registration App")

    st.subheader("Select the type of vehicle")
    vehicle_type = st.radio("Vehicle Type:", ('2-Wheeler', '4-Wheeler'))

    st.subheader("Enter Vehicle Details")
    
    owner_name = st.text_input("Owner Name")
    vehicle_number = st.text_input("Vehicle Number")
    model = st.text_input("Vehicle Model")
    registration_year = st.number_input("Registration Year", min_value=1900, max_value=2024, value=2024)
    fuel_type = st.selectbox("Fuel Type", ("Petrol", "Diesel", "Electric", "Hybrid"))
    color = st.text_input("Color")

    # Optional fields based on vehicle type
    if vehicle_type == '4-Wheeler':
        seat_capacity = st.number_input("Seat Capacity", min_value=2, max_value=8, value=5)
        has_ac = st.checkbox("Air Conditioning")
    else:
        has_gears = st.checkbox("Has gears (for bikes)?")

    if st.button("Submit"):
        # Data to be stored/displayed
        st.success(f"Vehicle Registered Successfully!")
        st.write(f"**Owner Name:** {owner_name}")
        st.write(f"**Vehicle Number:** {vehicle_number}")
        st.write(f"**Vehicle Type:** {vehicle_type}")
        st.write(f"**Model:** {model}")
        st.write(f"**Registration Year:** {registration_year}")
        st.write(f"**Fuel Type:** {fuel_type}")
        st.write(f"**Color:** {color}")

        if vehicle_type == '4-Wheeler':
            st.write(f"**Seat Capacity:** {seat_capacity}")
            st.write(f"**Air Conditioning:** {'Yes' if has_ac else 'No'}")
        else:
            st.write(f"**Has Gears:** {'Yes' if has_gears else 'No'}")

# Main function
if __name__ == "__main__":
    vehicle_registration()
