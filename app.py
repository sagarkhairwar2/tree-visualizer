from flask import Flask, render_template, redirect, request
import random

app = Flask(__name__)

# GLOBAL STORAGE
collapsed_nodes = set()
current_root = None
MAX_RANDOM_NODES = 35
generated_nodes = 0

# TREE NODE CLASS
class TreeNode:
    def __init__(self, node_id, name, children=None):
        self.id = node_id
        self.name = name
        self.children = children or []

        self.x = 0
        self.y = 0

        self.collapsed = False

# LAYOUT SETTINGS
current_x = 200

HORIZONTAL_SPACING = 170
VERTICAL_SPACING = 170

NODE_WIDTH = 120
NODE_HEIGHT = 50

# APPLY COLLAPSE STATE
def apply_collapse_state(node):
    node.collapsed = node.id in collapsed_nodes
    for child in node.children:
        apply_collapse_state(child)

# LAYOUT ALGORITHM
def assign_positions(node, depth=0):
    global current_x
    node.y = depth * VERTICAL_SPACING + 150

    if not node.children or node.collapsed:
        node.x = current_x
        current_x += HORIZONTAL_SPACING
    else:
        for child in node.children:
            assign_positions(child, depth + 1)

        first_child = node.children[0]
        last_child = node.children[-1]

        node.x = (first_child.x + last_child.x) / 2

# GENERATE GRAPH
def generate_graph(node, nodes=None, edges=None, depth=0):
    if nodes is None:
        nodes = []

    if edges is None:
        edges = []

    nodes.append({
        "id": node.id,
        "name": node.name,
        "x": node.x,
        "y": node.y,
        "collapsed": node.collapsed,
        "has_children": len(node.children) > 0,
        "children_count": len(node.children),
        "depth": depth
    })

    if node.collapsed:
        return nodes, edges

    for child in node.children:
        edges.append({
            "source_x": node.x,
            "source_y": node.y,
            "target_x": child.x,
            "target_y": child.y
        })

        generate_graph(child, nodes, edges, depth + 1)
    return nodes, edges

# TREE STATISTICS
def count_nodes(node):
    total = 1
    for child in node.children:
        total += count_nodes(child)
    return total

def count_leaf_nodes(node):
    if not node.children:
        return 1

    total = 0
    for child in node.children:
        total += count_leaf_nodes(child)

    return total

def tree_depth(node):
    if not node.children:
        return 1
    return 1 + max(tree_depth(child) for child in node.children)

# SEARCH
def search_nodes(nodes, search_text):
    for node in nodes:
        if search_text and search_text.lower() in node["name"].lower():
            node["highlight"] = True
        else:
            node["highlight"] = False
    return nodes

# RANDOM TREE
def random_tree(level, max_level, prefix="Node"):

    global generated_nodes

    if generated_nodes >= MAX_RANDOM_NODES:

        return TreeNode(
            f"leaf_{random.randint(1,999)}",
            "Leaf"
        )

    node_id = f"{prefix}_{random.randint(1, 999999)}"

    generated_nodes += 1

    if level >= max_level:

        return TreeNode(
            node_id,
            f"{prefix}_{level}"
        )

    child_count = random.randint(2, 4)

    children = []

    for i in range(child_count):

        children.append(
            random_tree(
                level + 1,
                max_level,
                f"{prefix}_{i}"
            )
        )

    return TreeNode(
        node_id,
        f"{prefix}_{level}",
        children
    )

# DEFAULT TREE
def build_default_tree():
    child1 = TreeNode(
        "child1",
        "Child 1",
        [
            TreeNode("child1_a", "A"),
            TreeNode("child1_b", "B"),
            TreeNode("child1_c", "C")
        ]
    )

    child2 = TreeNode(
        "child2",
        "Child 2",
        [
            TreeNode("child2_a", "D"),
            TreeNode("child2_b", "E")
        ]
    )

    child4 = TreeNode(
        "child4",
        "Child 4",
        [
            TreeNode("child4_a", "F")
        ]
    )

    root = TreeNode(
        "root",
        "ROOT",
        [
            child1,
            child2,
            TreeNode("node5", "G"),
            child4,
            TreeNode("node6", "H"),
            TreeNode("node7", "I")
        ]
    )

    return root

# INITIALIZE TREE
current_root = build_default_tree()

# TOGGLE
@app.route("/toggle/<node_id>")
def toggle(node_id):

    if node_id in collapsed_nodes:
        collapsed_nodes.remove(node_id)
    else:
        collapsed_nodes.add(node_id)

    return redirect("/")

# RANDOM TREE
@app.route("/random")
def random_page():

    global current_root
    global collapsed_nodes
    global generated_nodes

    generated_nodes = 0
    collapsed_nodes.clear()
    current_root = random_tree(1, 4, "Random")

    return redirect("/")

# HOME

@app.route("/")
def home():

    global current_root
    global current_x

    current_x = 200

    apply_collapse_state(current_root)
    assign_positions(current_root)

    nodes, edges = generate_graph(current_root)
    search_text = request.args.get("search", "")
    nodes = search_nodes(nodes, search_text)

    total_nodes = count_nodes(current_root)
    leaf_nodes = count_leaf_nodes(current_root)
    depth = tree_depth(current_root)

    return render_template(
        "index.html",
        nodes=nodes,
        edges=edges,
        node_width=NODE_WIDTH,
        node_height=NODE_HEIGHT,
        total_nodes=total_nodes,
        leaf_nodes=leaf_nodes,
        tree_depth_value=depth,
        collapsed_count=len(collapsed_nodes),
        search_text=search_text
    )

# RUN
if __name__ == "__main__":
    app.run(debug=True)