import streamlit as st

# Sample vehicle database (for demo purposes)
# In a real application, this would be a database or an API call
vehicle_database = {
    'ABC123': {
        'owner_name': 'John Doe',
        'vehicle_number': 'ABC123',
        'engine_number': 'ENG5678',
        'chassis_number': 'CHS1234',
        'model': 'Toyota Corolla',
        'color': 'Blue',
        'fuel_type': 'Petrol'
    },
    'XYZ987': {
        'owner_name': 'Jane Smith',
        'vehicle_number': 'XYZ987',
        'engine_number': 'ENG9876',
        'chassis_number': 'CHS9876',
        'model': 'Honda Civic',
        'color': 'Red',
        'fuel_type': 'Diesel'
    }
    # Add more entries as needed
}

# Function to display vehicle details based on user input
def display_vehicle_details(vehicle_info):
    st.write(f"**Owner Name:** {vehicle_info['owner_name']}")
    st.write(f"**Vehicle Number:** {vehicle_info['vehicle_number']}")
    st.write(f"**Engine Number:** {vehicle_info['engine_number']}")
    st.write(f"**Chassis Number:** {vehicle_info['chassis_number']}")
    st.write(f"**Model:** {vehicle_info['model']}")
    st.write(f"**Color:** {vehicle_info['color']}")
    st.write(f"**Fuel Type:** {vehicle_info['fuel_type']}")

# Streamlit app for vehicle inquiry
def vehicle_inquiry_app():
    st.title("Vehicle Registration Inquiry App")

    st.subheader("Enter Vehicle Identification Information")

    # Select either Engine Number, Chassis Number, or Vehicle Number
    id_type = st.selectbox("Search via", ("Vehicle Number", "Engine Number", "Chassis Number"))

    # Input field for the selected ID type
    id_number = st.text_input(f"Enter {id_type}")

    # Submit button to search for vehicle
    if st.button("Search"):
        found_vehicle = None

        # Searching the vehicle in the sample database
        for vehicle in vehicle_database.values():
            if id_type == "Vehicle Number" and vehicle['vehicle_number'] == id_number:
                found_vehicle = vehicle
            elif id_type == "Engine Number" and vehicle['engine_number'] == id_number:
                found_vehicle = vehicle
            elif id_type == "Chassis Number" and vehicle['chassis_number'] == id_number:
                found_vehicle = vehicle

        # If the vehicle is found, display the details
        if found_vehicle:
            st.success("Vehicle found!")
            display_vehicle_details(found_vehicle)
        else:
            st.error(f"No vehicle found with {id_type}: {id_number}")

# Main function
if __name__ == "__main__":
    vehicle_inquiry_app()
