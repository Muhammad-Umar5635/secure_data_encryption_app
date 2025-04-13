# 🔐 Secure Data Encryption App

A secure, user-friendly Streamlit application that enables users to encrypt, store, and retrieve confidential data using modern cryptographic techniques. The app supports multiple users, secure authentication, and persistent JSON-based data storage.

---

## 📌 Features

### 🔑 Authentication & User Management
- Multi-user login and account creation
- Session management
- Time-based lockout after failed login attempts

### 🧠 Data Encryption
- Symmetric encryption using Fernet (from the `cryptography` module)
- Secure key management
- Hashing with PBKDF2 for advanced password protection

### 🗂️ Data Storage
- Persistent encrypted data stored in a local JSON file
- Auto-loading of encrypted data on app startup

### ⚙️ Technologies Used
| Tech              | Description                      |
|------------------|----------------------------------|
| `Streamlit`      | UI for rapid Python web apps     |
| `cryptography`   | Encryption & key management      |
| `hashlib`        | Secure password hashing          |
| `json`           | Local encrypted data storage     |

---

## 🔒 Security Considerations

- All passwords are hashed using **PBKDF2**, a strong and industry-recommended key derivation function (stronger than SHA-256).
- User data is encrypted using **Fernet symmetric encryption** (AES 128-bit under the hood) ensuring confidentiality and integrity.
- A **time-based lockout mechanism** is enforced after multiple failed login attempts, mitigating brute-force attacks.

> ⚠️ **Disclaimer:** This application is developed for educational purposes. For production-level deployment:
> - Use secure deployment environments (e.g., Docker, Heroku, Streamlit Cloud).
> - Manage sensitive credentials using environment variables.
> - Employ cloud-based secret management systems like AWS Secrets Manager or HashiCorp Vault.
> - Regularly audit code for vulnerabilities and adopt best practices from OWASP guidelines.

---

## 🙋 Author

**Muhammad Umar**  
🎓 Computational Finance Student, NED University  
👨‍💻 Python Developer & AI Enthusiast  

- 🌐 [LinkedIn](https://www.linkedin.com/in/muhammad-umar5635/)  
- 💻 [GitHub](https://github.com/Muhammad-Umar5635)

---


