import imageio.v2 as imageio
import networkx as nx
import matplotlib.pyplot as plt
import os
from IPython.display import display, Image
import matplotlib

matplotlib.rcParams['axes.unicode_minus'] = False
#pozycje węzłów
pos = {
    'q0': (0, 0), 'q1': (-2, 1), 'q2': (2, 1), 'q3': (2, -1),
    'q4': (4, 1), 'q5': (4, -1), 'q6': (6, 0), 'q7': (3, 0),
    'qr': (8, 1), 'qa': (-2, 2),
    'qr1': (0, 1), 'qr2': (0, 1), 'qr3': (0, -1), 'qr4': (6, 1), 'qr5': (6, -1)  # Pozycje dla stanów odrzucających
}

class TuringMachine:
    def __init__(self, states, input_alphabet, tape_alphabet, transition_function, start_state, accept_state, reject_states):
        self.states = states
        self.input_alphabet = input_alphabet
        self.tape_alphabet = tape_alphabet
        self.transition_function = transition_function
        self.start_state = start_state
        self.accept_state = accept_state
        self.reject_states = reject_states  # Zmieniono na zbiór różnych stanów odrzucenia
        self.blank = '_'

    def run(self, word):
        tape = list(word) + [self.blank]
        head_position = 0
        state = self.start_state
        history = []

        while state != self.accept_state and state not in self.reject_states:
            if head_position >= len(tape):
                tape.append(self.blank)
            symbol = tape[head_position]
            history.append((state, head_position, tape.copy()))

            if (state, symbol) not in self.transition_function:
                break

            new_state, new_symbol, move = self.transition_function[(state, symbol)]
            tape[head_position] = new_symbol
            state = new_state

            if move == 'R':
                head_position += 1
            elif move == 'L' and head_position > 0:
                head_position -= 1

        history.append((state, head_position, tape.copy()))
        return history

    def visualize(self, history, filename='simulation.gif'):
        G = nx.MultiDiGraph()
        edge_labels = {}

        for (state, symbol), (new_state, new_symbol, move) in self.transition_function.items():
            if state == 'qa' and new_state == 'qa':
                continue
            if state in self.reject_states and new_state == state:
                continue
            G.add_edge(state, new_state)
            edge_labels.setdefault((state, new_state), set()).add(f'{symbol}->{new_symbol},{move}')

        #dodanie strzałek
        G.add_edge('q1', 'qr1')
        G.add_edge('q2', 'qr2')
        G.add_edge('q3', 'qr3')
        G.add_edge('q5', 'qr5')
        G.add_edge('q4', 'qr4')
        G.add_edge('q4', 'q6')

        #dodanie stanów odrzucenia
        for i in range(1, 6):
            G.add_node(f'qr{i}', color='red')
        G.add_node('qa', color='green')

        edge_labels = {k: "\n".join(sorted(v)) for k, v in edge_labels.items()}
        frames = []
        temp_dir = "temp_frames"
        os.makedirs(temp_dir, exist_ok=True)

        for i, (state, head_pos, tape) in enumerate(history):
            plt.figure(figsize=(10, 6))
            node_colors = [G.nodes[n].get('color', 'grey') if n != state else 'blue' for n in G.nodes]
            labels = {node: 'qr' if 'qr' in node else node for node in G.nodes} #węzły qr1 qr2 itd wyświetlają 'qr' zamiast swojej etykiety
            nx.draw_networkx_labels(G, pos, labels=labels, font_size=12)
            nx.draw(G, pos, with_labels=True, labels=labels, node_size=2000, node_color=node_colors, font_size=12)
            nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8)
            plt.title(f'Step {i}: State {state}, Tape: {"".join(tape)}')
            frame_path = os.path.join(temp_dir, f'frame_{i}.png')
            plt.savefig(frame_path, format='png', dpi=300)
            plt.close()
            frames.append(frame_path)

        images = [imageio.imread(frame) for frame in frames]
        imageio.mimsave(filename, images, duration=1.5, loop=0)
        display(Image(filename=filename))

        for frame in frames:
            os.remove(frame)
        os.rmdir(temp_dir)

states = {'q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'qr1', 'qr2', 'qr3', 'qr4', 'qr5', 'qa'}
input_alphabet = {'0', '1', 'b'}
tape_alphabet = {'0', '1', 'b', '_', '0/', '1/'}
transition_function = {
    ('q0', 'b'): ('q1', 'b', 'R'),
    ('q0', '0'): ('q2', '0/', 'R'),
    ('q0', '1'): ('q3', '1/', 'R'),

    ('q1', '_'): ('qa', '_', 'L'),
    ('q1', '0/'): ('q1', '0/', 'R'),
    ('q1', '1/'): ('q1', '1/', 'R'),
    ('q1', '0'): ('qr1', '0', 'L'),
    ('q1', '1'): ('qr1', '1', 'L'),

    ('q2', '_'): ('qr2', '_', 'R'),
    ('q2', '0'): ('q2', '0', 'R'),
    ('q2', '1'): ('q2', '1', 'R'),
    ('q2', 'b'): ('q4', 'b', 'R'),

    ('q3', '0'): ('q3', '0', 'R'),
    ('q3', '1'): ('q3', '1', 'R'),
    ('q3', '_'): ('qr3', '_', 'R'),
    ('q3', 'b'): ('q5', 'b', 'R'),

    ('q4', '0/'): ('q4', '0/', 'R'),
    ('q4', '1/'): ('q4', '1/', 'R'),
    ('q4', '0'): ('q6', '0/', 'L'),
    ('q4', '0'): ('qr4', '0', 'L'),

    ('q5', '0/'): ('q5', '0/', 'R'),
    ('q5', '1/'): ('q5', '1/', 'R'),
    ('q5', '1'): ('q6', '1/', 'L'),
    ('q5', '_'): ('qr5', '_', 'R'),
    ('q5', '0'): ('qr5', '0', 'L'),

    ('q6', '0/'): ('q6', '0/', 'L'),
    ('q6', '1/'): ('q6', '1/', 'L'),
    ('q6', 'b'): ('q7', 'b', 'L'),

    ('q7', '0/'): ('q0', '0/', 'R'),
    ('q7', '1/'): ('q0', '1/', 'R'),

    ('qr1', '0'): ('qr1', '0', 'R'),
    ('qr1', '1'): ('qr1', '1', 'R'),

    ('qr2', '0'): ('qr2', '0', 'R'),
    ('qr2', '1'): ('qr2', '1', 'R'),

    ('qr3', '0'): ('qr3', '0', 'R'),
    ('qr3', '1'): ('qr3', '1', 'R'),

    ('qr4', '0'): ('qr4', '0', 'R'),
    ('qr4', '1'): ('qr4', '1', 'R'),

    ('qr5', '0'): ('qr5', '0', 'R'),
    ('qr5', '1'): ('qr5', '1', 'R'),

    ('qa', '0'): ('qa', '0', 'R'),
    ('qa', '1'): ('qa', '1', 'R')
}

start_state = 'q0'
accept_state = 'qa'
reject_states = {'qr1', 'qr2', 'qr3', 'qr4', 'qr5'}

tm = TuringMachine(states, input_alphabet, tape_alphabet, transition_function, start_state, accept_state, reject_states)
input_word = input("Podaj słowo wejściowe: ")
history = tm.run(input_word)
tm.visualize(history)


