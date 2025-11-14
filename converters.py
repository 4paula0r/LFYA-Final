# converters.py

from automata.regex.regex import Regex
from automata.fa.dfa import DFA


def regex_a_dfa(regex):
    r = Regex(regex)
    nfa = r.to_epsilon_nfa()
    return DFA.from_nfa(nfa)


def dfa_a_gramatica(dfa):
    reglas = {}

    for q in dfa.states:
        reglas[str(q)] = []

    start = str(dfa.initial_state)

    for origen, trans in dfa.transition_function.items():
        for simbolo, destino in trans.items():
            reglas[str(origen)].append(f"{simbolo}{destino}")

    for q in dfa.final_states:
        reglas[str(q)].append("ε")

    return start, reglas


def regex_a_dfa_y_gramatica(regex):
    dfa = regex_a_dfa(regex)
    start, reglas = dfa_a_gramatica(dfa)
    return dfa, start, reglas
