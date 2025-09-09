1.4 
(1) 
a sandwich in the floor understood a chief of staff .

is it true that the floor understood a pickle ?

a pickle ate the floor in a perplexed floor .

the delicious floor understood a president .

a floor in a president under the president in every perplexed fine floor with every pickle with a fine delicious pickle under the chief of staff on every pickled perplexed floor in a fine president with a pickle with every delicious pickle on the president with the floor on a chief of staff on every delicious floor under a pickled president in a chief of staff on the sandwich in a delicious chief of staff on every president in every pickle with every sandwich under a chief of staff on every floor under every pickle on the sandwich with a president with the president on a pickle in a president with the pickle under a floor on the pickle in every fine pickle with a president in every floor on a president on a perplexed sandwich in a president in the pickled president on every president on a sandwich under the sandwich in every sandwich under every sandwich in the chief of staff in the chief of staff with a sandwich with the chief of staff under every floor under every president in the floor under the pickle with the perplexed chief of staff with the pickle in the chief of staff under a president under the sandwich with every fine pickle in the chief of staff under the floor with every pickle with the president on the chief of staff in every pickle under the fine pickled sandwich with every pickle on ...

is it true that the perplexed sandwich wanted every chief of staff under a chief of staff in the chief of staff on the pickle in a sandwich in a pickle under every pickle under the sandwich with every delicious floor on a pickled delicious chief of staff in every floor in every chief of staff on the chief of staff on the perplexed sandwich on a floor on a delicious president ?

a sandwich under a fine sandwich ate a floor .

every fine floor understood a sandwich .

every perplexed floor kissed a chief of staff under the perplexed floor !

every chief of staff with the floor with the chief of staff under every floor under the pickled president in a sandwich kissed the sandwich on a sandwich with the chief of staff on the president with a perplexed chief of staff on a perplexed president with a sandwich !

(2) 
(ROOT (S (NP (NP (Det a)
                 (Noun pickle))
             (PP (Prep under)
                 (NP (NP (NP (Det the)
                             (Noun (Adj pickled)
                                   (Noun chief
                                         of
                                         staff)))
                         (PP (Prep in)
                             (NP (NP (NP (NP (Det the)
                                             (Noun pickle))
                                         (PP (Prep with)
                                             (NP (Det the)
                                                 (Noun sandwich))))
                                     (PP (Prep in)
                                         (NP (NP (NP (Det a)
                                                     (Noun sandwich))
                                                 (PP (Prep in)
                                                     (NP (NP (NP (NP (Det the)
                                                                     (Noun president))
                                                                 (PP (Prep in)
                                                                     (NP (Det every)
                                                                         (Noun sandwich))))
                                                             (PP (Prep in)
                                                                 (NP (Det the)
                                                                     (Noun floor))))
                                                         (PP (Prep in)
                                                             (NP (Det the)
                                                                 (Noun pickle))))))
                                             (PP (Prep on)
                                                 (NP (Det the)
                                                     (Noun floor))))))
                                 (PP (Prep with)
                                     (NP (Det the)
                                         (Noun (Adj pickled)
                                               (Noun president)))))))
                     (PP (Prep on)
                         (NP (Det every)
                             (Noun (Adj perplexed)
                                   (Noun (Adj delicious)
                                         (Noun president))))))))
         (VP (Verb pickled)
             (NP (NP (Det every)
                     (Noun president))
                 (PP (Prep in)
                     (NP (NP (Det every)
                             (Noun president))
                         (PP (Prep in)
                             (NP (Det the)
                                 (Noun (Adj fine)
                                       (Noun pickle)))))))))
      !)

(ROOT is
      it
      true
      that
      (S (NP (NP (Det every)
                 (Noun (Adj pickled)
                       (Noun chief
                             of
                             staff)))
             (PP (Prep in)
                 (NP (Det a)
                     (Noun chief
                           of
                           staff))))
         (VP (Verb wanted)
             (NP (Det every)
                 (Noun floor))))
      ?)

