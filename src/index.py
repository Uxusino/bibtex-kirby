"""
This module starts the Flask application.

The module imports the app variable from the app module and starts it 
when the file is run as the main program. The application runs on port 5001 
and is accessible from all network addresses (host="0.0.0.0"). 
Debug mode is enabled, which allows for error and change tracking 
during the development phase.
"""

from app import app

if __name__ == "__main__":
    app.run(port=5001, host="0.0.0.0", debug=True)
