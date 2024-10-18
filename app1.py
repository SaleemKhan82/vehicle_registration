import streamlit as st

# Function to display vehicle registration form
def vehicle_registration():
    st.title("Vehicle Registration App")

    st.subheader("Select the type of vehicle")
    vehicle_type = st.radio("Vehicle Type:", ('2-Wheeler', '4-Wheeler'))

    st.subheader("Enter Vehicle Identification Details")
    
    # Select either Engine Number, Chassis Number, or Vehicle Number
    id_type = st.selectbox("Register via", ("Vehicle Number", "Engine Number", "Chassis Number"))

    # Input field for selected ID type
    if id_type == "Vehicle Number":
        id_number = st.text_input("Enter Vehicle Number")
    elif id_type == "Engine Number":
        id_number = st.text_input("Enter Engine Number")
    else:
        id_number = st.text_input("Enter Chassis Number")
    
    st.subheader("Enter Other Vehicle Details")
    
    owner_name = st.text_input("Owner Name")
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

    # Submit button
    if st.button("Submit"):
        # Display entered data after submission
        st.success(f"Vehicle Registered Successfully!")
        st.write(f"**Owner Name:** {owner_name}")
        st.write(f"**Vehicle Type:** {vehicle_type}")
        st.write(f"**Identification Type:** {id_type}")
        st.write(f"**{id_type}:** {id_number}")
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
