# 🛠️ Lab 4.5: Case Study - Live Network Troubleshooting

### Date: 2025-07-23

### Mentor: *The Da Vinci Cypher*

### Protocol Tier: Tier 0 — System Fundamentals

### Module: Module 0.2 — Networking Fundamentals

---

## 🎯 1. Objective

To diagnose and resolve a critical network connectivity issue on a Red Hat Linux virtual machine. The initial symptom was a `100% packet loss` when attempting to `ping` any external or local gateway address, despite the host machine having full internet access. This lab documents the systematic, multi-step troubleshooting process undertaken to find the root cause and restore connectivity.

## 📝 2. Initial State & Problem Statement

* **Host System:** Windows PC, VMware Workstation installed, full internet connectivity confirmed via `ping 8.8.8.8`.
* **Guest System:** Red Hat Linux VM.
* **Initial Findings:** The guest VM had an IP address (`192.168.11.131`), but all `ping` attempts resulted in `100% packet loss`, indicating a network isolation issue.
* **Mission:** To identify the root cause of the network block and restore full internet egress for the guest VM.

---

## 🗺️ 3. Troubleshooting Methodology & Investigation Log

A bottom-up troubleshooting methodology, guided by the OSI model, was employed.

<details>
<summary>🕵️ Click to expand the step-by-step investigation log...</summary>

### 🔹 Step 1: Verify VM Network Adapter Mode

* **Action:** Checked the VM's hardware settings in VMware.
* **Finding:** The adapter was set to **NAT** mode.
* **Conclusion:** This is a standard and correct setting, so it was unlikely to be the root cause.

### 🔹 Step 2: Verify Host VMware Services

* **Action:** Used `services.msc` on the Windows host to inspect VMware services.
* **Finding:** Both `VMware NAT Service` and `VMware DHCP Service` were **Running**.
* **Conclusion:** The core services were active. A service restart was performed as a precautionary measure, but it did not resolve the issue.

### 🔹 Step 3: Isolate the Problem (Host vs. Guest)

* **Action:** Pinged `8.8.8.8` from the Windows host (`cmd`).
* **Finding:** The host received successful replies with `0% packet loss`.
* **Conclusion:** The issue was definitively isolated to the Guest VM or the software bridge (VMware/Firewall) connecting it to the host.

### 🔹 Step 4: Investigate Host Firewall

* **Action:** Temporarily disabled Windows Defender Firewall for diagnostic purposes.
* **Finding:** The `ping` from the guest VM still failed.
* **Conclusion:** The Windows Defender Firewall was not the primary blocking component. The firewall was immediately re-enabled.

### 🔹 Step 5: Restore VMware Network Defaults

* **Action:** Used the "Restore Defaults" function within VMware's Virtual Network Editor to reset all virtual networking configurations.
* **Finding:** The `ping` from the guest VM now produced a new error: `"Destination Host Unreachable"`.
* **Conclusion:** The state had changed. The new error indicated the guest VM itself was now determining it had no valid route to the destination.

### 🔹 Step 6: Attempt Network Re-initialization (Modern Method)

* **Action:** Used `nmcli connection down` and `nmcli connection up` to force the guest to re-establish its network connection.
* **Finding:** The issue persisted. A check of `ip addr` revealed the VM was retaining the *same IP address* even after a full network reset.
* **Conclusion:** This was the critical "Aha!" moment. The VM was not accepting a new IP address, which strongly suggested a static configuration.

### 🔹 Step 7: The Root Cause Analysis - Static IP Configuration

* **Action:** Inspected the connection profile configuration file at `/etc/NetworkManager/system-connections/ens160.nmconnection`.
* **Finding:** The file contained the line **`method=manual`**, along with hardcoded IP, gateway, and DNS addresses.
* **Conclusion:** **ROOT CAUSE IDENTIFIED.** The VM was configured with a static IP address by its original creators, preventing it from adapting to any new network environment (like NAT or Bridged).

</details>

---

## 🔧 4. The Solution & Remediation Steps

The following commands were executed within the Red Hat VM to convert the network profile from a static configuration to an automatic (DHCP) one.

1. **Clear Old Static IP:**

    ```bash
    sudo nmcli connection modify ens160 ipv4.addresses ""
    ```

2. **Clear Old Static Gateway:**

    ```bash
    sudo nmcli connection modify ens160 ipv4.gateway ""
    ```

3. **Clear Old Static DNS:**

    ```bash
    sudo nmcli connection modify ens160 ipv4.dns ""
    ```

4. **Change Method to Automatic:**

    ```bash
    sudo nmcli connection modify ens160 ipv4.method auto
    ```

5. **Restart the Connection:**

    ```bash
    sudo nmcli connection down ens160 && sudo nmcli connection up ens160
    ```

---

## ✅ 5. Final Result & Verification

After applying the solution, a final `ping` test was conducted.

* **Command:** `ping -c 4 8.8.8.8`
* **Output:**

  ```plaintext
  PING 8.8.8.8 (8.8.8.8) 56(84) bytes of data.
  64 bytes from 8.8.8.8: icmp_seq=1 ttl=110 time=73.6 ms
  64 bytes from 8.8.8.8: icmp_seq=2 ttl=110 time=51.4 ms
  64 bytes from 8.8.8.8: icmp_seq=3 ttl=110 time=48.1 ms
  64 bytes from 8.8.8.8: icmp_seq=4 ttl=110 time=45.9 ms

  --- 8.8.8.8 ping statistics ---
  4 packets transmitted, 4 received, 0% packet loss, time 3006ms
  ```

* **Verification:** The `0% packet loss` and successful replies confirm that **full internet connectivity was successfully restored.**

---

## 🧠 6. Key Takeaways & Lessons Learned

This troubleshooting exercise was more valuable than a standard lab. Key lessons include:

* **Trust, but Verify:** Don't assume a VM is configured for DHCP. Always check the configuration files when encountering unexpected network behavior.
* **Observe State Changes:** The change in `ping` error from a generic timeout to `"Destination Host Unreachable"` was a critical clue that narrowed down the problem space.
* **Mastery of `nmcli`:** The `nmcli` utility is the modern, powerful standard for managing networking in RHEL-based systems.
* **Persistence is Key:** Systematic elimination of possibilities is the only way to solve complex technical problems.
