from graphviz import Digraph

def visualize_dfa():
    dot = Digraph(comment='DFA Elevator Model')

    # Define states
    states = ['F1', 'F2', 'F3']
    inputs = ['req1', 'req2', 'req3']
    transitions = {
        'F1': {'req1': 'F1', 'req2': 'F2', 'req3': 'F3'},
        'F2': {'req1': 'F1', 'req2': 'F2', 'req3': 'F3'},
        'F3': {'req1': 'F1', 'req2': 'F2', 'req3': 'F3'}
    }

    # Mark start state
    dot.node('start', '', shape='point')
    dot.edge('start', 'F1', label='start')

    # Add all states
    for state in states:
        dot.node(state, state, shape='circle')

    # Add transitions
    for from_state in transitions:
        for inp, to_state in transitions[from_state].items():
            dot.edge(from_state, to_state, label=inp)

    # Output as PDF and render
    dot.render('dfa_elevator_diagram', format='pdf', view=True)

visualize_dfa()
