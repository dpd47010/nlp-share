
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
From https://github.com/tommccoy1/hans
gold_label: The correct label for this sentence pair (either entailment or non-entailment)
sentence1_binary_parse: A binary parse of the premise, generated using a template based on the Stanford PCFG; this is necessary as input for some tree-based models.
sentence2_binary_parse: A binary parse of the hypothesis, generated using a template based on the Stanford PCFG; this is necessary as input for some tree-based models.
sentence1_parse: A parse of the premise, generated using a template based on the Stanford PCFG
sentence2_parse: A parse of the hypothesis, generated using a template based on the Stanford PCFG
sentence1: The premise
sentence2: The hypothesis
pairID: A unique identifier for this sentence pair
heuristic: The heuristic that this example is targeting (lexical_overlap, subsequence, or constituent)
subcase: The subcase of the heuristic that is being targeted; each heuristic has 10 subcases, described in the appendix to the paper
template: The specific template that was used to generate this pair (most of the subcases have multiple templates; e.g., for subcases depending on relative clauses, there might be one template for relative clauses modifying the subject, and another for relative clauses modifying the direct object). This template ID corresponds to the ID in templates.py.

no neutral!
assuming
entail = 0, not = 2
'''
f_out = open("mccoyData.jsonl", "w")

with open('./hans-master/heuristics_evaluation_set.jsonl') as jsonFile:
	jsonList = list(jsonFile)
	for line in jsonList:
		lineDict = json.loads(line)

		tempLabel = lineDict['gold_label']
		if (tempLabel == 'entailment'):
			label = 0
		elif (tempLabel == "non-entailment"):
			label = 2
		del lineDict['gold_label']
		del lineDict['heuristic']
		del lineDict['template']
		del lineDict['subcase']
		del lineDict['sentence2_parse']
		del lineDict['sentence2_binary_parse']
		del lineDict['sentence1_binary_parse']
		del lineDict['sentence1_parse']
		del lineDict['pairID']


		lineDict['premise'] = lineDict.pop('sentence1')
		lineDict['hypothesis'] = lineDict.pop('sentence2')
		lineDict['label'] = label

		#print (json.dumps(lineDict))
		f_out.write(str(json.dumps(lineDict)) + "\n")

f_out.close()

