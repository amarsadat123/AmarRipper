# 🎓 PAF-IAST Cyber Security Lab Guide
**Project:** AmarRipper - Network Stress Testing & Resource Exhaustion
**Student:** amarsadat123
**Major:** BS Cyber Security

---

## 1. Objective
The goal of this lab is to understand how **Layer 7 (Application Layer)** DDoS attacks work by simulating high-volume HTTP GET requests. This helps in studying server-side bottlenecks and configuring Rate Limiting.

## 2. Methodology
AmarRipper uses **Multi-threading**. In Python, each thread acts as a separate "user" requesting data from the server. 
* **Target:** A local web server (e.g., Apache or Nginx).
* **Tool:** AmarRipper.py
* **Monitoring:** Use `htop` on the target to monitor CPU/RAM spikes.

## 3. Key Concepts for Exams
* **Thread Contention:** When too many threads compete for CPU cycles, the server slows down.
* **TCP Handshake:** Every connection made by AmarRipper completes a 3-way handshake (SYN, SYN-ACK, ACK).
* **HTTP Headers:** We use randomized User-Agents to bypass basic Signature-based Detection.

## 4. How to Defend (PAF-IAST Lab Exercise)
After running the tool, try to stop the attack by:
1. Configuring **iptables** to limit connections per IP.
2. Enabling **mod_evasive** on an Apache server.
3. Setting up a **Reverse Proxy** (like Nginx) with `limit_req`.

---
*Created for educational purposes at Pakistan-Austria Fachhochschule (PAF-IAST).*
