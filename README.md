# 📚 Book Recommender System

A web-based **Book Recommendation System** built with **Flask**, **Python**, and **Machine Learning**.  
It recommends books similar to the one entered by the user, based on collaborative filtering.

---
## Deployed Link
https://book-recommender-system-jnbr.onrender.com

---

## 🚀 Features

- 📖 Displays Top 50 Popular Books  
- 🔍 Suggests similar books using cosine similarity  
- 🎨 Modern responsive UI built with **Bootstrap 5**  
- ⚙️ Model preprocessed and stored using **Pickle (.pkl)**  
- ☁️ Deployable easily on **Render** or **Heroku**

---

## 🧠 Tech Stack

- **Backend:** Python, Flask  
- **Frontend:** HTML, CSS, Bootstrap  
- **Machine Learning:** Pandas, NumPy, Scikit-learn  
- **Model Storage:** Pickle (.pkl files)  
- **Deployment:** Render / Heroku  

---

## 🗂️ Folder Structure

book-recommender-system/<br>
│<br>
├── app.py # Flask backend<br>
├── requirements.txt # Dependencies<br>
├── Procfile # Deployment configuration (for Render/Heroku)<br>
├── templates/<br>
│ ├── index.html # Homepage - Top 50 books<br>
│ ├── recommend.html # Recommendation page<br>
│<br>
├── static/<br>
│ ├── style.css # (optional) Custom CSS<br>
│<br>
├── popular.pkl # Preprocessed data for popular books<br>
├── books.pkl # Book dataset<br>
├── pt.pkl # Pivot table data<br>
├── similarity_scores.pkl # Precomputed similarity matrix<br>
└── README.md # Project documentation<br>
<br>
yaml<br>
Copy code<br>
<br>
## ⚙️ Setup Instructions (Run Locally)

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/prakriti1111/book-recommender
cd book-recommender-system
2️⃣ Create and Activate Virtual Environment (optional but recommended)
bash
Copy code
python -m venv venv
venv\Scripts\activate        # For Windows
# OR
source venv/bin/activate     # For macOS/Linux
3️⃣ Install Dependencies
bash
Copy code
pip install -r requirements.txt
4️⃣ Run the Application
bash
Copy code
python app.py
5️⃣ Open in Browser
Visit 👉 http://127.0.0.1:5000/
```
**📸 Screenshots<br>**
**🏠 Homepage**<br>
Displays top 50 most popular books.<br>

**🔍 Recommendation Page**<br>
Search for a book and get similar recommendations instantly.<br>

**🧑‍💻 Author**<br>
**Prakriti GUPTA**<br>
📍 B.Tech CSE | MNNIT Prayagraj<br>
💡 Passionate about Machine Learning and Web Development<br>
