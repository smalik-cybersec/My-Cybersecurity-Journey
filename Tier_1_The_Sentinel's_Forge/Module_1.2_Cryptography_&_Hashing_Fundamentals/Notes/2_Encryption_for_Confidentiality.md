
**Notes File:** `Module_1.2/Notes/2_Encryption_for_Confidentiality.md`

```markdown
# 📝 Notes: Encryption for Confidentiality

### Date: 2025-07-24
### Mentor: The Da Vinci Cypher

---

## 1. Key Definitions

*   **Encryption:** The process of converting readable data (**Plaintext**) into unreadable data (**Ciphertext**) using a **Key** to ensure confidentiality.
*   **Decryption:** The process of converting ciphertext back into plaintext using a key.
*   **Confidentiality:** A core principle of the CIA Triad, ensuring that data is accessible only to authorized individuals.

## 2. The Two Types of Encryption

### Symmetric Encryption (Single Key)
*   **Mechanism:** Uses the **same key** for both encryption and decryption.
*   **Analogy:** A secret mailbox key; you need an identical copy to open the box.
*   **Algorithm Example:** AES (Advanced Encryption Standard).
*   **Strength:** Very fast and computationally efficient. Ideal for large amounts of data (e.g., full-disk encryption).
*   **Weakness:** **Key Distribution Problem.** How do you securely share the secret key to begin with?

### Asymmetric Encryption (Public-Key Cryptography)
*   **Mechanism:** Uses a mathematically linked **key pair**: a public key and a private key.
*   **The Rule:** Data encrypted with a public key can *only* be decrypted by its corresponding private key.
*   **Analogy:** The Public Padlock. Anyone can use your public padlock to lock a box, but only you have the one-of-a-kind private key to open it.
*   **Algorithm Example:** RSA.
*   **Strength:** Solves the key distribution problem, allowing for secure initial communication over an insecure channel.
*   **Weakness:** Computationally expensive and much slower than symmetric encryption.

---

## 3. The Hybrid Solution: How HTTPS Works

Modern systems combine the best of both worlds:
1.  **Asymmetric Encryption** is used first to securely exchange a small piece of data: a brand new, temporary symmetric "session key."
2.  **Symmetric Encryption** is then used with that fast session key to encrypt all the actual data for the remainder of the conversation.

This provides the secure key exchange of asymmetric and the high-speed performance of symmetric.
