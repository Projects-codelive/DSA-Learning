# 🎓 DSA Visual Lab Assistant

An interactive, web-based Data Structures and Algorithms (DSA) visualization and learning platform built with **Flask (Python)** and **Vanilla JavaScript/CSS**. DSA Visual Lab Assistant helps students and developers understand complex algorithms, data structures, and graph traversals through intuitive, step-by-step animations and interactive quizzes.

---

## 🚀 Features

### 1. 🔄 Sorting Algorithms
- **Bubble Sort**: Step-by-step element comparisons and adjacent swaps.
- **Merge Sort**: Visualizes the divide-and-conquer strategy and sub-array merging.
- **Quick Sort**: Interactive partitioning, pivot selection, and recursive sub-sorting.
- **Heap Sort**: Binary heap construction (Max/Min Heap) and extraction sequence.

### 2. 🔍 Searching Algorithms
- **Linear Search**: Sequential scan illustrating target matches and indices.
- **Binary Search**: Interactive low, mid, and high pointer shifts on sorted datasets.

### 3. 📦 Core Data Structures
- **Stack**: Visual LIFO (Last-In-First-Out) operations with `Push`, `Pop`, `Peek`, and `Clear`.
- **Queue**: Visual FIFO (First-In-First-Out) operations with `Enqueue`, `Dequeue`, `Front`, and `Clear`.

### 4. 🕸️ Graph Traversals
- **Breadth-First Search (BFS)**: Level-order traversal of nodes using queue-based state tracking.
- **Depth-First Search (DFS)**: Recursive/stack-based depth exploration with backtracking visualization.

### 5. 📝 Interactive DSA Quiz System
- Dynamic question sets categorized by topic (`Linear Search`, `Binary Search`, `Bubble Sort`, `Merge Sort`, `Quick Sort`, `Heap Sort`, `Stack`, `Queue`, `BFS`, `DFS`).
- Instant feedback, score tracking, and detailed explanations.

---

## 🛠️ Tech Stack

- **Backend**: Python 3.x, Flask
- **Frontend**: HTML5, CSS3, JavaScript (ES6+), Jinja2 Templates
- **Data & APIs**: JSON-based step tracing & quiz question bank

---

## 📂 Project Structure

```text
DSA-Visual-Lab-Assistant/
├── algorithms.py          # Core algorithmic step-generation logic
├── app.py                 # Flask server and routing endpoints
├── enrich_quiz.py         # Utility script for managing/enriching quiz data
├── quiz.json              # Base quiz configuration
├── quiz_questions.json    # Extensive question bank for quizzes
├── static/                # Stylesheets, scripts, images, and static assets
│   ├── css/
│   ├── js/
│   └── images/
├── templates/             # Jinja2 HTML templates for each visualizer
│   ├── dashboard.html     # Main landing page & visualizer hub
│   ├── linear_search.html # Linear search visualizer
│   ├── binary_search.html # Binary search visualizer
│   ├── bubble_sort.html   # Bubble sort visualizer
│   ├── merge_sort.html    # Merge sort visualizer
│   ├── quick_sort.html    # Quick sort visualizer
│   ├── heap_sort.html     # Heap sort visualizer
│   ├── stack.html         # Stack data structure visualizer
│   ├── queue.html         # Queue data structure visualizer
│   ├── BFS.html           # Breadth-First Search visualizer
│   ├── DFS.html           # Depth-First Search visualizer
│   ├── quiz.html          # Interactive quiz arena
│   └── visualize.html     # Generic visualization hub
└── venv/                  # Python Virtual Environment
```

---

## ⚡ Quickstart & Setup Guide

### 1. Clone the Repository & Navigate

```bash
git clone https://github.com/your-username/DSA-Visual-Lab-Assistant.git
cd DSA-Visual-Lab-Assistant
```

### 2. Set Up Virtual Environment

#### On Windows (PowerShell):
```powershell
# Create venv if not already created
python -m venv venv

# Activate venv
.\venv\Scripts\Activate.ps1
```

> *If you encounter a script execution error in PowerShell, run: `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`*

#### On Windows (Command Prompt - CMD):
```cmd
venv\Scripts\activate.bat
```

#### On Linux / macOS / Git Bash:
```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install flask
```
*(or `pip install -r requirements.txt` if available)*

### 4. Run the Application

```bash
python app.py
```

### 5. Open in Browser

Navigate to **[http://127.0.0.1:5000](http://127.0.0.1:5000)** (or `http://localhost:5000`) in any modern web browser.

---

## 🔌 API Endpoints Summary

| Endpoint | Method | Description |
| :--- | :---: | :--- |
| `/` | `GET` | Main Dashboard |
| `/linear_search` | `GET` | Linear Search Visualizer |
| `/binary_search` | `GET` | Binary Search Visualizer |
| `/bubble_sort` | `GET` | Bubble Sort Visualizer |
| `/merge_sort` | `GET` | Merge Sort Visualizer |
| `/quick_sort` | `GET` | Quick Sort Visualizer |
| `/heap_sort` | `GET` | Heap Sort Visualizer |
| `/stack` | `GET` | Stack Visualizer |
| `/queue` | `GET` | Queue Visualizer |
| `/bfs` | `GET` | Breadth-First Search (BFS) Visualizer |
| `/dfs` | `GET` | Depth-First Search (DFS) Visualizer |
| `/quiz` | `GET` | Quiz Arena |
| `/quiz-data?algorithm=<name>` | `GET` | Fetches quiz questions by topic |
| `/run-algo` | `POST` | Executes algorithm logic and returns animation step objects |

---

## 🤝 Contributing

Contributions are always welcome!
1. Fork the Project.
2. Create your Feature Branch (`git checkout -b feature/NewVisualizer`).
3. Commit your Changes (`git commit -m 'Add New Visualizer'`).
4. Push to the Branch (`git push origin feature/NewVisualizer`).
5. Open a Pull Request.

---

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.
