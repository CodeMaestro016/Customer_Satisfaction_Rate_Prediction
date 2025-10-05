# Customer_Satisfaction_Rate_Prediction

This repository holds a small Flask web app and supporting notebook used to predict customer satisfaction for airline travelers using a pre-trained CatBoost model.
Contents
--
- `website/` - Flask app, model, and HTML templates
	- `app.py` - Flask application that loads `model/catboost_model.pkl` and exposes a `/predict` endpoint and simple pages (`/`, `/analytics`, `/reports`).
- `model/catboost_model.pkl` - Pretrained CatBoost model (binary pickle).
	- `templates/` - HTML templates used by the Flask app (`home.html`, `analytics.html`, `reports.html`, `base.html`).
- `Notebooks/` - Jupyter notebook used to train/export the CatBoost model (and a text file).
- `requirements.txt` - Python dependencies required to run the project.
- `Dockerfile` - Optional Dockerfile to containerize the app.

Quick start (Windows PowerShell)
--
1. Create and activate a virtual environment (recommended):

```powershell
python -m venv .venv
 venv\Scripts\Activate
```

2. Install dependencies:

```powershell
pip install -r requirements.txt
```

3. Run the Flask app from the `website` folder:

```powershell
cd website
python app.py
```

The app will start on port 5000 by default. Open http://127.0.0.1:5000 in your browser.

Notes and verification
--
- The Flask app expects `website/model/catboost_model.pkl` to exist. If it is missing, the app will print an error and the `/predict` endpoint will return an error indicating the model is not loaded.
- `requirements.txt` lists `catboost` and `flask`. If you plan to deploy in production, pin exact versions and use a secure secret key (do not keep `app.secret_key` hard-coded).
- A `Dockerfile` is provided for convenience. Build with:

```powershell
docker build -t customer-satisfaction-app .
docker run -p 5000:5000 customer-satisfaction-app
```

Security and next steps
--
- Replace the hard-coded `app.secret_key` with a secure value from environment variables.
- Add input validation and better error handling for the `/predict` endpoint.
- Add automated tests (unit tests) for the Flask endpoints.

If you'd like, I can add a small smoke test that imports `website.app` and ensures the app object is created and the model loads (or returns a clear error). Tell me if you want that and I will add it.
# Customer_Satisfaction_Rate_Prediction

This repository holds a small Flask web app and supporting notebook used to predict customer satisfaction for airline travelers using a pre-trained CatBoost model.
Contents
--
- `website/` - Flask app, model, and HTML templates
	- `app.py` - Flask application that loads `model/catboost_model.pkl` and exposes a `/predict` endpoint and simple pages (`/`, `/analytics`, `/reports`).
- `model/catboost_model.pkl` - Pretrained CatBoost model (binary pickle).
	- `templates/` - HTML templates used by the Flask app (`home.html`, `analytics.html`, `reports.html`, `base.html`).
- `Notebooks/` - Jupyter notebook used to train/export the CatBoost model (and a text file).
- `requirements.txt` - Python dependencies required to run the project.
- `Dockerfile` - Optional Dockerfile to containerize the app.

Quick start (Windows PowerShell)
--
1. Create and activate a virtual environment (recommended):

```powershell
python -m venv .venv
 venv\Scripts\Activate
```

2. Install dependencies:

```powershell
pip install -r requirements.txt
```

3. Run the Flask app from the `website` folder:

```powershell
cd website
python app.py
```

The app will start on port 5000 by default. Open http://127.0.0.1:5000 in your browser.

Notes and verification
--
- The Flask app expects `website/model/catboost_model.pkl` to exist. If it is missing, the app will print an error and the `/predict` endpoint will return an error indicating the model is not loaded.
- `requirements.txt` lists `catboost` and `flask`. If you plan to deploy in production, pin exact versions and use a secure secret key (do not keep `app.secret_key` hard-coded).
- A `Dockerfile` is provided for convenience. Build with:

```powershell
docker build -t customer-satisfaction-app .
docker run -p 5000:5000 customer-satisfaction-app
```

Security and next steps
--
- Replace the hard-coded `app.secret_key` with a secure value from environment variables.
- Add input validation and better error handling for the `/predict` endpoint.
- Add automated tests (unit tests) for the Flask endpoints.

If you'd like, I can add a small smoke test that imports `website.app` and ensures the app object is created and the model loads (or returns a clear error). Tell me if you want that and I will add it.
# Customer_Satisfaction_Rate_Prediction
