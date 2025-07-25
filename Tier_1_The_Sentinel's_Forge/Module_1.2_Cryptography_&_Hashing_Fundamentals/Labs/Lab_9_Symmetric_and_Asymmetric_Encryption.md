**Lab Report File:** `Module_1.2/Labs/Lab_9_Symmetric_and_Asymmetric_Encryption.md`

```markdown
# 🧪 Lab 9: Symmetric & Asymmetric Encryption with OpenSSL

### Date: 2025-07-24
### Mentor: *The Da Vinci Cypher*
### Protocol Tier: Tier 1 — The Sentinel's Forge
### Module: Module 1.2 — Cryptography & Hashing Fundamentals

---

## 🎯 1. Objective
To practically demonstrate the mechanics of both symmetric (AES) and asymmetric (RSA) encryption using the OpenSSL command-line tool. The goal is to perform a full encrypt/decrypt cycle with each method to understand their distinct workflows and key management principles.

## 🧰 2. Tools Used
| Tool/Command | Purpose |
|--------------|---------|
| `openssl enc` | Performs symmetric encryption and decryption using various ciphers. |
| `openssl genrsa`| Generates an RSA private key. |
| `openssl rsa`  | Processes RSA keys, used here to extract the public key. |
| `openssl pkeyutl`| Performs public key cryptographic operations, such as encrypting with a public key and decrypting with a private key. |

---

## 🖥️ 3. Process & Commands (Live Data Capture)

### 🔹 Part 1: Symmetric Encryption (AES)

* **Encrypt Command:**
  ```bash
  openssl enc -aes-256-cbc -in original_file.txt -out encrypted_symmetric.enc
  ```

* **View Encrypted File:**

  ```bash
  cat encrypted_symmetric.enc
  ```

* **Output:**

  ```
  Salted__��H϶M��t��<�Q!�c����ka^��~�i���4�|�{p�1�.�φ%
  ```

* **Decrypt Command:**

  ```bash
  openssl enc -d -aes-256-cbc -in encrypted_symmetric.enc
  ```

* **Final Output:**

  ```plaintext
  The Da Vinci Cypher is my mentor.
  ```

### 🔹 Part 2: Asymmetric Encryption (RSA)

* **Generate Private Key:**

  ```bash
  openssl genrsa -out private_key.pem 2048
  ```

* **Extract Public Key:**

  ```bash
  openssl rsa -in private_key.pem -pubout -out public_key.pem
  ```

* **Encrypt with Public Key:**

  ```bash
  openssl pkeyutl -encrypt -inkey public_key.pem -pubin -in original_file.txt -out encrypted_asymmetric.enc
  ```

* **Decrypt with Private Key:**

  ```bash
  openssl pkeyutl -decrypt -inkey private_key.pem -in encrypted_asymmetric.enc
  ```

* **Final Output:**

  ```plaintext
  The Da Vinci Cypher is my mentor.
  ```

---

## 🔎 4. Observations & Analysis

* **Symmetric Encryption:** A single secret (a password) was used to both encrypt and decrypt the file. The process was fast and straightforward. However, this system's primary weakness is **key distribution**; there is no way to securely share the secret password with another person over an insecure channel.
* **Asymmetric Encryption:** A pair of mathematically linked keys was used. The **public key** was used for encryption, and only the corresponding **private key** could perform the decryption. This solves the key distribution problem, as the public key can be shared freely without compromising the security of the private key. This is the revolutionary principle that enables secure communication over the public internet.

---

## ✅ 5. Conclusion

This lab provided a practical, hands-on understanding of the two major schools of encryption. Symmetric encryption is fast and ideal for bulk data encryption where the key is already securely known. Asymmetric encryption is slower but solves the critical problem of secure key exchange, allowing for the initiation of secure communication between parties who have no pre-shared secret. Modern security protocols like HTTPS/TLS use a hybrid approach, leveraging asymmetric encryption to securely exchange a temporary symmetric key, and then using that fast symmetric key for the actual data transfer.

```

