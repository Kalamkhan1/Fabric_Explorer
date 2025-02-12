import streamlit as st
import requests



def app():
    # Base URL of your Express.js API
    BASE_URL = "http://localhost:5000/api/fabrics"  # Replace with your actual API URL

    # Page title
    st.title("Fabric Explorer")

    # Select mode: Search or Compare

    search,compare= st.tabs(["Search Fabrics","Compare Fabrics"])

    with search:
        # Search options
        search_type = st.selectbox(
            "Search by:",
            ["Name", "Type", "Durability", "Texture", "Best Use"]
        )

        # Input field for search
        search_query = st.text_input(f"Enter the {search_type.lower()} of the fabric:")

        # Submit button
        if st.button("Search"):
            if search_query:
                # Map search type to API endpoints
                endpoint_mapping = {
                    "Name": f"/name/{search_query}",
                    "Type": f"/type/{search_query}",
                    "Durability": f"/durability/{search_query}",
                    "Texture": f"/texture/{search_query}",
                    "Best Use": f"/best-use/{search_query}",
                }

                # Construct the API URL
                endpoint = endpoint_mapping[search_type]
                url = f"{BASE_URL}{endpoint}"

                # Make the API call
                try:
                    response = requests.get(url)
                    response.raise_for_status()  # Raise an error for HTTP codes like 404, 500

                    # Parse the JSON response
                    fabric_data = response.json()  # Already in JSON format
                    print(fabric_data)

                    # Display results
                    if fabric_data:
                        st.write(f"#### {search_type}: {search_query}")
                        for fabric in fabric_data if isinstance(fabric_data, list) else [fabric_data]:
                            st.write(f"**Fabric Name**: {fabric.get('FabricName', 'N/A')}")
                            st.write(f"**Type**: {fabric.get('FabricType', 'N/A')}")
                            st.write(f"**Durability**: {fabric.get('Durability', 'N/A')}")
                            st.write(f"**Texture**: {fabric.get('Texture', 'N/A')}")
                            st.write(f"**Best Use**: {', '.join(fabric.get('BestUse', []))}")
                            st.write("---")  # Separator between results
                    else:
                        st.warning(f"No fabrics found for {search_type.lower()} '{search_query}'.")
                except requests.exceptions.RequestException as e:
                    st.error(f"Error connecting to API: {e}")
            else:
                st.warning("Please enter a value to search.")

    with compare:
        st.subheader("Compare Fabrics")
        compare_query = st.text_input("Enter fabric names to compare (comma-separated):")

        # Compare button
        if st.button("Compare"):
            if compare_query:
                # Construct the API URL
                url = f"{BASE_URL}/compare/{compare_query}"

                # Make the API call
                try:
                    response = requests.get(url)
                    response.raise_for_status()  # Raise an error for HTTP codes like 404, 500

                    # Parse the JSON response
                    result = response.json()
                    fabrics = result.get("fabrics", [])
                    missing_names = result.get("missingNames", [])
                    print(result)

                    # Display comparison results
                    if fabrics:
                        st.subheader(f"Comparison Results for: {compare_query}")

                        # Create columns for side-by-side display
                        columns = st.columns(len(fabrics))  # Create as many columns as there are fabrics
                        for idx, fabric in enumerate(fabrics):
                            with columns[idx]:  # Assign each fabric to a separate column
                                st.write(f"**Fabric Name**: {fabric.get('FabricName', 'N/A')}")
                                st.write(f"**Type**: {fabric.get('FabricType', 'N/A')}")
                                st.write(f"**Durability**: {fabric.get('Durability', 'N/A')}")
                                st.write(f"**Texture**: {fabric.get('Texture', 'N/A')}")
                                st.write(f"**Best Use**: {', '.join(fabric.get('BestUse', []))}")

                        # Handle missing names
                        if missing_names:
                            st.warning(f"The following fabrics were not found: {', '.join(missing_names)}")
                    else:
                        st.warning(f"No matching fabrics found for: {compare_query}")
                except requests.exceptions.RequestException as e:
                    st.error(f"Error connecting to API: {e}")
            else:
                st.warning("Please enter fabric names to compare.")
if __name__ == "__main__":
    app()
