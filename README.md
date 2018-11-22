# :fire: Realtime-Recommender :fire:
## About the Project
This application is a blueprint of a **realtime recommender** system with various functionallities. The recommender engine could host different models and different pipelines of data transformations.

---
### Technologies
* Python 3.x
* Apache Streaming Spark (soon!)
* Apache Kafka (soon!)
* MongoDb (soon!)

---
### Application structure

```
src\
|__app\
|    | __init__.py
|    |input_transformer.py
|    |post_processor.py
|    |pre_processot.py
|    |results_calculator.py
|    |run_recommender.py
|    |scorer.py
|    |settings.py
|    |__models\
|       |model_1.py
|       |model_2.py
|       |...
|     
|__tests\
    |__init__.py
    |input_transformer_tests.py
    |post_processor_tests.py
    |pre_processot_tests.py
    |results_calculator_tests.py
    |run_recommender_tests.py
    |scorer_tests.py

```
## Run Application engine
The Recommender application could support different modes and transformation pipelines:
#### Application mode
* Static mode
* Streaming mode

**Static Mode High-level Design**

soon!!

**Streaming Mode High-level Design**
![alt text](https://github.com/ggeop/Realtime-Recommender/blob/master/imgs/High_level_design.png)

The above architecture shows how to implement a streaming recommendation system from  an application perspective. The users will use a web interface which will be connected with a Kafka server. In kafka terms the web application(producer) will be enrolled in a specific Kafka topic. On the other side a Spark application(a Spark streaming application) will consume the data of the Kafka.

The models will be stored in flat file format in MongoDB database. Then the Spark will be enrolled in an another topic for the results (as a producer) and a web application will be also enrolled in this topic as consumer.

---
#### Application pipeline
![alt text](https://github.com/ggeop/Realtime-Recommender/blob/master/imgs/Recommendation_system_architecture.png)


* Representation Transformation
* Pre-processing
* Similarity Calculation
* Scoring
* Post-processing
* Calculate Results

**Representation Transformation**
This module is the first layer of our system. The aim of this module is to change the representation of the input in the appropriate structure. After this process, may we could filter the data from not useful values, wrong values or reduce the dimensionality of the data.

**Pre-processing**
This module refers to the transformation applied to the data before feeding to the algorithm.With preprocessing is a technique that is used to convert the raw data into a clean data set. Another aspect is that data set should be formatted in such a way that more than one Machine Learning and Deep Learning algorithms are executed in one data set, and best out of them is chosen. Preprocessing techniques are:
* Data rescale : This is a useful for optimization algorithms and also it’s useful for algorithms that weights inputs like neural networks
* Binarize data: This method transform the data using a binary threshold. All values above the threshold are marked as one and all equal or below are marked as zero.
* Standardize data: This technique is useful to transform attributes with Gaussian distributions and differing means and standard deviations to a Gaussian distribution with mean of zero and a standard deviation of one.

**Similarity Calculation**
This module is the ‘heart’ of the model. The similarity measure is the measure of how much alike two data objects are. Similarity measure in a data mining context is a distance with dimensions representing features of the objects. If this distance is small, it will be the high degree of similarity where large distance will be the low degree of similarity. The most popular similarity measures are:

* Euclidean distance
* Cosine Similarity
* Manhattan distance
* Minkowski distance
* Jaccard distance

In other words the model compares the similarity of the new entry with the existing objects. As a result is a ‘ similarity score’ . Then, the model should update (retrain) the stored model with this new entry and calculate the new weights.
NOTE: The retrain process is computationally intensive and maybe in a production server with high traffic is difficult to retrain the model in each user entity. So, it depends with the case the design of the system and how frequent will update the model weights.

**Scoring**
This module is an extra layer before the calculation of the final score of the new entity. Maybe the model has an extra layer with weights (e.g depends with the Helixes) or another model for weights calculation.

**Post-processing**
This stage is the final processing step before calculate the model results. In this step we check the quality of the results, maybe the algorithm has calculated results that are not business right or meaningful. In other words will apply business roles in the results.

**Calculate Results**
This module has as an input a matrix with scores and as an output the recommendation result with the right representation. It’s a transformation step, we can say that is the reverse procedure of the module ‘pre-processing’.

---
