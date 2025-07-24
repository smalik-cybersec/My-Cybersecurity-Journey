# 📝 Notes: Hashing for Integrity

### Date: 2025-07-24

### Mentor: The Da Vinci Cypher

---

## 1. Key Definitions

* **Cryptographic Hash Function:** A mathematical algorithm that takes an input of any size and produces a fixed-size, unique output string called a **hash** or **digest**. It serves as a "digital fingerprint" for data.
* **Integrity:** A core principle of the CIA Triad, ensuring that data is accurate and has not been tampered with by unauthorized parties.

## 2. The Three Core Properties of a Hash Function

1. **Deterministic:** The same input will always produce the exact same hash.
2. **Irreversible (One-Way):** It is computationally infeasible to reverse the process and derive the original input from its hash. This is why hashes are used for secure password storage.
3. **Collision Resistant:** It is computationally infeasible to find two different inputs that produce the same output hash.

## 3. The Avalanche Effect

A critical characteristic of collision resistance. It states that a tiny change in the input (e.g., flipping a single bit) will cause a drastic, unpredictable, and complete change in the output hash. This was demonstrated in our lab by changing "The" to "the".

---

## 4. Cybersecurity Relevance

* **File Integrity Verification:** This is the primary use case demonstrated in our lab. Software developers publish the SHA-256 hashes of their programs so users can verify their download has not been corrupted or replaced with malware.
* **Password Storage:** Websites store hashes of user passwords instead of the plain text. The one-way nature prevents an attacker who steals the database from immediately knowing everyone's password.
* **Digital Forensics:** Investigators create hashes of digital evidence (like a hard drive image) the moment it's collected. This hash acts as a seal. At any point in the future, they can re-hash the evidence to prove that it has not been altered during the investigation, which is critical for its admissibility in court.
* **Blockchain:** Each block in a blockchain contains the hash of the previous block, creating a secure, tamper-evident chain.
