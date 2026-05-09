# ✅ To-Do List Manager

A feature-rich command-line **To-Do List Manager** built with Python that helps users manage their daily tasks with priority levels, due dates, and status tracking — all saved persistently using JSON storage.

---

## 🚀 Features

- ➕ Add tasks with name, due date, priority, and status
- 📋 View all tasks in a formatted table
- ✅ Filter and view **Done** tasks
- ⏳ Filter and view **Pending** tasks
- 🔴 View **High Priority** tasks
- 🟡 View **Medium Priority** tasks
- 🟢 View **Low Priority** tasks
- 🗑️ Delete tasks by name
- 💾 Persistent storage using JSON — data saved between sessions
- ✔️ Input validation for date, priority, and status fields
- 🔁 Duplicate task detection

---

## 🛠️ Technologies Used

- **Language:** Python 3
- **Concepts:** Functions, File Handling, JSON, CRUD Operations, Input Validation, Loops
- **Storage:** JSON (data persists between sessions)

---

## 📌 How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/priyanshupatel-tech/Todo-List-Python.git
   cd Todo-List-Python
   ```

2. Run the program:
   ```bash
   python todo.py
   ```

3. Use the menu to manage your tasks.

> **Note:** `todo.json` is auto-generated on first run. No setup needed.

---

## 🖥️ Menu Options

```
=================================== To Do List Menu ===================================
1. Add Task
2. View Task
3. Done Task
4. Pending Task
5. High Priority Task
6. Low Priority Task
7. Medium Priority Task
8. Delete Task
10. Exit
```

---

## 🖥️ Sample Output

```
Task Name           Due Date                 Task Priority             Task Status
-------------------------------------------------------------------------------------
Buy Groceries       5/6/2026                 High                      Pending
Study Python        10/6/2026                Medium                    Done
Pay Bills           1/7/2026                 Low                       Pending
```

---

## 📂 Project Structure

```
Todo-List-Python/
│
├── todo.py        # Main application file
├── todo.json      # Auto-generated task storage file
└── README.md
```

---

## ✅ Input Validation

| Field | Validation |
|-------|-----------|
| Task Name | Checks for duplicate task names |
| Day | Must be between 1–31 |
| Month | Must be between 1–12 |
| Year | Must be 2026 or later |
| Priority | Only 1 (Low), 2 (High), 3 (Medium) accepted |
| Status | Only 1 (Done), 2 (Pending) accepted |

---

## 💡 Learning Outcomes

- Building a complete CRUD application in Python
- Using JSON for persistent data storage
- Implementing multi-level filtering (priority + status)
- Writing clean input validation logic
- Designing formatted CLI table output using f-strings

---

## 👨‍💻 Author

**Priyanshu Patel**
- 🔗 [LinkedIn](https://www.linkedin.com/in/priyanshupatel-tech/)
- 💻 [GitHub](https://github.com/priyanshupatel-tech)
