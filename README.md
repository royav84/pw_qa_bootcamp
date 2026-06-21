# QA Automation Portfolio — Roi Avital

Senior QA Engineer with 12+ years of experience.
This repo documents my hands-on automation practice across API testing, UI automation, and CI/CD.

---

## Postman — API Testing Collection

A full API testing collection built against JSONPlaceholder API.

**What's covered:**
- GET, POST, PUT, DELETE requests
- Schema validation (field types, nested objects, email format)
- Negative testing (404, invalid IDs, edge cases)
- Environment variables (Dev/Staging)
- Request chaining with collection variables
- Newman CLI automation with data files

**How to run:**
```bash
newman run "QA Training.postman_collection.json" -e Dev.json
newman run "QA Training.postman_collection.json" --folder "CRUD Flow" -e Dev.json
newman run "QA Training.postman_collection.json" --folder "Negative - Invalid User ID" -d invalid_ids.json -e Dev.json
```

---

## Stack
- Postman / Newman
- Python / Playwright (in progress)
- SQL
- GitHub Actions (coming soon)