(3)
(ROOT (S (NP (Det every)
             (Noun ...))
         ...)
      .)

(ROOT is
      it
      true
      that
      (S (NP (NP (Det every)
                 ...)
             ...)
         ...)
      ?)

2.1
(1) The reason is that the basic grammar rules have some loops in it, which make recursive DFS hard to find a way out. Nonterminals are very likely to link to itself along the process, and make quick terminating less likely. With the given probability of each rule being used, this can be very common.

VP -> VP PP is mainly responsible for this because it creates loops (left-recursive). It introduces another copy of the same nonterminal plus some extra material. If its probability of being used is not low, program will tend to generate very long sentences.

(2)
There is only one Adjective occurring in the grammar rule, Noun -> Adj Noun, and there is no rule that stipulate Adj -> Adj. Therefore, conjunction of multiple Adjs is impossible. Moreover, Since there are 5 Noun terminator, Noun -> Adj v.s. Noun terminator is 1:5, which make multiple adjectives rare.

(3) It has to reduce the weight of the aforementioned 2 rules and increse the weight of the Noun ->Adj to make the sentences
shorter and the adjectives more frequent.

(4) 1. For Det, a more natural weight ratio should be 'the':'a':'every' = 5:4:1
    2. For punctuation symbols, a period is more common than an exclamation or question mark. We change the ratio to 6:2:2.
    3. For the Prep 'under' is less common than the rest.
   
(5) 
a fine fine pickle kissed the pickled sandwich .

is it true that every perplexed floor kissed the floor ?

the pickled chief of staff kissed the perplexed pickled fine pickled pickle .

a delicious perplexed floor pickled the pickled president in a fine chief of staff .

the delicious fine pickled fine fine pickled pickled pickled president understood the sandwich .

the chief of staff on every fine floor with a floor in the sandwich under a delicious perplexed floor kissed a pickled pickled pickled perplexed delicious pickled delicious pickle !

a pickled pickle understood a floor !

a sandwich in the perplexed perplexed chief of staff understood a delicious fine floor .

every perplexed pickled perplexed pickle kissed a floor on every pickled chief of staff on a pickled floor !

a sandwich in the perplexed perplexed chief of staff understood a delicious fine floor .

2.3
(1) 
In grammar3, we extended the baseline grammar (grammar2) to cover the phenomena required in Section 2.2. The main modifications are:

Verb Subcategorization
 we introduced finer verb categories:
V_i (e.g., sighed, worked), which cannot take an NP, preventing ungrammatical forms like sighed a pickle.
V_t (e.g., ate, wanted), which take an NP object.
V_clausal (e.g., thought), which take a sentential complement (that S).
V_np_sbar (currently perplexed), which take both an NP and a sentential complement. This allows "it perplexed the president that a sandwich ate Sally" without overgenerating with other transitive verbs.

That-Clauses (S')
 we added S' → that S, allowing embedding of sentences as complements or as NP-like constituents. Wealso allowed NP → S', so a that-clause can act as subject (That a sandwich ate Sally perplexed the president).

Coordination
 we added subject coordination (S → NP Conj NP VP) and VP coordination (S → NP VP Conj VP, plus VP → VP Conj VP). Wealso allowed VP → Vt Conj Vt NP so multiple transitive verbs can share the same object (wanted and ate a sandwich).

Recursive NP Structure
Using an intermediate Nbar category, we enabled recursive adjective and PP modification of nouns (the very very perplexed president, every proposal on the desk).

AdjP Recursion and PP Attachments
 We added AdjP → Adv AdjP for stacked intensifiers, and rules like NP → NP PP and VP → V_intrans PP to allow PP attachment at both NP and VP levels (worked on every proposal on the desk).

Lexicon Extensions
 We added conjunctions (and), the pronoun it, name noun Sally, and the necessary nouns and adjectives to cover the example sentences.

In the meanwhile, we adjust the weights of some of the new rules that might create loops, such as VP -> V_clausal S' (S' -> that S) and Nbar -> AdjP Nbar.

