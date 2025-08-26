# Key Security & IT Terms

## 1. CMDB (Configuration Management Database)
- *What:* Database of all Configuration Items (CIs) — IT assets like servers, apps, users, networks — and their relationships.
- *How:* Auto-discover assets, sync from EDR/cloud/AD, assign owners, keep updated.
- *Use in Companies:* Helps IT/Security know “what we have, where it is, how it’s connected”—crucial for audits, compliance, and troubleshooting.

## 2. SLA (Service Level Agreement)
- *What:* Contract/target defining how fast issues need fixing.
- *How:* Example – Critical vulnerabilities on internet-facing servers must be patched in 7 days.
- *Use:* Companies track SLA compliance for efficiency, management and regulatory proof.

## 3. MTTR (Mean Time to Repair/Remediate)
- *What:* Average time taken to fix a vulnerability or restore service.
- *How:* Calculate = (Fix time – Detection time).
- *Use:* Shows how quickly IT/Security teams react; a key improvement metric.

## 4. MSP (Managed Service Provider)
- *What:* External company managing IT (networks, servers, endpoints) for clients.
- *Use:* Hired by small/medium businesses instead of building large internal IT teams.

## 5. MSSP (Managed Security Service Provider)
- *What:* Similar to MSP but focused on cybersecurity for clients.
- *Use:* Provides SOC monitoring, threat detection, and incident response.

## 6. Tenants & Sub-tenants
- *Tenant:* One customer using a platform.
- *Sub-tenant:* A child unit (department, branch, subsidiary).
- *Use:* Lets MSPs securely manage client/branch data and multi-company environments.

## 7. EDR (Endpoint Detection & Response)
- *What:* Security tool for monitoring/protecting laptops, servers, and mobiles.
- *How:* Detects malware, isolates infected devices, blocks malicious files.
- *Use:* Protects against ransomware and advanced endpoint attacks.

## 8. Shadow IT
- *What:* Unapproved apps/devices used by employees (e.g., personal Google Drive).
- *Use:* Creates security risks since IT doesn’t control or monitor them.
- *Fix:* Discover hidden apps/devices, approve safe ones, block risky ones.

## 9. NVD (National Vulnerability Database)
- *What:* U.S. government database of known vulnerabilities (CVEs).

- *Use:* Security teams check NVD to identify threats and patch software quickly.

## 10. CVE ID (Common Vulnerabilities & Exposures)
- *What:* Unique ID for each vulnerability (e.g., CVE-2023-12345).
- *Use:* Used in reports, tickets, and patching workflows to track issues.

## 11. Vulnerability Standards
- *What:* Frameworks to track and score vulnerabilities.
  - CVE → IDs
  - CVSS → Severity score (0–10)
  - CWE → Weakness type
  - OWASP → Web app risks (Top 10)
- *Use:* Companies use these standards to prioritize and fix vulnerabilities.

## 12. ITAM (IT Asset Management)
- *What:* Tracking/managing IT assets throughout their lifecycle.
- *Use:* Controls costs, ensures license compliance, reduces security risk.

## 13. ITSM (IT Service Management)
- *What:* Managing IT services (incidents, changes, requests).
- *Use:* Platforms like ServiceNow, Jira Service Management help teams resolve issues faster and track accountability.

## 14. Remediation
- *What:* Process of fixing vulnerabilities (patching, config changes, removing malware).
- *Use:* Companies remediate quickly to avoid breaches and SLA violations.

## 15. Rogue Assets (Rogue IT/Zones)
- *What:* Unauthorized devices or accounts on the network.
- *Use:* Risky because they bypass security controls.
- *Fix:* Detect and quarantine unknown devices using NAC or asset discovery.

## 16. Multi-Tenancy
- *What:* One platform serving multiple customers with securely isolated data.
- *Use:* SaaS platforms (e.g., Office 365, ApexaiQ), MSP/MSSP scenarios for scalable, secure client separation.

---

## 17. CVE (Common Vulnerabilities and Exposures)

   * A unique identifier given to a publicly known cybersecurity vulnerability.
   * Example: `CVE-2025-12345`.
   * Managed by **MITRE** and used worldwide.

---

## 18. CPE (Common Platform Enumeration)

   * A standardized way to name software, operating systems, and hardware.
   * Example: `cpe:2.3:a:apache:http_server:2.4.57:*:*:*:*:*:*:*` (refers to Apache HTTP Server v2.4.57).
   * Used to match vulnerabilities (CVEs) to products.

---

## 19. CWE (Common Weakness Enumeration)

   * A list of **software weaknesses** (like coding flaws) that can lead to vulnerabilities.
   * Example: `CWE-89` → SQL Injection.
   * Helps classify *types* of security problems, not specific bugs.

---

## 20. CVID

   * Sometimes confused with CVE, but **CVID is not an official standard** in security databases.
   * It may be used internally by some vendors as *“Common Vulnerability ID”*.
   * If you saw it in your context, it’s likely referring to a **custom/alternate identifier** for vulnerabilities (not a global standard like CVE).

---

## 21. Shadow ID

   * Refers to identifiers created by **third-party vulnerability databases** (outside official CVE/NVD).
   * Example: Some security vendors assign a *Shadow ID* when a CVE hasn’t yet been published.

---

## 22. Rogue ID

   * Similar to Shadow ID → unofficial identifiers assigned by companies/security tools.
   * Often used to track **unconfirmed or zero-day vulnerabilities** before CVE assignment.

---


