# M01-L04 | Algorithm

**Date:** 2025-06-27
---
### 1. Definition & Core Concept
> An algorithm is a well-defined, step-by-step procedure or a finite set of unambiguous instructions designed to solve a specific problem or accomplish a particular task.

Algorithms are the logical blueprints of programs, independent of any specific programming language. They provide the precise sequence of operations required to transform input into desired output.

---
### 2. Why It Matters (The Cybersecurity Context)
* **Relevance:** In cybersecurity, designing clear and efficient algorithms is critical for developing robust security tools, analyzing malicious code, and optimizing defensive strategies. It ensures predictable and correct program behavior, reducing vulnerabilities from logical flaws.
* **Use-Case 1:** **Malware Detection Algorithms:** Antivirus software and Intrusion Detection Systems (IDS) rely on sophisticated algorithms to detect known malware signatures, identify anomalous network traffic patterns, or recognize malicious behavior. The effectiveness of these tools directly depends on the efficiency and accuracy of their underlying algorithms.
* **Use-Case 2:** **Encryption and Hashing Algorithms:** Cryptography, a cornerstone of cybersecurity, is entirely built upon algorithms. Encryption algorithms (e.g., AES, RSA) ensure data confidentiality, while hashing algorithms (e.g., SHA-256, MD5) are used for data integrity verification, password storage, and digital signatures.
* **Use-Case 3:** **Vulnerability Scanning Logic:** When developing a vulnerability scanner, you must define an algorithm that systematically checks for weaknesses: e.g., "for each port, attempt to connect; if open, then try default credentials; if successful, then report vulnerability." This structured approach is algorithmic.

---
### 3. Syntax & Practical Implementation
#### Annotated Example:
Algorithms are conceptual, often described in pseudocode or plain language before actual coding. Let's consider an algorithm for a simple cybersecurity task: checking if a list of IP addresses is present in a "blacklist".

**Algorithm: Check IPs against Blacklist**

1.  **Start**
2.  **Input:** A list of `target_ips` (e.g., `['192.168.1.1', '10.0.0.5', '172.16.0.10']`) and a `blacklist` (e.g., `['10.0.0.5', '192.168.1.100']`).
3.  **Step 1:** Initialize an empty list called `found_in_blacklist`.
4.  **Step 2:** For each `ip_address` in `target_ips`:
    * **Step 2a:** Check if `ip_address` exists within the `blacklist`.
    * **Step 2b:** If `ip_address` is found in `blacklist`, add `ip_address` to `found_in_blacklist`.
5.  **Step 3:** Print the `found_in_blacklist`.
6.  **Output:** A list of IP addresses that are present in the blacklist.
7.  **End**

**Python Implementation (based on the algorithm):**
```python
def check_ips_against_blacklist(target_ips, blacklist):
    """
    Checks if any target IP addresses are present in a given blacklist.
    """
    found_in_blacklist = [] # Step 1

    for ip_address in target_ips: # Step 2
        if ip_address in blacklist: # Step 2a
            found_in_blacklist.append(ip_address) # Step 2b

    return found_in_blacklist # Step 3 (implicitly, as we return to print)

# Example Usage:
my_target_ips = ['192.168.1.1', '10.0.0.5', '172.16.0.10', '192.168.1.50']
known_blacklist = ['10.0.0.5', '192.168.1.100', '172.16.0.10']

malicious_ips_detected = check_ips_against_blacklist(my_target_ips, known_blacklist)

if malicious_ips_detected:
    print(f"Malicious IPs detected in target list: {malicious_ips_detected}")
else:
    print("No malicious IPs found in target list.")