import json

automata_questions = [
    {
        "question": "What is the primary role of a Dead State (or Trap State) in a Deterministic Finite Automaton (DFA)?",
        "options": [
            "To make the DFA non-deterministic",
            "To trap strings that can never lead to an accepting state, ensuring total transition completeness",
            "To reduce the total number of states in any machine",
            "To accept strings containing epsilon transitions"
        ],
        "answer": "To trap strings that can never lead to an accepting state, ensuring total transition completeness",
        "explanation": "In a formal DFA, every state must define exactly one transition for every input symbol in alphabet Sigma. A Dead State acts as an inescapable non-accepting sinkhole for rejected prefixes.",
        "option_reasons": {
            "To make the DFA non-deterministic": "Incorrect. DFAs remain strictly deterministic regardless of whether dead states are present.",
            "To trap strings that can never lead to an accepting state, ensuring total transition completeness": "Correct! Once a prefix cannot be extended into a valid string in L, it transitions to a Dead State which loops on all alphabet symbols forever.",
            "To reduce the total number of states in any machine": "Incorrect. Adding a dead state increases the state count by 1 to satisfy formal mathematical completeness.",
            "To accept strings containing epsilon transitions": "Incorrect. Dead states are non-accepting, and DFAs do not allow epsilon transitions."
        }
    },
    {
        "question": "For the language L = {01} U {1^n 0 | n >= 1}, which of the following strings is ACCEPTED by the DFA?",
        "options": ["0010", "010", "1110", "1101"],
        "answer": "1110",
        "explanation": "The language accepts either the exact string '01' or one or more '1's followed by exactly one '0'. '1110' has three '1's followed by a single '0', matching 1^+ 0.",
        "option_reasons": {
            "0010": "Incorrect. '0010' starts with two zeros, violating the pattern and entering the Dead State X.",
            "010": "Incorrect. '010' contains an extra '0' after '01'. At state E, reading another bit sends the machine to Dead State X.",
            "1110": "Correct! '1110' satisfies 1^+ 0 with n = 3 ones followed by a single zero.",
            "1101": "Incorrect. '1101' contains an extra '1' after reaching accepting state D on '110'."
        }
    },
    {
        "question": "Why is the string '010' rejected by the Neso Academy Example 4 DFA?",
        "options": [
            "Because state E has no transitions defined",
            "Because reading '0' in state E sends the automaton into Dead State X",
            "Because state A rejects all strings starting with 0",
            "Because the string length is odd"
        ],
        "answer": "Because reading '0' in state E sends the automaton into Dead State X",
        "explanation": "State E accepts the exact string '01'. If any additional character arrives (either 0 or 1), the condition 'exact string 01' is violated, so delta(E, 0) = X and delta(E, 1) = X.",
        "option_reasons": {
            "Because state E has no transitions defined": "Incorrect. A complete formal DFA has transitions defined for all symbols; state E transitions to Dead State X on 0 and 1.",
            "Because reading '0' in state E sends the automaton into Dead State X": "Correct! State E is final for '01', and any subsequent symbol transitions to the dead state X.",
            "Because state A rejects all strings starting with 0": "Incorrect. State A transitions to C on '0', which is valid for accepting '01'.",
            "Because the string length is odd": "Incorrect. Acceptance depends strictly on language grammar, not string length parity."
        }
    },
    {
        "question": "In the formal 5-tuple definition of a DFA, M = (Q, Sigma, delta, q0, F), what does F represent?",
        "options": [
            "The initial start state",
            "The alphabet symbols",
            "The set of final (accepting) states",
            "The transition function"
        ],
        "answer": "The set of final (accepting) states",
        "explanation": "F is a subset of Q representing the accepting or final states. If computation halts in a state belonging to F after processing the entire input string, the string is accepted.",
        "option_reasons": {
            "The initial start state": "Incorrect. The start state is denoted by q0 in Q.",
            "The alphabet symbols": "Incorrect. The finite alphabet is denoted by Sigma.",
            "The set of final (accepting) states": "Correct! F is the subset of states in Q that denote accepted strings.",
            "The transition function": "Incorrect. The transition function mapping Q x Sigma -> Q is delta."
        }
    },
    {
        "question": "What are the outgoing transitions from Dead State X in a DFA over alphabet {0, 1}?",
        "options": [
            "delta(X, 0) = A and delta(X, 1) = B",
            "delta(X, 0) = X and delta(X, 1) = X (self-loops)",
            "No outgoing transitions are permitted",
            "delta(X, 0) = null and delta(X, 1) = null"
        ],
        "answer": "delta(X, 0) = X and delta(X, 1) = X (self-loops)",
        "explanation": "By definition, a Dead State is a trap state. Once entered, the machine can never escape regardless of what input symbols arrive, so both 0 and 1 self-loop to X.",
        "option_reasons": {
            "delta(X, 0) = A and delta(X, 1) = B": "Incorrect. Transitions back to live states would violate the property of an inescapable trap.",
            "delta(X, 0) = X and delta(X, 1) = X (self-loops)": "Correct! Self-loops ensure BitBot remains trapped indefinitely.",
            "No outgoing transitions are permitted": "Incorrect. In a formal DFA, every state must define transitions for all alphabet symbols.",
            "delta(X, 0) = null and delta(X, 1) = null": "Incorrect. Formal DFAs do not allow undefined or null transitions."
        }
    },
    {
        "question": "What is the regular expression corresponding to Neso Academy DFA Example 4?",
        "options": [
            "(01)* | (10)*",
            "01 | 1+0",
            "(0 | 1)* 01",
            "1* 01*"
        ],
        "answer": "01 | 1+0",
        "explanation": "The language accepts either '01' or strings starting with one or more 1s followed by a single 0, represented in regex as 01 | 1^+0 (or 01 | 11*0).",
        "option_reasons": {
            "(01)* | (10)*": "Incorrect. This would accept the empty string epsilon and repetitions like 0101, which the DFA rejects.",
            "01 | 1+0": "Correct! Exactly matches the accepted set: {'01', '10', '110', '1110', ...}.",
            "(0 | 1)* 01": "Incorrect. This represents any string ending in 01, which would accept '101' or '001', both rejected by this DFA.",
            "1* 01*": "Incorrect. This allows multiple ones after zero and also accepts '0', which is rejected."
        }
    },
    {
        "question": "What happens if BitBot is at start state A and receives input '1'?",
        "options": [
            "Transitions to state C",
            "Transitions to state B (Loop Room)",
            "Falls directly into Dead State X",
            "Accepts immediately"
        ],
        "answer": "Transitions to state B (Loop Room)",
        "explanation": "In state A, receiving '1' initiates the 1^+0 pattern by moving to state B, which self-loops on additional 1s.",
        "option_reasons": {
            "Transitions to state C": "Incorrect. Input '0' transitions to state C.",
            "Transitions to state B (Loop Room)": "Correct! Delta(A, 1) = B, preparing to accumulate 1s before the final 0.",
            "Falls directly into Dead State X": "Incorrect. '1' is a valid prefix.",
            "Accepts immediately": "Incorrect. B is not an accepting state; a zero must follow to reach state D."
        }
    },
    {
        "question": "How many total states Q exist in the complete DFA for this language?",
        "options": ["4 states", "5 states", "6 states: {A, B, C, D, E, X}", "7 states"],
        "answer": "6 states: {A, B, C, D, E, X}",
        "explanation": "The complete DFA has 6 states: A (start), B (1s loop), C (0 prefix), D (final for 1+0), E (final for 01), and X (dead state).",
        "option_reasons": {
            "4 states": "Incorrect. 4 states is insufficient to distinguish the two disjoint paths and trap states.",
            "5 states": "Incorrect. 5 states would omit the Dead State X, resulting in an incomplete DFA.",
            "6 states: {A, B, C, D, E, X}": "Correct! Exactly 6 states define this minimal complete deterministic automaton.",
            "7 states": "Incorrect. 6 states fully satisfy all language conditions without redundancy."
        }
    },
    {
        "question": "Can a string be accepted if it passes through the Dead State X during computation?",
        "options": [
            "Yes, if the string length is even",
            "Yes, if it encounters an accepting symbol later",
            "Never, because all transitions from X lead back to X, and X is non-accepting",
            "Yes, by backtracking to the previous state"
        ],
        "answer": "Never, because all transitions from X lead back to X, and X is non-accepting",
        "explanation": "A Dead State is an absorbing state. Since delta(X, a) = X for all a in Sigma and X is not in F, no path out of X exists.",
        "option_reasons": {
            "Yes, if the string length is even": "Incorrect. Dead states cannot be exited regardless of string length.",
            "Yes, if it encounters an accepting symbol later": "Incorrect. Once in X, all symbols keep the machine in X.",
            "Never, because all transitions from X lead back to X, and X is non-accepting": "Correct! An absorbing non-final state permanently rejects the string.",
            "Yes, by backtracking to the previous state": "Incorrect. DFAs operate in a strictly forward, memoryless manner without backtracking."
        }
    },
    {
        "question": "Where are Finite Automata and Dead States commonly utilized in modern computing systems?",
        "options": [
            "Only in theoretical puzzles with no real-world use",
            "In Lexical Analyzers (Compilers), Network Protocol Validators, and Regex engines",
            "To increase CPU clock frequencies",
            "In relational database query sorting"
        ],
        "answer": "In Lexical Analyzers (Compilers), Network Protocol Validators, and Regex engines",
        "explanation": "Lexers (like Lex/Flex in compiler design) use DFAs to tokenize keywords and identifiers. Invalid tokens trigger dead states to report syntax errors.",
        "option_reasons": {
            "Only in theoretical puzzles with no real-world use": "Incorrect. Automata theory is the foundation of compiler design, protocol verification, and hardware design.",
            "In Lexical Analyzers (Compilers), Network Protocol Validators, and Regex engines": "Correct! Lexical scanners, TCP state machines, and regex search rely directly on DFAs.",
            "To increase CPU clock frequencies": "Incorrect. DFAs are computational models, not physical clock generators.",
            "In relational database query sorting": "Incorrect. Query sorting uses algorithmic sorting like Quick/Merge Sort."
        }
    }
]

with open('quiz_questions.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

data['automata'] = automata_questions
data['dfa'] = automata_questions

with open('quiz_questions.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2)

print('Successfully updated quiz_questions.json with Automata & DFA questions!')
