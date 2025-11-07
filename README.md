# 🧩 Python Developer Technical Assessment

Flask REST API for Task Management (CRUD with SQLite)

## 📘 Overview

Μια απλή REST API εφαρμογή σε Flask για τη διαχείριση εργασιών (tasks).
Ο χρήστης μπορεί να δημιουργεί, διαβάζει, ενημερώνει και διαγράφει εργασίες.
Η εφαρμογή ακολουθεί RESTful αρχιτεκτονική και χρησιμοποιεί SQLite για αποθήκευση δεδομένων (persistent storage).

## 🚀 Δυνατότητες

- 📄 Δημιουργία, προβολή, ενημέρωση και διαγραφή tasks (CRUD λειτουργίες)  
- ⚙️ RESTful αρχιτεκτονική  
- 🧱 Αποθήκευση δεδομένων σε **SQLite** (persistent storage)  
- 🔎 Υποστήριξη φίλτρων και ταξινόμησης (προαιρετικά)  
- 💬 JSON responses και σωστό error handling

---

## 🧠 Τεχνολογίες

- **Python 3.10+**
- **Flask**
- **Flask SQLAlchemy**
- **SQLite**

---

## Πηγή Δεδομένων

Τα δεδομένα που χρησιμοποιήθηκαν στο project ελήφθησαν μέσω του **Postman** από το αντίστοιχο API. Οι κύριες μέθοδοι που χρησιμοποιήθηκαν είναι:

Κάθε μέθοδος έχει τεκμηριωθεί με παραδείγματα αιτημάτων και απαντήσεων στο Postman collection που περιλαμβάνεται στο repository.

1) db κενή
<img width="1698" height="825" alt="Screenshot 2025-10-27 201327" src="https://github.com/user-attachments/assets/7ad05105-ee50-4ee9-a57f-9d54f5de3d9b" />

2) Post method
<img width="1699" height="827" alt="Screenshot 2025-10-27 201518" src="https://github.com/user-attachments/assets/fe2535ec-515d-4399-872d-aeeaf1b39fd1" />
<img width="1694" height="820" alt="Screenshot 2025-10-27 201546" src="https://github.com/user-attachments/assets/f4642b13-cfeb-441b-981f-6c6ae8debc1d" />

3) Get Method
<img width="1699" height="827" alt="Screenshot 2025-10-27 201808" src="https://github.com/user-attachments/assets/4153769f-401f-407e-9ece-4ec1a4becbf3" />

4) Put Method
<img width="1695" height="825" alt="Screenshot 2025-10-27 201940" src="https://github.com/user-attachments/assets/6e632cf0-077b-48f0-9105-97432f6c62f4" />
<img width="1699" height="824" alt="Screenshot 2025-10-27 202002" src="https://github.com/user-attachments/assets/a27ea056-fa42-4269-825e-cbd4c541708a" />

5) Delete Method
<img width="1695" height="826" alt="Screenshot 2025-10-27 202048" src="https://github.com/user-attachments/assets/76c6c628-ec2f-4c31-a5aa-110741efa308" />
<img width="1698" height="825" alt="Screenshot 2025-10-27 202116" src="https://github.com/user-attachments/assets/65bd17a8-4ece-4433-bc92-6ad09a44bbdd" />


## ⚙️ Εγκατάσταση & Εκτέλεση
```bash
# 1️⃣ Κλωνοποίησε το repo
git clone https://github.com/VoudourisAM/Python-Developer-Technical-Assessment.git
cd Python-Developer-Technical-Assessment

# 2️⃣ Εγκατέστησε τα requirements
pip install -r requirements.txt

# 3️⃣ Τρέξε την εφαρμογή
python app.py

# 4️⃣ Άνοιξε στο browser ή Postman
http://127.0.0.1:5000/tasks
