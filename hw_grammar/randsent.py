#!/usr/bin/env python3
"""
601.465/665 — Natural Language Processing
Assignment 1: Designing Context-Free Grammars

Assignment written by Jason Eisner
Modified by Kevin Duh
Re-modified by Alexandra DeLucia

Code template written by Alexandra DeLucia,
based on the submitted assignment with Keith Harrigian
and Carlos Aguirre Fall 2019
"""
import os
import sys
import random
import argparse

# Want to know what command-line arguments a program allows?
# Commonly you can ask by passing it the --help option, like this:
#     python randsent.py --help
# This is possible for any program that processes its command-line
# arguments using the argparse module, as we do below.
#
# NOTE: When you use the Python argparse module, parse_args() is the
# traditional name for the function that you create to analyze the
# command line.  Parsing the command line is different from parsing a
# natural-language sentence.  It's easier.  But in both cases,
# "parsing" a string means identifying the elements of the string and
# the roles they play.

def parse_args():
    """
    Parse command-line arguments.

    Returns:
        args (an argparse.Namespace): Stores command-line attributes
    """
    # Initialize parser
    parser = argparse.ArgumentParser(description="Generate random sentences from a PCFG")
    # Grammar file (required argument)
    parser.add_argument(
        "-g",
        "--grammar",
        type=str, required=True,
        help="Path to grammar file",
    )
    # Start symbol of the grammar
    parser.add_argument(
        "-s",
        "--start_symbol",
        type=str,
        help="Start symbol of the grammar (default is ROOT)",
        default="ROOT",
    )
    # Number of sentences
    parser.add_argument(
        "-n",
        "--num_sentences",
        type=int,
        help="Number of sentences to generate (default is 1)",
        default=1,
    )
    # Max number of nonterminals to expand when generating a sentence
    parser.add_argument(
        "-M",
        "--max_expansions",
        type=int,
        help="Max number of nonterminals to expand when generating a sentence",
        default=450,
    )
    # Print the derivation tree for each generated sentence
    parser.add_argument(
        "-t",
        "--tree",
        action="store_true",
        help="Print the derivation tree for each generated sentence",
        default=False,
    )
    return parser.parse_args()


class Grammar:
    def __init__(self, grammar_file):
        """
        Context-Free Grammar (CFG) Sentence Generator

        Args:
            grammar_file (str): Path to a .gr grammar file
        
        Returns:
            self
        """
        # Parse the input grammar file
        self.rules = None
        self._load_rules_from_file(grammar_file)

    def _load_rules_from_file(self, grammar_file):
        """
        Read grammar file and store its rules in self.rules

        Args:
            grammar_file (str): Path to the raw grammar file 
        """
        self.rules = {}
        with open (grammar_file,"r") as file:
            for line in file:
                if not line.strip():
                    continue
                if line[0] == "#":
                    continue
                parts = line.strip().split()

                if parts[1] not in self.rules.keys():
                    self.rules[parts[1]] = {"weights": [float(parts[0])], "rules": []}
                else:
                    self.rules[parts[1]]["weights"].append(float(parts[0]))
                rules_list = []

                for rules in parts[2:]:
                    if "#" in rules:
                        break
                    rules_list.append(rules)
                self.rules[parts[1]]["rules"].append(rules_list)
    
        

    def sample(self, derivation_tree, max_expansions, start_symbol):
        """
        Sample a random sentence from this grammar

        Args:
            derivation_tree (bool): if true, the returned string will represent 
                the tree (using bracket notation) that records how the sentence 
                was derived
                               
            max_expansions (int): max number of nonterminal expansions we allow

            start_symbol (str): start symbol to generate from

        Returns:
            str: the random sentence or its derivation tree
        """
        results = []
        total_expansions = 0
        if not derivation_tree:
            stack = [start_symbol]
            while stack:
                if total_expansions > max_expansions:
                    results.append("...")
                    break
                symbol = stack.pop()
                if symbol in self.rules:
                    RHS = random.choices(self.rules[symbol]["rules"], weights=self.rules[symbol]["weights"], k=1)[0]
                    total_expansions += 1
                    stack.extend(reversed(RHS))
                else:
                    # terminate
                    results.append(symbol)
            return " ".join(results)
        else:
            stack = [(start_symbol, "enter")]
            while stack:
                if total_expansions > max_expansions:
                    results.append("...")
                    break

                symbol, state = stack.pop()
                if state == "exit":
                    results.append(")")
                    continue

                # enter
                if symbol in self.rules:
                    results.append(f"({symbol}")
                    stack.append((symbol, "exit"))
                    rhs = random.choices(self.rules[symbol]["rules"],
                                     weights=self.rules[symbol]["weights"], k=1)[0]
                    total_expansions += 1
                    for sym in reversed(rhs):
                        stack.append((sym, "enter"))
                else:
                    results.append(symbol)

            return " ".join(results)


####################
### Main Program
####################
def main():
    # Parse command-line options
    args = parse_args()

    # Initialize Grammar object
    grammar = Grammar(args.grammar)

    # Generate sentences
    for i in range(args.num_sentences):
        # Use Grammar object to generate sentence
        sentence = grammar.sample(
            derivation_tree=args.tree,
            max_expansions=args.max_expansions,
            start_symbol=args.start_symbol
        )

        # Print the sentence with the specified format.
        # If it's a tree, we'll pipe the output through the prettyprint script.
        if args.tree:
            prettyprint_path = os.path.join(os.getcwd(), 'prettyprint')
            t = os.system(f"echo '{sentence}' | perl {prettyprint_path}")
        else:
            print(sentence)


if __name__ == "__main__":
    main()