(2)
a very fine pickle in Sally in a proposal and Sally worked .

it thought that Sally ate a sandwich on that Sally under it sighed !

is it true that Sally wanted it ?

is it true that a very very perplexed chief of staff with Sally in Sally and Sally worked ?

it thought that Sally worked .

is it true that it sighed ?

Sally sighed .

the very perplexed chief of staff on it sighed on it .

it worked on it .

a proposal sighed .

2.4 
(1) Neural hardware restores the grammar tree in another invisible way. It is trained (stimulated) on large text to capture the rule and grammer uderlying the sentences by years of accumulation. Memorization is conducted by the memory neuron unit in the human brain and is gradually formed.

(2)Maybe, as long as there is an unnatural language corpus, which is very unlikely because nobody will create such a corpus. Wethink the way that human children learning a language and the way that NN learns it are very alike. They all read the books to gain such experience, and if the children are emerged in such 'unnatural language', we think they will still learn some pattern to understand such language. 

(3) we think it is because every language has its own pattern, and the tree-structed sentence is very easy for achieve high-efficient expression and make everyone else understand it more easily. Moreover, it is easy to generate more or even unseen sentences. Yes, due to the efficiency that human requires for communication. This has to do with the evolution. 

(4) 
[1]It's good but with deawbacks. To some extent, grammar-based modeling is useful for generating legitimate sentences. However, it is too hard to construct the whole English linguistic system.
[2]Yes, and this represents that grammer-based modeling is not perfect. 
[3]The true semantics of a whole sentence, the context, and frequency of word being used.

3.1
(a) The other one is:
 (ROOT (S (NP (NP (Det every) 
                    (Noun sandwich)) 
              (PP (Prep with)
                  (NP (NP (Det a) 
                       (Noun pickle))
                       (PP (Prep on) 
                           (NP (Det the) 
                               (Noun floor)))))) 
              (VP (Verb wanted) 
                  (NP (Det a)
                  (Noun president)))) 
        .)
(b) Yes, because different derivations represent that there are more than one way to interpret the senetence, which will produce ambiguity. Different interpretations can lead to completely different semantics. 
3.3
(1) is missing
(2) 
sentence1: it and it worked in a chief of staff !
tree:
(ROOT (S (NP (Pron it))
         (Conj and)
         (NP (Pron it))
         (VP (V_i worked)
             (PP (Prep in)
                 (NP (Det a)
                     (Nbar (Noun chief
                                 of
                                 staff))))))
      !)
parser:
(ROOT (S (NP (Pron it))
         (Conj and)
         (NP (Pron it))
         (VP (V_i worked)
             (PP (Prep in)
                 (NP (Det a)
                     (Nbar (Noun chief
                                 of
                                 staff))))))
      !)
sentence2:
that a very very very perplexed chief of staff with it pickled Sally pickled it !
tree:
(ROOT (S (S' that
             (S (NP (Det a)
                    (Nbar (AdjP (Adv very)
                                (AdjP (Adv very)
                                      (AdjP (Adv very)
                                            (AdjP (Adj perplexed)))))
                          (Nbar (Nbar (Noun chief
                                            of
                                            staff))
                                (PP (Prep with)
                                    (NP (Pron it))))))
                (V_t pickled)
                (NP (Name Sally))))
         (V_t pickled)
         (NP (Pron it)))
      !)
parser:
(ROOT (S (S' that
             (S (NP (Det a)
                    (Nbar (AdjP (Adv very)
                                (AdjP (Adv very)
                                      (AdjP (Adv very)
                                            (AdjP (Adj perplexed)))))
                          (Nbar (Nbar (Noun chief
                                            of
                                            staff))
                                (PP (Prep with)
                                    (NP (Pron it))))))
                (V_t pickled)
                (NP (Name Sally))))
         (V_t pickled)
         (NP (Pron it)))
      !)

