# E2E Data Engineering Project — Version 1 (Beginner)

This is **Version 1 (Beginner)** of my end-to-end data engineering project using **open-source tools only**.  
It demonstrates how to build a simple data pipeline using **PostgreSQL and Python**, with Docker for easy setup.

---

## 🗂 Project Structure

version-1-beginner/
├── data/
│ ├── users.csv
│ ├── products.csv
│ └── orders.csv
├── scripts/
│ └── load_data.py
└── README.md

- **data/**: Contains sample CSV files used in this version  
- **scripts/**: Python scripts to create tables and load CSV data into PostgreSQL  

---

## 🛠 Tools Used

- **Docker & Docker Compose** — for containerized PostgreSQL and Python environment  
- **PostgreSQL** — relational database  
- **Python** — for scripting the ETL (Extract, Transform, Load) pipeline  
- **Pandas** — for reading and processing CSV files  
- **psycopg2** — PostgreSQL adapter for Python  

---

## 🚀 How to Run

1. **Clone the repository**

```bash
git clone https://github.com/Tharmithan-N/e2e-data-engineering-project.git
cd e2e-data-engineering-project
```


2. **Start Docker containers**

```bash
docker-compose up -d
```

3. **Enter Python container**

```bash
docker exec -it de_python bash
```

4. **Install dependencies (inside container)**

```bash
pip install psycopg2-binary pandas
```

5. **Run the ETL script**

```bash
python scripts/load_data.py
```

6. **You should see output like:**

Tables created successfully!
Data loaded successfully!
Users rows: 5
Products rows: 5
Orders rows: 5
