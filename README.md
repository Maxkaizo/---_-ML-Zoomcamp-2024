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

- [Files](placeholder)

We will treat this project as a binary **classification problem** since our main goal is to identify whether a student will drop out of their school grade. In other words, there are only two possible outcomes in the final prediction: yes or no. However, thanks to the fact that Machine Learning algorithms are based on mathematical models and probabilities, this result will be accompanied by a **probability score**.

On the other hand, the survey (ENAPE) includes a question related to the completion of the school grade, which we will use as the label for our training process. Therefore, the type of learning will be **supervised**.

Finally, to determine the evaluation metrics we will focus on, we need to analyze the potential implications of incorrect predictions. The goal is to strike a balance that ensures the model truly adds value to decision-making processes while minimizing possible negative impacts.

In cases where a dropout is not detected (false negative), we will have missed the opportunity to intervene with the student, diminishing the project's proposed value as this scenario occurs. Therefore, minimizing this condition will be our priority. The metric associated with this situation is **Recall**.

On the other hand, in cases where a regular student is mistakenly identified as a dropout (false positive), the impact is less severe. This misclassification could serve as a targeted reinforcement toward completing their studies, with associated costs depending on the measures implemented. The metric tied to this situation is **Precision**, to which we will assign moderate priority.

Lastly, as additional support and to achieve an appropriate balance, we will use the F1-score, which is the harmonic mean of Recall and Precision.

With these considerations, the problem is described as follows:

Problem Type:           Binary Classification
Learning Type:          Supervised
Evaluation Metrics:
                        Recall
                        Precision
                        F1-score

- Data Understanding
This phase is documented in detail in the 
(poner aqui la liga al archivo de pre procesing)
Explore the dataset, identify patterns, and assess its quality and relevance to the problem.

- Data Preparation 
Clean, transform, and preprocess the data to make it suitable for modeling.

- Modeling --- aqui hacer referencia al archivo de modelado
Apply Machine Learning algorithms to develop predictive models.

- Evaluation
Assess the model's performance using appropriate metrics to ensure it meets the defined objectives.

- Deployment
Implement the model into a functional system for real-world application.

## Proceso para replicar:

Supuestos y Consideraciones

## sesgos identificados:

 al apoyo que recibe para sus estudios, desde el sustento, la

## Potencial de mejora
- Hacer el modelo multiclase para agregar la probabilidad de cada causa de abandono
- Hacer el modelo segmentado por rango de edades, el primer bloque, de primaria y secundaria, donde la educación es obligatoria y el segundo de bachillerato hacia arriba, donde es común en México que esa población se encuentre trabajando.

## Conclusiones