sentence3:
a sandwich perplexed a delicious proposal that the very delicious floor under Sally sighed .
tree:
(ROOT (S (NP (Det a)
             (Nbar (Noun sandwich)))
         (V_np_sbar perplexed)
         (NP (Det a)
             (Nbar (AdjP (Adj delicious))
                   (Nbar (Noun proposal))))
         (S' that
             (S (NP (Det the)
                    (Nbar (AdjP (Adv very)
                                (AdjP (Adj delicious)))
                          (Nbar (Nbar (Noun floor))
                                (PP (Prep under)
                                    (NP (Name Sally))))))
                (V_i sighed))))
      .)
parser:
(ROOT (S (NP (Det a)
             (Nbar (Noun sandwich)))
         (V_np_sbar perplexed)
         (NP (Det a)
             (Nbar (AdjP (Adj delicious))
                   (Nbar (Noun proposal))))
         (S' that
             (S (NP (Det the)
                    (Nbar (Nbar (AdjP (Adv very)
                                      (AdjP (Adj delicious)))
                                (Nbar (Noun floor)))
                          (PP (Prep under)
                              (NP (Name Sally)))))
                (V_i sighed))))
      .)
discussion:
The parser not always recover the original derivation. However, it is very accurate, there is only a mild difference when parsing the third sentence. The parser didn't parse this sentence is very likely that this sentence is not deterministic, which means that there are more than one ways to derive the original sentence. 

(3)
Basic mode is:
   Det:Every -> Noun:sandwich -> Prep:with -> Det:a ->Noun:pickle -> Prep:on -> Det:the -> Noun:floor -> Prep:under -> Det:the -> Noun:chief of staff
My possible derivation:
    1.
    (NP (NP (NP (Det every)
                (Noun sandwich))
            (PP (Prep with)
                (NP (Det a)
                    (Noun pickle))
        (PP (Prep on)
            (NP (Det the)
                (Noun) floor))
            (PP (Prep under)
                (NP (Det the)
                    (Noun chief
                        of
                        staff))))))
    'with a pickle' is describing 'every sandwch', and this 'sandwich' is 'on th floor', where is 'under the chief of staff'.
    2.
    (NP (NP (NP (Det every)
                (Noun sandwich))
            (PP (Prep with)
                (NP (Det a)
                    (Noun pickle))
                (PP (Prep on)
                    (NP (Det the)
                        (Noun) floor))
        (PP (Prep under)
            (NP (Det the)
                (Noun chief
                    of
                    staff))))))
    'every sandwich' and 'a pickle', which is 'on the floor', are 'under the chief of staff'.
    3.
    (NP (NP (Det every)
            (Noun sandwich))
        (PP (Prep with)
            (NP (Det a)
                (Noun pickle))
            (PP (Prep on)
                (NP (Det the)
                    (Noun) floor))
                (PP (Prep under)
                    (NP (Det the)
                        (Noun chief
                                of
                                staff)))))
    'every sandwich' and 'a pickle' are 'on the floor', and the 'floor' is 'under the chief of staff'
    4.
    (NP (NP (Det every)
            (Noun sandwich))
        (PP (Prep with)
            (NP (NP (Det a)
                    (Noun pickle)))
                (PP (Prep on)
                    (NP (Det the)
                        (Noun) floor))
            (PP (Prep under)
                (NP (Det the)
                    (Noun chief
                        of
                        staff))))) 
    'every sandwich' <- 'with a pickle' <- 'on the floor', is 'under the chief of staff'.
    5.
    (NP (NP (NP (NP (Det every)
                    (Noun sandwich)))
                (PP (Prep with)
                    (NP (Det a)
                        (Noun pickle)))
            (PP (Prep on)
                (NP (Det the)
                    (Noun) floor))
        (PP (Prep under)
            (NP (Det the)
                (Noun chief
                    of
                    staff)))))
    'every sandwich' is 'with a pickle', 'on the floor', and 'under the chief'.

(4).
grammar.gr:
every fine floor understood a sandwich .
 (ROOT (S (NP (Det every) (Noun (Adj fine) (Noun floor))) (VP (Verb understood) (NP (Det a) (Noun sandwich)))) .)
