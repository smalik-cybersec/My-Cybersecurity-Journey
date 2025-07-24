# 🧪 Lab 8: Hashing for File Integrity

### Date: 2025-07-24
### Mentor: *The Da Vinci Cypher*
### Protocol Tier: Tier 1 — The Sentinel's Forge
### Module: Module 1.2 — Cryptography & Hashing Fundamentals

---

## 🎯 1. Objective
To practically demonstrate the core properties of a cryptographic hash function (SHA-256) for verifying file integrity. The goal is to observe the deterministic nature and the "Avalanche Effect" of hashing by creating a file, hashing it, making a minuscule change, and observing the drastically different hash result.

## 🧰 2. Tools Used
| Tool/Command | Purpose |
|--------------|---------|
| `echo`       | A shell command to output a string of text. Used here to create files. |
| `sha256sum`  | A Linux command-line utility that computes and checks SHA-256 hashes. |

---

## 🖥️ 3. Process & Commands (Live Data Capture)

### 🔹 Step 1: Create and Hash an Original File

* **Command to Create File:**
  ```bash
  echo "The Da Vinci Cypher is my mentor." > original_file.txt
  ```

* **Command to Hash File:**

  ```bash
  sha256sum original_file.txt
  ```

* **Output:**

  ```plaintext
  95e9809f26a6bca218a7c0fef8a4627b307516bb43187023ee353197783274a4  original_file.txt
  ```

### 🔹 Step 2: Create and Hash a Tampered File

* **Command to Create Tampered File (Note the lowercase 't'):**

  ```bash
  echo "the Da Vinci Cypher is my mentor." > tampered_file.txt
  ```

* **Command to Hash Tampered File:**

  ```bash
  sha256sum tampered_file.txt
  ```

* **Output:**

  ```plaintext
  8a05ad08aceaa6354f73022c62d474363ebc24a79342d2bca1ceb246b859e1dc  tampered_file.txt
  ```

---

## 🔎 4. Observations & Analysis

* A minuscule, one-bit change in the input data (changing the first character from `T` to `t`) resulted in a completely different and unpredictable output hash.
* This demonstrates the **Avalanche Effect**, a critical property of secure cryptographic hash functions.
* **Security Insight:** The Avalanche Effect is what makes hashes reliable for integrity checking. An attacker cannot simply make a small, malicious change to a file and hope to produce a hash that is even remotely similar to the original. The integrity check would immediately and definitively fail, alerting the user that the file has been tampered with.

---

## ✅ 5. Conclusion

This lab provided a hands-on demonstration of how hashing serves as the bedrock for data integrity verification. By generating and comparing SHA-256 hashes, we proved that even the slightest modification to a file results in a catastrophic change to its hash, known as the Avalanche Effect. This simple but powerful mechanism is a cornerstone of cybersecurity, used to ensure the integrity of software downloads, digital forensic evidence, and countless other applications where data trustworthiness is paramount.
