
# Create and activate virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Set environment variables
export FLASK_APP=blackjackr
export FLASK_ENV=development

# Initialize the database
flask db init
flask db migrate -m "Initial schema"
flask db upgrade

# Run the app
flask run --debug
