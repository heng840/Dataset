# Multilingual Paraphrased Query Dataset

This repository contains a multilingual version of the ParaRel dataset, featuring paraphrased queries for each language. The dataset is designed to facilitate research on fact-based knowledge mechanisms across multiple languages.

## Introduction

Our dataset is an extension of the following two datasets:
1. [ParaRel](https://github.com/yanaiela/pararel)
2. [mLAMA](https://github.com/norakassner/mlama)

mLAMA is an extended version of LAMA that includes a multilingual expansion of ParaRel. However, during the expansion process, each fact in mLAMA was associated with only one query. In contrast, ParaRel's original design associates each fact with multiple queries expressed in different ways (rephrased queries).

The paper ["Knowledge Localization: Mission Not Accomplished? Enter Query Localization!"](https://arxiv.org/abs/2405.14117) discusses the query localization hypothesis and concludes that studying different rephrased queries is necessary for researching facts. To facilitate the study of fact-based knowledge mechanisms across multiple languages, we present our dataset.

## Languages

Currently, our dataset covers 6 languages belonging to 3 language families:

- Indo-European:
  - English (en)
  - French (fr)
- Uralic:
  - Finnish (fi)
  - Hungarian (hu)
- Altaic:
  - Japanese (ja)
  - Korean (ko)

## Dataset Structure

The dataset is organized as follows:

```
.
└── Aligned_my_MLAMA/
    ├── en/
    │   ├── P19.jsonl
    │   ├── ...
    │   └── templates.jsonl
    ├── fr/
    │   ├── P19.jsonl
    │   ├── ...
    │   └── templates.jsonl
    ├── fi/
    │   ├── P19.jsonl
    │   ├── ...
    │   └── templates.jsonl
    ├── hu/
    │   ├── P19.jsonl
    │   ├── ...
    │   └── templates.jsonl
    ├── ja/
    │   ├── P19.jsonl
    │   ├── ...
    │   └── templates.jsonl
    └── ko/
        ├── P19.jsonl
        ├── ...
        └── templates.jsonl
```

Each language directory contains JSONL files for various relations (e.g., P19.jsonl) and a `templates.jsonl` file that holds the rephrased query templates for each relation.

## Data Examples

Here are a few examples of the rephrased queries in different languages:

English (en):
```json
{"relation": "P19", "pattern": "[X] was born in [Y]."}
{"relation": "P19", "pattern": "[X] is originally from [Y]."}
{"relation": "P19", "pattern": "[X] was originally from [Y]."}
```

French (fr):
```json
{"relation": "P19", "pattern": "[X] est né en [Y]."}
{"relation": "P19", "pattern": "[X] est originaire de [Y]."}
{"relation": "P19", "pattern": "[X] était originaire de [Y]."}
```

Finnish (fi):
```json
{"relation": "P19", "pattern": "[X] syntyi [Y]."}
{"relation": "P19", "pattern": "[X] on kotoisin [Y]."}
{"relation": "P19", "pattern": "[X] oli kotoisin [Y]."}
```

For more examples, please refer to the respective language directories in the `Aligned_my_MLAMA` folder.

## Dataset Construction

To understand the process of constructing our dataset, please refer to the `prepare` folder in this repository.

## Applications

This multilingual paraphrased query dataset can be used for various applications, such as:
- Cross-lingual fact-based knowledge probing
- Evaluating the robustness of language models across different query formulations
- Studying the impact of query localization on knowledge localization

We hope that this dataset will contribute to the advancement of research in multilingual natural language processing and knowledge representation.

## License

This dataset is licensed under the [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/).

## Contact

If you have any questions or suggestions regarding this dataset, please feel free to open an issue or contact the repository maintainers.
