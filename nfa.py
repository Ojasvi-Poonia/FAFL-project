from graphviz import Digraph
from collections import defaultdict

def visualize_nfa():
    dot = Digraph(comment='NFA Elevator Model')

    # Define states and input symbols
    states = ['F1', 'F2', 'F3']
    inputs = ['req1', 'req2', 'req3']

    # Create NFA transition table with nondeterminism
    transitions = defaultdict(lambda: defaultdict(set))
    transitions['F1']['req1'].add('F1')
    transitions['F1']['req2'].update(['F2', 'F3'])  # Non-deterministic
    transitions['F1']['req3'].add('F3')

    transitions['F2']['req1'].add('F1')
    transitions['F2']['req2'].add('F2')
    transitions['F2']['req3'].add('F3')

    transitions['F3']['req1'].add('F1')
    transitions['F3']['req2'].add('F2')
    transitions['F3']['req3'].add('F3')

    # Start state
    dot.node('start', '', shape='point')
    dot.edge('start', 'F1', label='start')

    # Create nodes
    for state in states:
        dot.node(state, state, shape='circle')

    # Create edges (including nondeterministic multiple edges)
    for from_state, input_dict in transitions.items():
        for input_symbol, to_states in input_dict.items():
            for to_state in to_states:
                dot.edge(from_state, to_state, label=input_symbol)

    # Render output
    dot.render('nfa_elevator_diagram', format='pdf', view=True)

visualize_nfa()
