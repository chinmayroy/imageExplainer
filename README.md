📂 Project Structure
imageExplainer/
├── .venv/
├── uploads/
├── run.py          # Main server entry point
├── .gitignore      # Specifies files for Git to ignore
├── README.md       # Project documentation
└── app/
    ├── __init__.py
    ├── urls.py       # URL route definitions
    └── handlers/
        ├── __init__.py
        └── upload.py   # Logic for the /upload endpoint

🚀 Getting Started
Prerequisites
Python 3.6+

A virtual environment (recommended)

Installation & Setup
Clone the repository:

git clone https://github.com/chinmayroy/imageExplainer.git
cd imageExplainer

Create and activate a virtual environment:

For macOS/Linux
python3 -m venv .venv
source .venv/bin/activate

For Windows
python -m venv .venv
.\.venv\Scripts\activate

Running the Server
You can run the server with the default port (9090) or specify a custom one.

To run on the default port (9090):

python run.py

To run on a custom port (e.g., 8000):

python run.py 8000

The server will start, and you will see a confirmation message in the terminal.

📝 API Endpoints
Health Check
URL: /

Method: GET

Description: Confirms that the server is running.

Success Response:

Code: 200 OK

Content: { "status": "online", "message": "Welcome..." }

Image Upload
URL: /upload

Method: POST

Description: Uploads an image file to the server. The file is saved in the uploads/ directory.

Form Data:

file: The image file to be uploaded.

Example Usage (with cURL):

curl -X POST -F "file=@/path/to/your/image.jpg" http://127.0.0.1:9090/upload

Success Response:

Code: 200 OK

Content: { "message": "File uploaded successfully", "filename": "image.jpg" }

Error Response:

Code: 400 Bad Request

Content: { "error": "No \"file\" field found in the request." }