# Definition-Guided Zero-Shot Classification of Student Sentiment on College Mental Health Support Using Gemini 2.5 Flash: A Comparative Study with the SMILE-College Benchmark

## Abstract
This study reproduces and extends the work of Sood et al. (2024), who introduced the SMILE-College dataset for analyzing student sentiment on mental health support in U.S. colleges using large language models (LLMs). We evaluate the performance of Google’s Gemini 2.5 Flash, a free and efficiency-optimized lightweight version of the Gemini 2.5 family, on a subset of 334 annotated student responses using the fine-grained sentiment classification prompt from the original study. The model’s results are compared to GPT-3.5 and BERT baselines from the SMILE-College paper. Gemini 2.5 Flash achieved an overall accuracy of 0.762 and a weighted F1-score of 0.761, performing comparably to GPT-3.5 (F1 = 0.80) and outperforming smaller open-source models like Llama 2 and Mistral. Class-wise analysis revealed strong performance on Dissatisfied and Satisfied categories, moderate performance on Mixed, and weaker detection of Neutral responses. Confusion matrix patterns closely mirrored those reported in the original paper. This study demonstrates that efficient, freely available LLMs can effectively approximate premium model performance when guided by robust, fine-grained prompting strategies. This highlights how free LLMs could be a good alternative in facilitating mental health management.

---

## Introduction

Student mental health has emerged as a critical dimension of higher education quality and student success. Universities increasingly invest in mental health services, yet assessing their effectiveness remains challenging due to limited data and reliance on qualitative feedback. Sood et al. (2024) addressed this gap by developing SMILE-College, the first sentiment analysis dataset capturing student perspectives on college mental health support through a combination of human and machine annotations.

Their research demonstrated the power of Large Language Models (LLMs) such as GPT-3.5 and BERT for nuanced sentiment classification, outperforming traditional models like Logistic Regression (LR) and Support Vector Machines (SVM).

This paper presents a replication and comparative study using Gemini 2.5 Flash, a free LLM optimized for fast, low-cost inference. We aimed to test whether the fine-grained prompting strategy proposed in the SMILE-College paper generalizes across LLM architectures and cost tiers.

## Related Work

The SMILE-College dataset was derived from the Student Voice Survey (SVS) by College Pulse (2022), consisting of 793 valid responses categorized into four sentiment classes: Satisfied, Dissatisfied, Mixed, and Neutral. Sood et al. used a human-machine collaborative annotation process, leveraging GPT-3.5 and manual validation to produce reliable sentiment labels. Their study showed that GPT-3.5 achieved an F1-score of 0.80, outperforming BERT (0.78) and other open-source LLMs (0.57–0.65).


## Methodology

### A. Dataset

This replication study used 334 records sampled from the public SMILE-College dataset. Each record includes a student’s narrative response regarding their college’s mental health and wellness services, along with a human-validated sentiment label.

### B. Sentiment Categories
Following the original study, responses were classified into four categories:

**Satisfied**: Primarily positive expressions of approval.

**Dissatisfied**: Negative or critical feedback about services.

**Mixed**: tentatively balanced combination of satisfaction and criticism.

**Neutral**:  no clear emphasis on satisfaction, dissatisfaction, or criticism

### C. Prompting Strategy

The fine-grained prompting template from Sood et al. was adopted without modification. The prompt defines explicit task roles, sentiment definitions, and constrained output formatting:

```
You are an experienced sentiment analyst studying students’ feedback on mental health services.       
Categorize the following response into one of these four labels: Satisfied, Dissatisfied, Mixed, Neutral.

The specific criteria for each category are as follows. 
(1) “Satisfied”: at least 75% of the language expressed satisfaction, with minimal suggestions for improvement. 
(2) “Dissatisfied”: at least 75% of the language indicated discontent or suggestions for enhancement, with little mention of satisfaction. 
(3) “Mixed”: expressions of satisfaction and dissatisfaction/suggestions were approximately evenly split, with each constituting about 50%. 
(4) “Neutral”: no clear emphasis on satisfaction, dissatisfaction, or suggestions for improvement

Question: “What mental health or wellness services and supports provided by your college are working well? What aspects need more attention?”
Response: "we get free therapy, but the therapists are known to be really bad and overwhelmed and unavailable."

Output: 

```

Gemini 2.5 Flash was run in zero-shot mode, producing one of 4 categories as output.

### D. Experimental Setup

- Model: Google Gemini 2.5 Flash (Free version)

- Sample size: 334 responses

- Evaluation metrics: Precision, Recall, F1-score, and Accuracy

- Confusion matrices: Raw and normalized for interpretability

- Ground truth: Human-verified labels from the SMILE-College dataset

---

## Results
### A. Model Outputs

Two of the outputs contain reasoning excerpts:

