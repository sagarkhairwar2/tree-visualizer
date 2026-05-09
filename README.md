# Tree Visualizer

An interactive Tree Visualization project built using Flask, Python, HTML, SVG, CSS.

This project visualizes hierarchical tree structures with features like expand/collapse, random tree generation, node search, zoom controls, and tree statistics.

---

# Live Demo

Add your deployed Render link here:

```text
https://tree-visualizer-3wky.onrender.com
```

---

# GitHub Repository

Add your GitHub repository link here:

```text
https://github.com/sagarkhairwar2/tree-visualizer.git
```

---

# Features

- Recursive tree rendering
- Expand / collapse nodes
- Random tree generation
- Search and highlight nodes
- Tree statistics display
- Zoom in / Zoom out
- SVG-based visualization
- Scroll position persistence
- Zoom state persistence

---

# Technologies Used

- Python
- Flask
- HTML
- CSS
- SVG
- Git
- GitHub
- Render

---

# Project Structure

```text
tree-visualizer/
│
├── app.py
├── requirements.txt
├── README.md
│
├── templates/
│   └── index.html
│
├── screenshots/
│   ├── home.png
│   ├── collapse.png
│   ├── random_tree.png
│   └── search.png
```

---

# Installation

Clone repository:

```bash
git clone https://github.com/sagarkhairwar2/tree-visualizer.git
```

Move inside project folder:

```bash
cd tree-visualizer
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run Flask server:

```bash
python app.py
```

Open browser:

```text
http://127.0.0.1:5000
```

---

# Deployment

This project is deployed using Render.

Build Command:

```text
pip install -r requirements.txt
```

Start Command:

```text
gunicorn app:app
```

---

# Screenshots

## Home Page

Add screenshot here:

```md
![Home Page](screenshots/home.png)
```

Suggested screenshot:
- Full tree visualization
- Toolbar visible
- Zoom buttons visible

---

## Collapse Functionality

Add screenshot here:

```md
![Collapse Functionality](screenshots/collapse.png)
```

Suggested screenshot:
- One subtree collapsed
- "+" collapse icon visible

---

## Random Tree Generation

Add screenshot here:

```md
![Random Tree](screenshots/random_tree.png)
```

Suggested screenshot:
- Randomly generated large tree

---

## Search and Highlight

Add screenshot here:

```md
![Search Feature](screenshots/search.png)
```

Suggested screenshot:
- Highlighted searched node

---

# How the Layout Algorithm Works

The project uses a recursive tree layout algorithm.

## Logic

- Every node stores:
  - x coordinate
  - y coordinate

- Leaf nodes are positioned sequentially from left to right.

- Parent nodes are centered between their first and last child.

- Collapsed nodes stop recursive rendering of their subtree.

## Advantages

- Simple recursive implementation
- Easy expand/collapse support
- Readable tree structure
- Dynamic rendering

---

# Tree Features

## Expand / Collapse

- Nodes with children can be expanded or collapsed.
- Collapse state is stored dynamically.

## Random Tree Generation

- Random trees are generated recursively.
- Maximum node limit prevents huge graph generation.

## Search System

- Search box highlights matching nodes.
- Matching nodes are displayed in red color.

## Zoom System

- Zoom in and zoom out supported.
- Zoom level is preserved using browser localStorage.

## Scroll Persistence

- Scroll position is restored after page reload.
- Improves user experience during tree interaction.

---

# Future Improvements

- Better automatic layout optimization
- Node dragging
- Export as image
- Editable nodes
- Database support
- Large-scale graph optimization

---

# Learning Outcomes

This project helped in understanding:

- Recursion
- Tree data structures
- Graph visualization
- SVG rendering
- Flask backend development
- UI interaction
- State management
- Deployment workflow
- Git and GitHub

---

# Author

Your Name Here

---

# License

This project is created for educational and learning purposes.
