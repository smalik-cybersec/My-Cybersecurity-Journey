# 🧩 Concept 1: The Core Components of a Computer

> **Mentor:** The Da Vinci Cypher  
> **Tier:** 0 — The Bedrock  
> **Module:** 0.1 — Computer Architecture & Operating Systems  
> **Cert Alignment:** CompTIA A+, Linux+, CEH (Foundations)  
> **Job Role Relevance:** SOC Analyst, IR Specialist, Pentester  
> **Red/Blue Relevance:** ✅ Memory Attacks (Red) | ✅ Forensic Analysis (Blue)

---

## 🧠 What Makes a Computer Work?

At its heart, a computer is a system of **three main components** working in concert:

| Component | Role | Volatility | Speed | Real-World Term |
|-----------|------|------------|-------|------------------|
| **CPU** (Central Processing Unit) | Executes instructions | N/A | ⚡ Very Fast | 🧠 Brain |
| **RAM** (Random Access Memory) | Temporary workspace for active data | 🟠 Volatile | ⚡⚡ Fast | 🧾 Countertop |
| **Storage** (HDD/SSD) | Long-term data retention | 🟢 Non-volatile | 🐢 Slower | 📚 Pantry |

---

## 👨‍🍳 Real-World Analogy: The Chef’s Kitchen

> To understand how these components interact, imagine a **chef preparing a meal** in a kitchen:

| Element | Analogy |
|--------|---------|
| **CPU** | 👨‍🍳 The Chef — Performs the actions (cooking, chopping) |
| **RAM** | 🧾 The Countertop — A small, fast-access workspace |
| **Storage** | 📚 The Pantry — Holds many recipe books (files), but retrieval is slow |

### 🍳 Step-by-Step

1. The **chef (CPU)** retrieves a **recipe book (program data)** from the **pantry (Storage)**.
2. He places the recipe on the **countertop (RAM)** to read from it quickly.
3. While cooking, the **chef only works from the countertop** — not from the pantry.
4. If the power goes out, the **countertop is wiped clean**, but the **pantry retains all recipe books**.

---

## 🛡️ Cybersecurity Relevance

> Understanding these components is crucial for both offense and defense in cybersecurity.

### 🔺 Why Attackers Care About RAM

- **Sensitive data** (passwords, session keys, decrypted files) lives in **RAM temporarily** while programs run.
- RAM is a **target for memory scraping**, live forensics, or **cold boot attacks**.
  
### 🔓 Common RAM-Based Attacks

| Attack Type | Description |
|-------------|-------------|
| **Buffer Overflow** | Overwrites memory areas by exceeding allocated RAM space — can hijack execution. |
| **RAM Dumping** | Attackers extract sensitive credentials from active memory (e.g., using `mimikatz` or `volatility`). |
| **Fileless Malware** | Runs purely in RAM without touching disk — harder to detect and forensically trace. |

---

## 🧪 Knowledge Check

> 💬 **Mentor Asks:**  
> Shahid, based on our kitchen analogy:

> **❓ If a piece of malware wants to ensure it runs *every time the computer starts*, would it be more effective for it to hide in the pantry (Storage) or on the countertop (RAM)? Why?**

```markdown
[Write your answer here — explain whether persistence belongs in volatile or non-volatile memory, and what red/blue teams would look for.]
