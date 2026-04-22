# AI SmartSell – AI-Powered Marketplace Listing Generator

AI SmartSell is an AI-powered marketplace listing generator designed to simplify the process of creating product listings for online marketplaces. Instead of manually entering the title, description, category, and price, users can upload a product image and the system automatically generates structured listing details using AI.

The goal of this project is to reduce manual effort, improve listing quality, and create a faster and more efficient selling experience.

---

## Features

- Upload product images for automatic analysis
- Preview uploaded image before processing
- AI-generated product title and description
- Automatic product category detection
- Suggested product price generation
- Editable form fields for user review and correction
- Save final product details to PostgreSQL
- Success confirmation after saving

---

## Tech Stack

### Backend
- Python
- FastAPI
- PostgreSQL
- Psycopg2
- Hugging Face Transformers
- BLIP Model (Salesforce/blip-image-captioning-base)

### Frontend
- HTML
- CSS
- JavaScript
- Fetch API

### Other Tools
- Git
- GitHub
- REST APIs
- CORS Middleware

---

## Project Workflow

1. The user uploads a product image through the frontend interface.
2. The selected image is previewed for confirmation.
3. The frontend sends the image to the FastAPI backend using a POST request.
4. The BLIP image captioning model analyzes the image and generates a descriptive caption.
5. The backend converts the caption into structured product details such as title, description, category, and suggested price.
6. These generated details are automatically displayed in editable form fields.
7. The user can review and modify the details if needed.
8. After confirmation, the user clicks Save Product.
9. The final product listing is stored in PostgreSQL.

---

## Project Structure

```text
ai-smartsell/
│
├── backend/
│   └── main.py
│
├── frontend/
│   └── index.html
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Installation and Setup
### Clone the Repository

git clone https://github.com/Abhinand098/ai-smartsell.git
cd ai-smartsell

### Install Dependencies
pip install -r requirements.txt

### PostgreSQL Setup
Create a PostgreSQL database named:
marketplace
Update your PostgreSQL credentials inside main.py:

- host
- database
- user
- password

### Run the Backend

cd backend
uvicorn main:app --reload

The backend will run at:

http://127.0.0.1:8000

### Run the Frontend

Open the following file in your browser:

frontend/index.html

---

## Future Improvements

- Replace rule-based category detection with a dedicated classification model
- Implement dynamic price prediction using machine learning
- Use LLM structured output instead of rule-based product detail generation
- Add user authentication and seller dashboard
- Support multiple image uploads
- Deploy the project using cloud platforms such as AWS, Render, or Railway
- Add analytics and admin monitoring dashboard

---

## Learning Outcomes

This project demonstrates practical experience in:

- Full-stack application development
- FastAPI backend development
- AI model integration using Hugging Face
- PostgreSQL database management
- Frontend-backend communication using REST APIs
- Image upload handling and file processing
- Real-world workflow design for production-oriented applications

---

## Author

Abhinand Krishnan R S

B.Tech Computer Science Graduate
Aspiring Software Engineer | Backend Developer | AI-Integrated Full Stack Developer
