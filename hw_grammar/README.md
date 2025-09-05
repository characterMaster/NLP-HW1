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

2.2
(1) 