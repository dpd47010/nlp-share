
import json
import random
'''
Instructions from run.py
# You need to format the dataset appropriately. For SNLI, you can prepare a file with each line containing one
# example as follows:
# {"premise": "Two women are embracing.", "hypothesis": "The sisters are hugging.", "label": 1}
# contra = 2
# net = 1
# entail = 0
'''

'''
from snli readme
== Fields ==

sentence1: The premise caption that was supplied to the author of the pair.

sentence2: The hypothesis caption that was written by the author of the pair.

sentence{1,2}_parse: The parse produced by the Stanford Parser (3.5.2, case insensitive PCFG, trained on the standard training set augmented with the parsed Brown Corpus) in Penn Treebank format.

sentence{1,2}_binary_parse: The same parse as in sentence{1,2}_parse, but formatted for use in tree-structured neural networks with no unary nodes and no labels.

annotator_labels (label1-5 in the tab separated file): These are all of the individual labels from annotators in phases 1 and 2. The first label comes from the phase 1 author, and is the only label for examples that did not undergo phase 2 annotation. In a few cases, the one of the phase 2 labels may be blank, indicating that an annotator saw the example but could not annotate it.

gold_label: This is the label chosen by the majority of annotators. Where no majority exists, this is '-', and the pair should not be included when evaluating hard classification accuracy.

captionID: A unique identifier for each sentence1 from the original Flickr30k example.

pairID: A unique identifier for each sentence1--sentence2 pair.

NOTE: captionID and pairID contain information that can be useful in making classification decisions and should not be included in model input (nor, of course, should either annotator_labels or gold_label).
'''

# get 60% of mccoy (even distribution overall attack types) in train set
def parseMccoyToJsonl(fstr, foutstr, foutdevstr):
    ftrainout = open(foutstr, 'w')
    fdevout = open(foutdevstr, 'w')
    with open(fstr) as jsonFile:
        jsonList = list(jsonFile)


        # 30k total samples. 10k of each category, 1k of each subcategory, all linear
        linecount = 0
        devlimit = 1000
        trainlimit = 600

        for line in jsonList:
            lineDict = json.loads(line)
            #pnew = lineDict["premise"].replace(" .", ".")
            #hnew = lineDict["hypothesis"].replace(" .", ".")
            #lineDict["premise"] = pnew
            #lineDict["hypothesis"] = hnew
            if (linecount < trainlimit):
                ftrainout.write(str(line))
            else:
                fdevout.write(str(line))
        
            linecount += 1
            if (linecount >= devlimit):
                linecount = 0
            
    ftrainout.close()
    fdevout.close()



# get snli input to standard jsonl form
def convertToJsonl(fstr, foutstr):
    fout = open(foutstr, 'w')
    with open(fstr) as jsonFile:
        jsonList = list(jsonFile)
        for line in jsonList:
            lineDict = json.loads(line)
            tempLabel = lineDict['gold_label']
            if (tempLabel == 'entailment'):
                label = 0
            elif (tempLabel == "neutral"):
                label = 1
            elif (tempLabel == 'contradiction'):
                label = 2
            del lineDict['gold_label']
            del lineDict['captionID']
            del lineDict['sentence1_parse']
            del lineDict['sentence2_parse']
            del lineDict['sentence1_binary_parse']
            del lineDict['sentence2_binary_parse']
            del lineDict['annotator_labels']
            del lineDict['pairID']
            lineDict['premise'] = lineDict.pop('sentence1')
            lineDict['hypothesis'] = lineDict.pop('sentence2')
            lineDict['label'] = label
            #print(json.dumps(lineDict))
            fout.write(str(json.dumps(lineDict)) + "\n")
    fout.close()

# create shuffle of combined input
def shuffleCombined(fstr, foutstr):
    fout = open(foutstr, 'w')
    with open(fstr) as jsonFile:
        jsonList = list(jsonFile)
        random.shuffle(jsonList)
        for line in jsonList:
            lineDict = json.loads(line)
            fout.write(str(json.dumps(lineDict)) + "\n")
    fout.close()


fsnliin = './snli_1.0/snli_1.0_train.jsonl'
fsnliout = './jsonl/snli_only_train.jsonl'

fmccoyin = './mccoyData.jsonl'
fmccoyout = './jsonl/mccoy_parsed_only_train.jsonl'
fmccoydev = './jsonl/mccoy_parsed_only_dev.jsonl'

fshufflein = './jsonl/snli-mccoy-combined-noshuffletrain.jsonl'
fshuffleout= './jsonl/snli-mccoy-combined-train-shuffle.jsonl'

#convertToJsonl(fsnliin, fsnliout)
#parseMccoyToJsonl(fmccoyin, fmccoyout, fmccoydev)
shuffleCombined(fshufflein, fshuffleout)