## ArcFormer

# Hobby project to solve the ARC benchmark
build a set of rules
generate a huge dataset of examples from the rules
train a big transformer on just this

two major issues:
it has to get pixel perfect
it has to generalize to unseen rules

initial assumption:
pretraining on non-aligned data will help 'prime' the model
non-aligned = it doesn't just see complete examples
input data can start anywhere in an example, so it may not even be possible to get the rule...
but it will learn the 'language' the grids, example sets, etc.


TODO:

1. try a new data plan that makes every sample contain exactly one example, start at the beginning and get the whole thing, pad the rest
    - will be wasteful, there will be a punch of pad
    - but thats ok, it will be getting exactly the rule, exactly the task from the very beginning
    - still a role for tokenization. imagine a 20x20 array. so thats 400 per grid, x 8 grids, 3200 pixels min.
    - need to figure out the encoding at a per "document" level
    - the biggest issue is actually the data diversity, now instead of sampling random pixels, I only have N training points where N is the number of examples. so say 100 rules, to get a million points (very low!), need 10,000 examples per rule...
    - to get 500 Million with 1000 rules, need 500,000 examples per rule... crazy. but that might be what it takes. I really think the document based approach is better
2. build a model.generate scorer to use during training, check for exact token matches







MORE rules!

train longer with a bigger model prove I can overfit
- trained for a while (arcformer_dev_03_10_2024_08:40:52), never overfit, got down to ~1 loss

training must haves:
- save and load
- figure out speed on big gpu (update pytorch, update cuda, pin dataloader better, could it just be SSD?)
- figure out why I got an OOM error on big gpu for something fit on the little windows gpu...
- add in a test set, completely different rules - need to show overfitting before I believe I'm making progress. It could still just be learning the basics (grids, copy the input, whatever - but even that would be really good!)
- load a checkpoint and actually check inference


explore tokenization - how effecient it is as I add more rules with different pixel distributions?
build the inference tools - process a given example, feed through, de-process (check for valid grid structure)
set up fine tuning data + train loop (specific examples with just the example pairs, then the missing output on the last one)
