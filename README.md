# Image Explainer
## Project Structure

```
imageExplainer/
├── .venv/
├── uploads/
├── run.py          
├── .gitignore     
├── README.md      
└── app/
    ├── __init__.py
    ├── urls.py      
    └── handlers/
        ├── __init__.py
        └── upload.py   
```
## Getting Started
Prerequisites
Python 3.6+

A virtual environment (recommended)

Installation & Setup
Clone the repository:

```
git clone https://github.com/chinmayroy/imageExplainer.git
cd imageExplainer
```
Create and activate a virtual environment:
```
For macOS/Linux
python3 -m venv .venv
source .venv/bin/activate

For Windows
python -m venv .venv
.\.venv\Scripts\activate
```

Running the Server
You can run the server with the default port (9090) or specify a custom one.

To run on the default port (9090):
```
python run.py
```
To run on a custom port (e.g., 8000):
```
python run.py 8000
```
The server will start, and you will see a confirmation message in the terminal.
