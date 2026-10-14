from flask import Flask, render_template, jsonify, request
import algorithms
import json

app = Flask(__name__, template_folder="templates")

# -------------------- ROUTES ------------------

@app.route("/")
def index():
    return render_template("dashboard.html")


@app.route("/visualize")
def visualize():
    topic = request.args.get("topic")  # example: ?topic=linear
    return render_template("visualize.html", current_topic=topic)


@app.route("/linear_search")
def linear_search_page():
    return render_template("linear_search.html")



@app.route("/bfs")
def bfs_page():
    return render_template("BFS.html")

@app.route("/dfs")
def dfs_page():
    return render_template("DFS.html")

@app.route("/binary_search")
def binary_search_page():
    return render_template("binary_search.html")


@app.route("/merge_sort")
def merge_sort_page():
    return render_template("merge_sort.html")


@app.route("/bubble_sort")
def bubble_sort_page():
    return render_template("bubble_sort.html")


@app.route("/heap_sort")
def heap_sort_page():
    return render_template("heap_sort.html")


@app.route("/quick_sort")
def quick_sort_page():
    return render_template("quick_sort.html")


@app.route("/stack")
def stack_page():
    return render_template("stack.html")


@app.route("/queue")
def queue_page():
    return render_template("queue.html")


@app.route("/quiz")
def quiz():
    return render_template("quiz.html")


# -------------------- AUTOMATA THEORY ROUTES ------------------

@app.route("/automata")
@app.route("/automata/dfa-dungeon")
@app.route("/dfa")
def dfa_page():
    return render_template("dfa_dungeon.html")


@app.route("/nfa")
@app.route("/automata/nfa-quantum")
def nfa_page():
    return render_template("nfa_quantum.html")


@app.route("/enfa")
@app.route("/enfa-to-dfa")
@app.route("/automata/enfa-to-dfa")
def enfa_page():
    return render_template("epsilon_nfa.html")


@app.route("/enfa-eliminate")
@app.route("/automata/eliminate-epsilon")
@app.route("/bridgebusters")
def enfa_eliminate_page():
    return render_template("enfa_eliminate.html")


@app.route("/moore-mealy")
@app.route("/automata/moore-to-mealy")
@app.route("/badge-thief")
def moore_mealy_page():
    return render_template("moore_mealy.html")



@app.route("/api/dfa/validate", methods=["POST"])
def validate_dfa_string():
    """
    Validates a binary string against the Neso Academy Example 4 DFA:
    States: A, B, C, D, E, X
    Alphabet: 0, 1
    Start: A
    Final: D, E
    Dead: X
    Language: 01 | 1+0
    """
    data = request.get_json(force=True) or {}
    raw_str = str(data.get("string", "")).strip()

    # DFA Transitions Delta: (current_state, symbol) -> next_state
    transitions = {
        ("A", "0"): "C", ("A", "1"): "B",
        ("B", "0"): "D", ("B", "1"): "B",
        ("C", "0"): "X", ("C", "1"): "E",
        ("D", "0"): "X", ("D", "1"): "X",
        ("E", "0"): "X", ("E", "1"): "X",
        ("X", "0"): "X", ("X", "1"): "X",
    }
    final_states = {"D", "E"}

    current = "A"
    steps = [{
        "step_idx": 0,
        "symbol": None,
        "from_state": None,
        "to_state": "A",
        "description": "BitBot starts at Initial State A (q0)",
        "is_dead": False,
        "is_accepting": False
    }]

    for idx, char in enumerate(raw_str):
        if char not in ("0", "1"):
            return jsonify({
                "error": f"Invalid character '{char}'. The alphabet Σ is strictly {{'0', '1'}}."
            }), 400

        from_s = current
        to_s = transitions.get((from_s, char), "X")
        current = to_s

        desc = f"Read '{char}' from state {from_s} -> transitioned to {to_s}"
        if to_s == "X":
            if from_s == "X":
                desc = f"Read '{char}' in Dead State X -> looping in Trap forever"
            else:
                desc = f"Read '{char}' from {from_s} -> no valid path forward! Fell into Dead State X (Trap)"
        elif to_s in ("D", "E"):
            desc = f"Read '{char}' from {from_s} -> reached Treasure Room {to_s} (Accepting State)"

        steps.append({
            "step_idx": idx + 1,
            "symbol": char,
            "from_state": from_s,
            "to_state": to_s,
            "description": desc,
            "is_dead": (to_s == "X"),
            "is_accepting": (to_s in final_states)
        })

    is_accepted = (current in final_states)

    return jsonify({
        "string": raw_str,
        "length": len(raw_str),
        "final_state": current,
        "is_accepted": is_accepted,
        "is_dead": (current == "X"),
        "steps": steps,
        "rule": "01 | 1+0 (Either '01', or one/more '1's followed by a single '0')"
    })



@app.route("/quiz-data")
def quiz_data():
    algorithm = request.args.get("algorithm", "").lower()
    try:
        with open("quiz_questions.json") as f:
            all_questions = json.load(f)
    except Exception as e:
        return jsonify({"error": f"Failed to load quiz questions: {e}"}), 500

    if algorithm not in all_questions:
        return jsonify({"error": f"No questions found for '{algorithm}'"}), 404

    return jsonify(all_questions[algorithm])


# -------------------- RUN ALGORITHM --------------------
# -------------------- RUN ALGORITHM --------------------
@app.route("/run-algo", methods=["POST"])
@app.route("/run-dfs-steps", methods=["POST"])  # alias for compatibility
def run_algo():
    data = request.get_json(force=True)
    algo = data.get("algo")
    arr = data.get("arr") or []
    target = data.get("target")
    ops = data.get("ops") or []
    graph = data.get("graph") or {}
    start = data.get("start")

    try:
        if algo == "bubble":
            _, steps = algorithms.bubble_sort_steps(arr)
        elif algo == "merge":
            steps = algorithms.merge_sort_steps(arr)
        elif algo == "quick":
            _, steps = algorithms.quick_sort_steps(arr)
        elif algo == "heap":
            # Only return steps from heap_sort_steps
            steps = algorithms.heap_sort_steps(arr, heap_type=data.get("heap_type", "max"))
        elif algo == "linear":
            steps = algorithms.linear_search_steps(arr, target)
        elif algo == "binary":
            steps = algorithms.binary_search_steps(arr, target)
        elif algo == "stack":
            steps = algorithms.stack_steps(ops)
        elif algo == "queue":
            steps = algorithms.queue_steps(ops)
        elif algo == "dfs":
            steps = algorithms.dfs_steps(graph, start)
        elif algo == "bfs":
            steps = algorithms.bfs_steps(graph, start)
        else:
            return jsonify({"error": f"Unknown algorithm: {algo}"}), 400

        return jsonify({"steps": steps})

    except Exception as e:
        print(f"Algorithm execution failed for {algo}: {e}")
        return jsonify({"error": "Algorithm execution failed. Check console for details."}), 500


# -------------------- MAIN --------------------
if __name__ == "__main__":
    app.run(debug=True, port=5000)
