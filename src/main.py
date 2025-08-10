# This script launches the Streamlit UI for the Nigerian Housing Predictor application.
# Import required modules for running subprocesses and handling file paths
import subprocess
import os

def launch_ui():
    """Function to launch the Streamlit application"""
    # Construct the path to the app.py file in the src directory
    ui_path = os.path.join("src", "app.py")
    # Run the Streamlit application using subprocess
    subprocess.run(["streamlit", "run", ui_path])

# Main execution block - runs only when script is executed directly
if __name__ == "__main__":
    launch_ui()
