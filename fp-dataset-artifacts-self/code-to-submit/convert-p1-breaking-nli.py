
import json
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
From https://github.com/BIU-NLP/Breaking_NLI
sentence1: The premise sentence.

sentence2: The hypothesis sentence, which is the same as the premise except for one word/phrase that was replaced.

annotator_labels: These are all of the individual labels from the three annotators. 

gold_label: This is the label chosen by the majority of annotators. 

pairID: A unique identifier for each sentence1--sentence2 pair.

category: This category sematically groups the replaced words.
'''
f_out = open("breakNLIdata.jsonl", "w")

with open('./Breaking_NLI-master/data/dataset.jsonl') as jsonFile:
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
		del lineDict['category']
		del lineDict['annotator_labels']
		del lineDict['pairID']
		lineDict['premise'] = lineDict.pop('sentence1')
		lineDict['hypothesis'] = lineDict.pop('sentence2')
		lineDict['label'] = label
		#print(json.dumps(lineDict))
		f_out.write(str(json.dumps(lineDict)) + "\n")

f_out.close()