# number of parses = 1
every perplexed floor kissed a chief of staff under the perplexed floor !
 (ROOT (S (NP (Det every) (Noun (Adj perplexed) (Noun floor))) (VP (Verb kissed) (NP (NP (Det a) (Noun chief of staff)) (PP (Prep under) (NP (Det the) (Noun (Adj perplexed) (Noun floor))))))) !)
# number of parses = 1
every chief of staff with the floor with the chief of staff under every floor under the pickled president in a sandwich kissed the sandwich on a sandwich with the chief of staff on the president with a perplexed chief of staff on a perplexed president with a sandwich !
 (ROOT (S (NP (NP (Det every) (Noun chief of staff)) (PP (Prep with) (NP (NP (Det the) (Noun floor)) (PP (Prep with) (NP (NP (NP (NP (Det the) (Noun chief of staff)) (PP (Prep under) (NP (Det every) (Noun floor)))) (PP (Prep under) (NP (Det the) (Noun (Adj pickled) (Noun president))))) (PP (Prep in) (NP (Det a) (Noun sandwich)))))))) (VP (Verb kissed) (NP (NP (Det the) (Noun sandwich)) (PP (Prep on) (NP (NP (Det a) (Noun sandwich)) (PP (Prep with) (NP (NP (Det the) (Noun chief of staff)) (PP (Prep on) (NP (NP (NP (Det the) (Noun president)) (PP (Prep with) (NP (NP (Det a) (Noun (Adj perplexed) (Noun chief of staff))) (PP (Prep on) (NP (Det a) (Noun (Adj perplexed) (Noun president))))))) (PP (Prep with) (NP (Det a) (Noun sandwich)))))))))))) !)
# number of parses = 5544
a pickle under the pickled chief of staff in the pickle with the sandwich in a sandwich in the president in every sandwich in the floor in the pickle on the floor with the pickled president on every perplexed delicious president pickled every president in every president in the fine pickle !
 (ROOT (S (NP (NP (Det a) (Noun pickle)) (PP (Prep under) (NP (NP (NP (Det the) (Noun (Adj pickled) (Noun chief of staff))) (PP (Prep in) (NP (Det the) (Noun pickle)))) (PP (Prep with) (NP (NP (Det the) (Noun sandwich)) (PP (Prep in) (NP (NP (Det a) (Noun sandwich)) (PP (Prep in) (NP (NP (Det the) (Noun president)) (PP (Prep in) (NP (NP (Det every) (Noun sandwich)) (PP (Prep in) (NP (NP (Det the) (Noun floor)) (PP (Prep in) (NP (NP (NP (NP (Det the) (Noun pickle)) (PP (Prep on) (NP (Det the) (Noun floor)))) (PP (Prep with) (NP (Det the) (Noun (Adj pickled) (Noun president))))) (PP (Prep on) (NP (Det every) (Noun (Adj perplexed) (Noun (Adj delicious) (Noun president)))))))))))))))))))) (VP (Verb pickled) (NP (NP (NP (Det every) (Noun president)) (PP (Prep in) (NP (Det every) (Noun president)))) (PP (Prep in) (NP (Det the) (Noun (Adj fine) (Noun pickle))))))) !)
# number of parses = 117572

grammar3.gr:
Sally perplexed a proposal that that it understood the sandwich pickled it .
 (ROOT (S (NP (Name Sally)) (V_np_sbar perplexed) (NP (Det a) (Nbar (Noun proposal))) (S' that (S (S' that (S (NP (Pron it)) (V_t understood) (NP (Det the) (Nbar (Noun sandwich))))) (V_t pickled) (NP (Pron it))))) .)
