# School Dropout Prediction in Mexico

## Introduction

In this project, we will implement a Machine Learning model capable of predicting the probability of a student dropping out of the current academic cycle. This prediction will be based on various characteristics associated with the student, ranging from demographic conditions to factors that facilitate academic performance, such as homework support, financial dependency, and the student's level of academic stress.

You can use this README file as a guide to follow all the development process, or if you prefer to just run it. I'll leave the instructions here ##placeholder##

## Information Source

We will utilize data collected from the National Survey on Access and Permanence in Education ([ENAPE](https://www.inegi.org.mx/programas/enape/2021/)), conducted by the National Institute of Statistics and Geography ([INEGI](https://www.inegi.org.mx/)), the official body for conducting and publishing national surveys and censuses in Mexico.

The survey was conducted via telephone and collects information on all household residents aged 0 to 29 years and you can find very detailed information about its strategy and process in the official [landpage](https://www.inegi.org.mx/programas/enape/2021/) or directly in the [Dataset Documentation](https://github.com/Maxkaizo/---_-ML-Zoomcamp-2024/tree/main/Dataset%20Documentation) of our project ##placeholder##

## Objective (Value Proposition)

The primary objective of this project is to provide a tool that helps mitigate dropout rates, which can be achieved through:

a. Identifying the likelihood of dropout for each student.
b. Identifying the factors or conditions that most significantly contribute, both positively and negatively, to dropout.

This information is valuable for focusing efforts within the education system or even for parents to develop action plans, public policies, or special programs to combat school dropout.

## Problem Development

We will utilize the [CRISP-DM](https://en.wikipedia.org/wiki/Cross-industry_standard_process_for_data_mining) methodology as a reference framework to follow a structured approach that helps us achieve a robust model.

We'll also use this structure as project phases and file structure within the repository

### Business Understanding (From a Machine Learning Perspective)

#### Problem Definition

We will treat this project as a **binary classification** problem since our main goal is to identify whether a student will drop out of their school grade. In other words, there are only two possible outcomes in the final prediction: yes or no. However, thanks to the fact that Machine Learning algorithms are based on mathematical models and probabilities, this result will be accompanied by a **probability score**.

On the other hand, the survey (ENAPE) includes a question related to the completion of the school grade, which we will use as the label for our training process. Therefore, the type of learning will be **supervised**.

#### Evaluation definition

Finally, to determine the evaluation metrics we will focus on, we need to analyze the potential implications of incorrect predictions. The goal is to strike a balance that ensures the model truly adds value to decision-making processes while minimizing possible negative impacts.

In cases where a dropout is not detected (false negative), we will have missed the opportunity to intervene with the student, diminishing the project's proposed value as this scenario occurs. Therefore, minimizing this condition will be our priority. The metric associated with this situation is **Recall**.

On the other hand, in cases where a regular student is mistakenly identified as a dropout (false positive), the impact is less severe. This misclassification could serve as a targeted reinforcement toward completing their studies, with associated costs depending on the measures implemented. The metric tied to this situation is **Precision**, to which we will assign moderate priority.

Lastly, as additional support and to achieve an appropriate balance, we will use the F1-score, which is the harmonic mean of Recall and Precision.

With these considerations, the problem is described as follows:

- Problem Type:           Binary Classification
- Learning Type:          Supervised
- Evaluation Metrics:     Recall (High priority), Precision (Moderate Priority), F1-score and ROC-AUC (support)

### Data Understanding
This phase is documented in detail in the [1_pre_processing.ipynb](https://github.com/Maxkaizo/---_-ML-Zoomcamp-2024/blob/main/1_pre_processing.ipynb) file.

The process at a macro scale is:

1. Filter out records out of scope.
2. Keep features related to the previous school cycle, as this is the part of the dataset that contains labels.
3. Format the dataset in a useful and standard way.

For this process, the input file is **enape_raw_dataset.csv** and the output file is **enape_db_formated.csv**

### Data Preparation 
This phase is documented in detail in the [2_eda.ipynb](https://github.com/Maxkaizo/---_-ML-Zoomcamp-2024/blob/main/2_eda.ipynb) file.

Here we do the Exploratory Data Analysis and select relevant features. Where we manage to reduce from over a hundred of features, to 42.
For this process, the input file is **enape_db_formated.csv** and the output file is **enape_post_eda.csv**

### Modeling
This phase is documented in detail in the [3_modeling.ipynb](https://github.com/Maxkaizo/---_-ML-Zoomcamp-2024/blob/main/3_modeling.ipynb) file.
Apply Machine Learning algorithms to develop predictive models.

### Evaluation
Assess the model's performance using appropriate metrics to ensure it meets the defined objectives.

### Deployment
Implement the model into a functional system for real-world application.

## Script:

The trainning script is this file [train.py](https://github.com/Maxkaizo/---_-ML-Zoomcamp-2024/blob/main/train.py)
The predict script is this file [predict.py](https://github.com/Maxkaizo/---_-ML-Zoomcamp-2024/blob/main/predict.py)

## Deployment:

WIP


## Potential Biases:
- The survey was conducted by phone, so we must consider that people without this service at home are being omitted.
- Similarly, this survey only considers people enrolled in formal education, so a similar study or project would need to be conducted for those who have never been enrolled.

## Potential for Improvement

- Develop the model as a multi-class classifier to include the probability for each dropout cause.
- Segment the model by age range: the first group for primary and secondary education, where education is mandatory, and the second group for high school and higher education, where it is common in Mexico for this population to be part of the workforce.