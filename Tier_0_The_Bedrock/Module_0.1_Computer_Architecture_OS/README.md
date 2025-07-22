# 🧠 Module 0.1: Computer Architecture & Operating Systems

> **Date:** [Enter Today’s Date]  
> **Mentor:** *The Da Vinci Cypher*  
> **Protocol Tier:** Tier 0 — The Bedrock  
> **Job Role Mapping:** Junior SOC Analyst, Helpdesk Technician  
> **Cert Alignment:** CompTIA A+, Linux+, CEH (Foundations)  
> **Difficulty:** 🟢 Beginner  
> **Red/Blue Relevance:** ✅ Blue Team Baseline | ✅ Red Team Target Profiling

---

## 📦 1. Module Overview

This foundational module explores **how computers are built and managed internally**. Understanding the structure of **hardware** and the role of the **Operating System (OS)** is critical for securing any digital environment.

You’ll learn:
- What makes up the architecture of a modern computer.
- How the OS (especially Linux) manages hardware and processes.
- Why this matters for cybersecurity operations.

---

## 🧩 2. Key Concepts Covered

### 🖥️ Computer Architecture

| Component | Description |
|----------|-------------|
| **CPU**  | The “brain” that executes instructions. |
| **RAM**  | Fast, temporary memory used for active processing. |
| **Storage** | Long-term memory (e.g., SSD/HDD) used to store the OS, logs, and files. |

---

### 🧑‍💻 Operating System Components

| Element     | Analogy                     | Description |
|-------------|-----------------------------|-------------|
| **Kernel**   | Conductor of an orchestra    | Controls access to CPU, memory, devices. Operates in **privileged mode**. |
| **User Space** | Stage for applications     | Runs programs with **limited permissions**. Interacts with kernel via system calls. |

---

## 🎭 3. Real-World Analogies

- **Chef's Kitchen Analogy:**
  - CPU → The Chef (executes instructions)
  - RAM → The Countertop (temporary workspace)
  - Storage → The Pantry (permanent storage)

- **Grand Orchestra Analogy:**
  - Kernel → Conductor (manages everything)
  - Applications → Musicians (run user code)
  - Hardware → Instruments (interact via kernel)

---

## 🔎 4. Red/Blue Team Perspective

| Role      | Use Case |
|-----------|----------|
| 🟥 Red Team | Targets kernel exploits (e.g., privilege escalation), user-space memory leaks |
| 🟦 Blue Team | Performs system baselining, monitors memory/disk/CPU abuse via EDR/SIEM |

---

## 🧠 5. Reflections & Questions

> *(Write your thoughts below — this is your journal section.)*

- What did I find most interesting?
- How does understanding the **kernel vs. user space** help in cybersecurity?
- Can an attacker manipulate memory or the OS at runtime?
- How does virtualization affect system architecture?

```markdown
[Write your answers here...]
