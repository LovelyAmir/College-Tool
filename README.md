College-Tool (Lab 08)

Flask web application using SQLAlchemy and a shared, cloud-hosted PostgreSQL database powered by Neon.

1. Initial Setup (All Collaborators)

Clone the Repository

git clone https://github.com/LovelyAmir/College-Tool.git
cd College-Tool


Configure Environment Variables

Create a local .env file in the project root directory (next to pyproject.toml):

Windows (PowerShell):

New-Item -ItemType File -Name .env


macOS / Linux:

touch .env


Open .env in your text editor and add the shared database connection URI:

DATABASE_URL="postgresql://<username>:<password>@<ep-name-123456>.us-east-2.aws.neon.tech/<dbname>?sslmode=require"


Note: Never commit the .env file to Git. It is excluded by .gitignore to prevent credential leaks.

2. Environment Setup & Execution

Choose one of the two workflows below to run the project.

Option A: Recommended Workflow (uv)

Using uv automates environment creation, dependency resolution, lockfile synchronization, and script execution without manual virtual environment activation.

Install uv (if not already installed):

Windows (PowerShell):

powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"


macOS / Linux:

curl -LsSf https://astral.sh/uv/install.sh | sh


Sync Dependencies:

uv sync


Verify Database Connection:

uv run python -c "
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, text

load_dotenv()
engine = create_engine(os.getenv('DATABASE_URL'))
with engine.connect() as conn:
    print('Connected successfully:', conn.execute(text('SELECT version();')).scalar())
"


Start the Flask Server:

uv run lab08


Option B: Alternative Workflow (python + pip)

If you prefer using standard Python tools without installing uv:

Create and Activate a Virtual Environment:

Windows (PowerShell):

python -m venv .venv
.\.venv\Scripts\Activate.ps1


macOS / Linux:

python3 -m venv .venv
source .venv/bin/activate


Install Dependencies in Editable Mode:

pip install --upgrade pip
pip install -e .


Verify Database Connection:

python -c "
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, text

load_dotenv()
engine = create_engine(os.getenv('DATABASE_URL'))
with engine.connect() as conn:
    print('Connected successfully:', conn.execute(text('SELECT version();')).scalar())
"


Start the Flask Server:

lab08


(Or alternatively: python -m lab08)

3. Verification & Endpoints

Once the server is running, open your browser:

App Home: http://localhost:5000/

Database Health Check: http://localhost:5000/health/db