# EduBot — Test Cases

## Test Environment
- OS: Windows
- Python: 3.14
- Flask: 3.1.3
- Date: 04-04-2026

---

## Test Results

| # | Input | Expected Output | Actual Output | Status |
|---|-------|----------------|---------------|--------|
| 1 | help | Full command list | Shows all commands: courses, fees, enroll, schedule, certificate, instructor, duration, show-status, contact, clear, about | ✓ |
| 2 | HELP | Full command list | Shows all commands, same as row 1 | ✓ |
| 3 | &nbsp;&nbsp;help&nbsp;&nbsp; | Full command list | Shows all commands, same as row 1 | ✓ |
| 4 | courses | List of 5 courses | Shows all 5 courses with "Type the course name to know more" | ✓ |
| 5 | fees | Fee structure | Shows all course fees with EMI note | ✓ |
| 6 | enroll | Enrollment steps | Shows 4-step enrollment process with contact suggestion | ✓ |
| 7 | schedule | Class timings | Shows weekday and weekend batch timings with recorded sessions note | ✓ |
| 8 | certificate | Certificate info | Shows attendance and assessment requirements | ✓ |
| 9 | duration | Course durations | Shows duration for all 5 courses | ✓ |
| 10 | contact | Support details | Shows email, phone, and support hours | ✓ |
| 11 | about | About EduBot | Shows EduBot description with tech stack | ✓ |
| 12 | bye | Farewell message | Shows goodbye message | ✓ |
| 13 | hello | Greeting | Shows welcome message with help suggestion | ✓ |
| 14 | show-status | System status | Shows status, version, query count, engine, server | ✓ |
| 15 | show status | System status | Shows status, version, query count, engine, server | ✓ |
| 16 | showstatus | System status | Shows status, version, query count, engine, server | ✓ |
| 17 | status | System status | Shows status, version, query count, engine, server | ✓ |
| 18 | what are the fees? | Fee structure | Partial match on "fees" — returns correct fee structure | ✓ |
| 19 | how do i enroll? | Enrollment steps | Partial match on "enroll" — returns correct enrollment steps | ✓ |
| 20 | i want to learn data science | Data science info | Partial match on "data science" — returns course details | ✓ |
| 21 | blahbalaj | Fallback message | Returns fallback with help, courses, contact suggestions | ✓ |
| 22 | (empty input) | Empty input message | Returns "Please type something" message | ✓ |

---

## Bugs Found & Fixed

| # | Bug | Input that failed | Fix applied |
|---|-----|------------------|-------------|
| 1 | show-status variants not recognized | "show status", "showstatus" | Added status_triggers list in chatbot.py line 26 |

---

## Summary
- Total test cases: 22
- Passed: 22
- Failed: 0
- Bugs found: 1
- Bugs fixed: 1