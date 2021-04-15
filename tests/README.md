# Settings for random generated tests
* `EPOCHS`: can be used to turn off completely (set to 0) the random generated tests or to increase their number
* `FUNC_RUNS`: define how many test cases will run on each epoch\
**WARNNING/ATTENTION: TESTS CAN TAKE A LOT OF TIME TO FINISH DEPENDING ON YOUR COMPUTER SPECS**
# File Structure
|File |Content|
|----|:-------|
|test_codon.py|Contains tests for codons function(s), tests also functions that are related to RNA. (Contains random generated tests)|
|test_levenshtein.py|Contains tests for levenshtein functions. (Contains random generated tests)|
|test_needleman.py|Contains tests for needleman functions. (Contains random generated tests)|
|test_stats.py|Contains tests for statistics functions. (Contains random generated tests)|
|test_utility.py|Contains tests for utility functions declared in `src/utility.py`.|