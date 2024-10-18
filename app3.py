import streamlit as st
import requests  # To make HTTP requests to the API

# Function to fetch vehicle details from API
def fetch_vehicle_details(id_type, id_number):
    # Replace with the real API endpoint
    api_url = "https://api.sindh-excise-vehicle.com/vehicle_search"
    
    # Sample API headers and parameters (this will depend on the API provider)
    params = {
        'id_type': id_type,
        'id_number': id_number
    }
    
    # Replace with your actual API key if required
    headers = {
        'Authorization': 'Bearer YOUR_API_KEY_HERE'
    }
    
    # Make the request to the API
    response = requests.get(api_url, params=params, headers=headers)
    
    if response.status_code == 200:
        return response.json()  # Return the JSON response if successful
    else:
        return None  # Return None if there was an error

# Streamlit app for vehicle inquiry
def vehicle_inquiry_app():
    st.title("Sindh Vehicle Registration Inquiry")

    st.subheader("Enter Vehicle Identification Information")

    # Select either Engine Number, Chassis Number, or Vehicle Number
    id_type = st.selectbox("Search via", ("Vehicle Number", "Engine Number", "Chassis Number"))

    # Input field for the selected ID type
    id_number = st.text_input(f"Enter {id_type}")

    # Submit button to search for vehicle
    if st.button("Search"):
        # Fetch vehicle details from the API
        vehicle_info = fetch_vehicle_details(id_type, id_number)

        if vehicle_info:
            st.success("Vehicle found!")
            # Display vehicle information
            st.write(f"**Owner Name:** {vehicle_info['owner_name']}")
            st.write(f"**Vehicle Number:** {vehicle_info['vehicle_number']}")
            st.write(f"**Engine Number:** {vehicle_info['engine_number']}")
            st.write(f"**Chassis Number:** {vehicle_info['chassis_number']}")
            st.write(f"**Model:** {vehicle_info['model']}")
            st.write(f"**Color:** {vehicle_info['color']}")
            st.write(f"**Fuel Type:** {vehicle_info['fuel_type']}")
        else:
            st.error(f"No vehicle found with {id_type}: {id_number}")

# Main function
if __name__ == "__main__":
    vehicle_inquiry_app()
