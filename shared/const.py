import json

from tqdm import tqdm

task_ner_labels = {
    'ace04': ['FAC', 'WEA', 'LOC', 'VEH', 'GPE', 'ORG', 'PER'],
    'ace05': ['FAC', 'WEA', 'LOC', 'VEH', 'GPE', 'ORG', 'PER'],
    'scierc': ['Method', 'OtherScientificTerm', 'Task', 'Generic', 'Material', 'Metric'],
}

task_rel_labels = {
    'ace04': ['PER-SOC', 'OTHER-AFF', 'ART', 'GPE-AFF', 'EMP-ORG', 'PHYS'],
    'ace05': ['ART', 'ORG-AFF', 'GEN-AFF', 'PHYS', 'PER-SOC', 'PART-WHOLE'],
    'scierc': ['PART-OF', 'USED-FOR', 'FEATURE-OF', 'CONJUNCTION', 'EVALUATE-FOR', 'HYPONYM-OF', 'COMPARE'],
}

assert task_ner_labels.keys() == task_rel_labels.keys()

tasks = set(task_ner_labels.keys()).add("custom")

def get_ner_labels(args):
    labels = set()

    for split_file in [args.train_data, args.dev_data, args.test_data]:
        with open(split_file, "r") as f:
            data = json.load(f)
        
        for item in tqdm(data):
            sample_labels = {e["type"] for e in item["entities"]}
            labels = labels.union(sample_labels)
    
    labels = list(labels)

    return labels

def get_labelmap(label_list):
    label2id = {}
    id2label = {}
    for i, label in enumerate(label_list):
        label2id[label] = i + 1
        id2label[i + 1] = label
    return label2id, id2label