# number of parses = 6
every very fine chief of staff with it perplexed a sandwich on Sally that Sally and a pickled floor wanted Sally .
 (ROOT (S (NP (Det every) (Nbar (AdjP (Adv very) (AdjP (Adj fine))) (Nbar (Nbar (Noun chief of staff)) (PP (Prep with) (NP (Pron it)))))) (V_np_sbar perplexed) (NP (Det a) (Nbar (Nbar (Noun sandwich)) (PP (Prep on) (NP (Name Sally))))) (S' that (S (NP (Name Sally)) (Conj and) (NP (Det a) (Nbar (AdjP (Adj pickled)) (Nbar (Noun floor)))) (VP (V_t wanted) (NP (Name Sally)))))) .)
# number of parses = 18

is it true that that it and it worked sighed ?
 (ROOT is it true that (S (NP (S' that (S (NP (Pron it)) (Conj and) (NP (Pron it)) (VP (V_i worked))))) (V_i sighed)) ?)
# number of parses = 6
It seems that the number parser gets larger when the generated sentence becomes longer. More precisely, since grammar.gr doesn't control the sentence length by reducing the weight of NP->NP PP (PP -> Prep NP), the loops are very likey to exist in the sentence, which induce many possible derivations. Compared to grammar1.gr, grammar3.gr controls the weight of rules that easily cause loop, sentences generated are tend to be shorter and thus have controled deviration number. However, due to the existence of clause and adjective phrase, the derivation number cannot be very low.

(5)
(a)
~Because a sentence is constructed by multiple rules and vocabulary, each of which is attached with a probability. When the number of rules and vocabulary are large, those probabilities after being multiplied could be very small.   
 ROOT	S . (1/3) * S   NP VP (1) * NP Det Noun (1/2) * the * (1/3) * president * (1/6) * VP	Verb NP (1) * ate (1/5) * the (1/3) * sandwich (1/6) = 1/19440 ~ 5.144e-5.
~Because theree is only one parse of rules and vocabulary that can form this sentence. This makes p(sentence) = p(best parse).
~This is a conditional probability that asks what's probability of the event best_parse happening given that randsent.py produce the sentence. It should be P (best_prse union sentence) / P (sentence). Since there is only one possible parsing of the sentence, the two probabilities should be equal, which results in 1.

(b) This represents that there are two ways of parsing this sentence, and thus the p(best_parse | sentence) is 1:2 = 0.5.

(c) -43.844 = log_2(p(sentence)= 5.144e-05 * p(sentence)= 1.240e-09) = log_2(5.144e-05) + log_2(1.240e-09) = -14.246 - 29.587 = 43.833. The log-prob is the odds that the 2 sentence are generated in this sequence after logarithm. And deviding by the total token number 18. The cross-entropy requires the difference to be positive, therefore another minus is in the front.  

(d) The perplexity is taking the exponential of cross-entropy, which is 2^(ce) = 5.4076

(e) Because 'the president ate .' ends with Vt, and this is not allowed from grammer.gr. The probability of producing this is 0, and log(0) is infinite. Therefore, it cannot be compressed well.

(6)
(a) Powershell command use: 1. python randsent.py -g .\grammar2.gr -n 1000 --seed 0 > .\corpus.txt; 
                            2. Get-Content .\corpus.txt | perl .\parse -g .\grammar2.gr -P | perl .\prettyprint
The entropy of grammar2 is 2.211 bits per word (30104.365 / 13614)
(b) The entropy of grammar3 is 2.631 bits per word (61378.589 / 23328). Grammar 3 has higher entropy than grammar 2. This is natural because grammar3 introduces more structures, and these expansions enable Grammar3 to generate a greater variety of sentence patterns. The probability mass is distributed over more possible outputs. This means that Grammar3 can cover a larger sentence space, and thus the average uncertainty of each word is higher, so the entropy value is naturally higher than that of Grammar2.
(c) For the original grammar.gr, the entropy is infinite. This is because the grammar allows unbounded recursion (e.g., NP → NP PP), so the generator often produces truncated sentences containing ... once the maximum expansion limit is reached. Since "..." is not part of the grammar, such sentences are assigned probability 0, yielding log-prob = −infinite and thus cross-entropy = infinite.

(7)
When the corpus is generated from grammar2, grammar2 assigns the highest probability to these sentences, because its rule set is more restrictive and exactly matches the distribution that produced the corpus. Thus its entropy (2.211 bits/word) is the lowest.
By contrast, grammar3 includes all the sentences grammar2 can produce, plus many additional possibilities due to coordination, recursion, and sentential complements. Since there are more rules per nonterminal, the probability mass is spread over a larger set of derivations, so each individual sentence receives lower probability. As a result, the cross-entropy of grammar3 on grammar2’s corpus is higher than grammar2’s entropy.
For the original grammar, the probability of producing shorter sentences (typical of grammar2’s corpus) is lower, since grammar tends to favor longer recursive expansions. Consequently, sentences from grammar2’s corpus are less probable under grammar, leading again to a higher cross-entropy value.

4.1
We have implemented (c) and (g) phenomena in grammar4.gr based on grammar3.gr. 
(c) Relative Clauses
To support relative clauses, I extended the grammar so that any noun phrase can be followed by a relative clause (NP → NP RelClause). I distinguished between two kinds of relative markers:
RelPron (e.g., who, which), which behave as both connectors and syntactic constituents inside the clause (they can serve as subject or object).
Comp (e.g., that), which only acts as a complementizer and does not itself fill a grammatical role.
The rule RelClause -> RelPron S_rel | Comp S_rel allows both forms.
To capture the phenomenon of gaps, I introduced a special sub-clause category S_rel. This has two variants:
S_rel -> VP handles cases where the subject is missing (the man who __ ate the sandwich).
S_rel -> NP VP_gap handles cases where the object is missing (the sandwich that the president ate __).
Here VP_gap -> Vt ensures that a transitive verb can appear without its object only in this special environment.
Finally, to allow recursive embedding like "the sandwich that the president thought that Sally ate", I added a sentential-complement rule VP_relcomp -> Vc Comp S_rel. This restricts embedding to verbs that normally take clausal complements (thought, believed, said).
Together these changes let the grammar generate both subject-gap and object-gap relative clauses, with correct control over where gaps can occur.
(g) Appositives
To implement appositives, I added a rule allowing an NP to be expanded with a comma-delimited appositive phrase:
NP -> NP , Appos ,
The nonterminal Appos can expand in several ways:
As another noun phrase (the president, the fine chief of staff,).
As a relative clause, enabling non-restrictive relative clauses (Sally, who ate a sandwich,).
As a fixed phrase such as an age expression (Sally, 59 years old,).
This design ensures that appositives are treated as optional modifiers embedded inside noun phrases, marked explicitly with commas. Because the rule is recursive, multiple appositives can be stacked if desired.

Extra credit:
In this part, we implemented the passive grammar. There are two main type of this grammar. For example, (1) `the pickle is eaten by the president .` and (2) `the sandwich eaten by Sally kissed the president .`. The first one is the most common passive structure with NP + Auxiliary verb + Ver, Past Participle (VBN) + NP. And the second passive structure that 'eaten by ...' is a reduced relative clasuse to describe the NP in front of it. 

For the first one, we define the VBN as V_pt ('done by') since those passive verb are transitive, and we also define auxiliary verb Auxpass to construct 'be done by'. V_pt is added with the rule '(NP) VP Auxpass V_pt (NP)'. The second one is harder since it cannot be regarded as a Verb-based component. Therefore, we add this structure to the relative clause we defined previously. 
We added 'RelClause   V_tp NP', which combined with 'NP VP' and 'NP NP RelClause' can form (2)  (ROOT (S (NP (NP (Det the) (Nbar (Noun sandwich))) (RelClause (V_tp eaten by) (NP (Name Sally)))) (V_t kissed) (NP (Det the) (Nbar (Noun president)))) .)

Moreover, we can combine these two structure into (3) `the pickle kissed by the sandwich is eaten by the president .`, which is  (ROOT (S (NP (NP (Det the) (Nbar (Noun pickle))) (RelClause (V_tp kissed by) (NP (Det the) (Nbar (Noun sandwich))))) (VP (Auxpass is) (V_tp eaten by) (NP (Det the) (Nbar (Noun president))))) .)