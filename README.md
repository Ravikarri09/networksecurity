
🛡️ Network Security: Phishing URL Detection using Machine Learning

A machine learning-based web security project designed to detect **phishing websites** by analyzing their **URL features** and **network attributes**.
This system helps users identify malicious links before they can cause harm — combining the power of **AI and cybersecurity** to enhance online safety.



🚀 Overview

Phishing is one of the most common cyberattacks, tricking users into revealing sensitive information by mimicking trusted websites.
This project aims to **predict whether a given URL is legitimate or phishing** using trained ML models.

The solution integrates **FastAPI**, **MLflow**, and **MongoDB** to create a scalable and efficient end-to-end system.



 ✨ Key Features

✅ **Phishing Detection:** Predicts whether a URL is phishing or legitimate.
✅ **FastAPI Backend:** Provides REST API endpoints for training and prediction.
✅ **File Upload Interface:** Accepts CSV files containing multiple URLs for batch prediction.
✅ **Interactive HTML Output:** Displays results in a clean table format using Jinja2 templates.
✅ **MongoDB Integration:** Stores dataset and processed results securely.
✅ **MLflow Tracking:** Tracks model experiments, versions, and performance metrics.
✅ **Automated ML Pipeline:** From data ingestion → validation → transformation → training → deployment.
⚙️ Tech Stack

| Component                  | Technology    |
| -------------------------- | ------------- |
| **Programming Language**   | Python 3.12   |
| **Framework**              | FastAPI       |
| **Machine Learning**       | Scikit-Learn  |
| **Data Handling**          | Pandas, NumPy |
| **Database**               | MongoDB Atlas |
| **Model Tracking**         | MLflow        |
| **Templating Engine**      | Jinja2        |
| **Environment Handling**   | dotenv        |
| **Certificate Management** | Certifi       |
🧠 Project Workflow

1. Data Ingestion

   * Fetch data from MongoDB or CSV files.
   * Split into training and test sets.

2. Data Validation

   * Check schema and handle missing or invalid values.

3. Data Transformation

   * Apply KNN imputation for missing data.
   * Prepare the dataset for ML model training.

4. Model Training

   * Train models using Scikit-Learn (e.g., RandomForest, XGBoost).
   * Evaluate performance using accuracy, precision, and recall.

5. Model Tracking & Storage

   * Use MLflow for experiment tracking.
   * Save final model and preprocessor as `.pkl` files.

6. Deployment (FastAPI)

   * Launch a REST API to handle training and predictions.
   * Users upload a CSV file to get phishing detection results.



🧩 How to Run the Project

 1️⃣ Clone the Repository

```bash
git clone https://github.com/<your-username>/networksecurity.git
cd networksecurity
```

 2️⃣ Create and Activate Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate     # For Windows
source venv/bin/activate  # For Mac/Linux
```

3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```
4️⃣ Configure Environment Variables

Create a `.env` file in the project root:

```
MONGODB_URL_KEY=your_mongodb_connection_string
MLFLOW_TRACKING_URI=https://dagshub.com/<username>/<repo>.mlflow
```

 5️⃣ Run the Application

```bash
python app.py
```

Server will start at:
👉 [http://localhost:8000](http://localhost:8000)

 6️⃣ Access the API

* Open **Swagger UI** at → [http://localhost:8000/docs](http://localhost:8000/docs)
* Use the `/train` endpoint to train the model
* Use the `/predict` endpoint to upload a CSV and view predictions



 📂 Project Structure

```
📦 networksecurity
 ┣ 📂 components
 ┣ 📂 constants
 ┣ 📂 entity
 ┣ 📂 pipeline
 ┣ 📂 utils
 ┣ 📂 templates
 ┃ ┗ 📜 table.html
 ┣ 📜 app.py
 ┣ 📜 requirements.txt
 ┣ 📜 README.md
 ┗ 📜 .env
```



📊 Output Example

After uploading your dataset, you’ll get an **interactive HTML table** displaying results like this:

| having_IP_Address | URL_Length | Prefix_Suffix | ... | predicted_column |
| ----------------- | ---------- | ------------- | --- | ---------------- |
| 1                 | -1         | 1             | ... | **Phishing**     |
| -1                | 1          | -1            | ... | **Legitimate**   |


🔮 Future Enhancements

🚀 Add **live URL scanning** using APIs (e.g., VirusTotal).
🌐 Build a **Chrome extension** for real-time phishing detection.
📈 Integrate **deep learning models** for feature extraction.
🧠 Enable **auto retraining** with continuous data updates.



 🙌 Acknowledgments

Special thanks to open-source contributors and the cybersecurity community for their research and datasets that made this possible.



 🧑‍💻 Author

**👨‍💻 Karri Ravi Shankar**
📍 Visakhapatnam, India
💡 Passionate about Machine Learning, Deep Learning & Cybersecurity
🌐 [LinkedIn](https://www.linkedin.com/in/karri-ravi-shankar)