**Output1**:
  ```
    "the student's response can be broken down as follows:

    1.  **positive/satisfied:** ""we had two days for drop-in counseling... this helped me learn about some resources for myself."" this is a clear expression of satisfaction with a specific service.
    2.  **dissatisfaction/suggestions for improvement:** ""i have heard from other students that there can be long wait times to meet with counselors and they're more a short-term solution (e.g., referring students to other therapists)."" these are specific criticisms and suggestions for enhancement, even if based on others' experiences.
    3.  **neutral/positive outlook:** ""there is a new telehealth counseling service which i don't know much about but it seems to address these problems."" while not direct satisfaction with a currently working service, this statement acknowledges a new service that is perceived as a positive step to address the previously mentioned issues. it balances the prior negative feedback.

    when weighing these points:
    *   there's a clear positive statement about drop-in counseling.
    *   there are two distinct negative points/suggestions for improvement (wait times, short-term solutions).
    *   there's a forward-looking, slightly positive statement about a new service that *seems* to address the problems, acting as a counterweight to the negative points.

    considering the positive personal experience, the identified areas for improvement, and the acknowledgement of a potential solution, the overall sentiment is a mix of satisfaction and dissatisfaction/suggestions that are approximately evenly split. the positive outlook on the telehealth service prevents it from being predominantly dissatisfied.

    therefore, the most appropriate category is mixed.

    **output:** mixed"
  ```
  
**Output2**:
```
"the student's response indicates they do not currently use the services due to a lack of awareness (""maybe if i heard more about it i would""). this directly addresses the ""what aspects need more attention?"" part of the question by identifying a need for better communication or promotion of services. this constitutes a suggestion for enhancement regarding the college's outreach efforts, implicitly expressing a form of dissatisfaction with the current level of awareness. since the entire response points to an area needing improvement and shows no satisfaction, it falls under the ""dissatisfied"" category.

**dissatisfied**"
```

### B. Quantitative Evaluation

#### Confusion Matrix (Counts):
| True \ Pred  | Dissatisfied | Neutral | Satisfied | Mixed |
| ------------ | ------------ | ------- | --------- | ----- |
| Dissatisfied | 124          | 5       | 2         | 22    |
| Neutral      | 8            | 19      | 3         | 4     |
| Satisfied    | 5            | 4       | 35        | 5     |
| Mixed        | 16           | 2       | 3         | 75    |

#### Confusion Matrix (Normalized %):
| True \ Pred  | Dissatisfied | Neutral | Satisfied | Mixed |
| ------------ | ------------ | ------- | --------- | ----- |
| Dissatisfied | 81.0         | 3.3     | 1.3       | 14.4  |
| Neutral      | 23.5         | 55.9    | 8.8       | 11.8  |
| Satisfied    | 10.2         | 8.2     | 71.4      | 10.2  |
| Mixed        | 16.7         | 2.1     | 3.1       | 78.1  |

#### Classification Report:

| Label        | Precision | Recall | F1-score | Support |
| ------------ | --------- | ------ | -------- | ------- |
| Dissatisfied | 0.810     | 0.810  | 0.810    | 153     |
| Mixed        | 0.708     | 0.781  | 0.743    | 96      |
| Neutral      | 0.633     | 0.559  | 0.594    | 34      |
| Satisfied    | 0.814     | 0.714  | 0.761    | 49      |

- **Overall Accuracy**: 0.762
- **Weighted F1-score**: 0.761
- **Macro F1-score**: 0.727
- **Weighted Precision**: 0.763
- **Weighted Recall**: 0.762
- **Weighted F1**: 0.761

---

## V. Comparative Analysis

| Model                             | F1 | Notes                            |
| --------------------------------- | ----------- | -------------------------------- |
| **GPT-3.5 (Sood et al., 2024)**   | **0.80**    | Best overall performance         |
| **BERT**                          | 0.78        | Slightly below GPT-3.5           |
| **Gemini 2.5 Flash (This Study)** | **0.761**   | ≈ 95 % of GPT-3.5 F1 performance |
| **Llama 2 / Mistral / Orca 2**    | 0.57 – 0.65 | Significantly lower              |


---

## Observations

- Gemini 2.5 Flash matches GPT-3.5 on Satisfied, Mixed, and Dissatisfied classes but shows reduced recall for Neutral (55.9%).

- The confusion matrix mirrors GPT-3.5’s pattern, particularly confusion between Mixed and Dissatisfied, confirming cross-model consistency.

- Gemini demonstrates structured reasoning outputs akin to GPT-3.5, even when constrained by a free-tier API.
---

## VI. Discussion

This study validates the generalizability and robustness of the fine-grained prompting strategy proposed in SMILE-College. The close alignment in performance between Gemini 2.5 Flash and GPT-3.5 (only ~4–5% difference) suggests that prompt design contributes as much to classification quality as raw model scale.

However, Neutral sentiment detection remains a challenge, as observed in both studies. 

Despite using fewer samples (334 vs. 793) and a free LLM, Gemini 2.5 Flash produced coherent reasoning, confirming that modern instruction-tuned LLMs can perform high-quality sentiment classification with minimal cost.

## Conclusion

This replication and extension study shows that:

- The SMILE-College prompting framework successfully generalizes to other modern LLMs.

- Gemini 2.5 Flash achieves 95% of GPT-3.5’s performance using a smaller evaluation set and zero-shot prompting.

- Both models show consistent confusion patterns, underscoring the stability of sentiment boundaries across architectures.

These findings highlight that free, efficient LLMs can democratize academic sentiment research, enabling scalable and reproducible analysis of student mental health feedback.
