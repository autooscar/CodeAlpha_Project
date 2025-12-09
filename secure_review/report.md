
---

# ✅ 3. Task 3 — Secure Coding Review  
Create folder **secure_review**

---

## ➤ a) report.md (paste this)
Create file: `secure_review/report.md`

```markdown
# Task 3 — Secure Coding Review
**Author:** Oscar Maduku  
**GitHub:** autooscar

This review analyzes insecure Python code and provides secure fixes.

---

## 1. SUMMARY
The original script contained common cybersecurity vulnerabilities:
- Command injection
- Unsafe `eval()` function
- Hardcoded values
- No input validation

---

## 2. MAIN FINDINGS

### ❌ Finding 1 — Command Injection (HIGH)
Code used:
```python
os.system("ping -c 1 " + user_input)
