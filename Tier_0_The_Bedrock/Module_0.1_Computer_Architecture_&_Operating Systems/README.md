# Module 0.1: Computer Architecture & Operating Systems

### Date: 2025-07-22

### Mentor: The Da Vinci Cypher

---

## Module Overview

This module covers the fundamental building blocks of a computer system. Understanding how hardware components interact and how the Operating System manages them is the essential first step in learning to secure a system.

As cybersecurity practitioners, we must deeply understand how the **processor (CPU)** executes instructions, how **memory (RAM)** and **storage** are utilized, and how the **operating system kernel** orchestrates these resources securely and efficiently. Every attack and defense method—from malware injection to system hardening—hinges on this foundational knowledge.

---

## Key Concepts Covered

### 🧠 Computer Architecture

- **CPU (Central Processing Unit):**  
  The CPU is the "brain" of the system. It performs calculations, executes instructions, and handles all logical decisions. Modern CPUs have multiple cores, instruction pipelines, and caching mechanisms. Understanding CPU registers, process context switching, and privilege levels is essential for secure software execution.

- **RAM (Random Access Memory):**  
  RAM is volatile memory, acting as the system's short-term working area. It stores the data and instructions that the CPU needs *right now*. When RAM is full, performance degrades, and processes may crash. RAM is a common target for live memory attacks (e.g., credential dumping, keyloggers).

- **Storage (HDD/SSD):**  
  This is non-volatile memory used to store operating systems, programs, logs, and user data. It retains data even after shutdown. Understanding file systems, I/O operations, and storage permissions is crucial for forensic investigations and secure system configuration.

---

### 🧮 Operating Systems

- **Kernel:**  
  The kernel is the core of the OS. It operates in **ring 0** (full privileges) and directly interfaces with the hardware. It manages memory, schedules processes, and controls access to hardware devices. Kernel exploits are some of the most dangerous in cybersecurity (e.g., privilege escalation, rootkits).

- **User Space:**  
  This is where user applications execute. These applications have restricted access to system resources and must use system calls to interact with the kernel. The separation between kernel space and user space is a key security boundary. Breaking this boundary (e.g., via buffer overflows) allows attackers to hijack the system.

---

## Analogies

### 👨‍🍳 Chef’s Kitchen

| Component      | Analogy                     | Role in the System                             |
|----------------|-----------------------------|-------------------------------------------------|
| CPU            | 👨‍🍳 The Chef                | Executes instructions (cooking).                |
| RAM            | 🍽️ The Countertop            | Temporary workspace for active preparation.     |
| Storage        | 🗃️ The Pantry                | Long-term storage of ingredients (data/files).  |

---

### 🎻 Grand Orchestra

| Component       | Analogy                 | Role in the System                                       |
|------------------|--------------------------|-----------------------------------------------------------|
| Kernel           | 🎼 Conductor              | Orchestrates access to CPU, memory, and devices.          |
| Applications     | 🎺 Musicians              | Perform tasks based on written music (user requests).     |
| Hardware         | 🎻 Instruments             | Generate the actual sound (output) when played.           |

---

## Reflections & Questions

- 🔍 I now understand that **cybersecurity begins at the system level**. Without knowing how a CPU, RAM, or the kernel functions, it’s impossible to defend against threats like privilege escalation, memory corruption, or kernel-mode rootkits.
- 💭 **Interesting Insight:** The user/kernel separation is a critical line of defense. A compromised user process can’t directly access kernel memory unless a vulnerability is exploited.
- ❓ **Open Questions:**
  - How do modern kernels (e.g., Linux) mitigate privilege escalation?
  - What exactly happens during a context switch between processes?
  - How are hardware interrupts handled securely?

- 🔐 **Cybersecurity Connection:**  
  Whether you're hardening Linux, performing incident response, or reversing malware, every action hinges on your grasp of how the OS manages execution, memory, and hardware access. Attackers exploit these exact interfaces. Defenders must master them.

---
