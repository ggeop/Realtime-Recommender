[![Build Status](https://travis-ci.com/ggeop/Realtime-Recommender.svg?token=82JpHh3MEmRmWpfnbt6K&branch=master)](https://travis-ci.com/ggeop/Realtime-Recommender)
[![CodeFactor](https://www.codefactor.io/repository/github/ggeop/realtime-recommender/badge)](https://www.codefactor.io/repository/github/ggeop/realtime-recommender)
#  :small_red_triangle: Realtime-Recommender
## About the Project
This application is a blueprint of a **realtime recommender** system with various functionallities. The recommender engine could host different models and different pipelines of data transformations.

---

### Depedencies

 Technologies | Libraries
 ---|---
[*Python 3.x*](https://www.python.org/downloads/release/python-360/), [*Apache Streaming Spark*](https://spark.apache.org/streaming/) (soon!), [*Apache Kafka*](https://kafka.apache.org/) (soon!)  | [Gensim](https://radimrehurek.com/gensim/tutorial.html), [Scikit-learn](https://scikit-learn.org/stable/), [Numpy](http://www.numpy.org/), [Pandas](https://pandas.pydata.org/)


---

### Application structure

```
src\
|__app\
|  |__init__.py
|
|__recommender\
|    | __init__.py
|    |input_transformer.py
|    |model_manager.py
|    |post_processor.py
|    |pre_processot.py
|    |results_calculator.py
|    |run_engine.py
|    |scorer.py
|    |settings.py
|    |__models\
|    |__
|       |__init__.py
|       |model_1.py
|       |model_2.py
|       |...
|     
|__tests\
    |__init__.py
    |input_transformer_tests.py
    |model_manager_tests.py
    |post_processor_tests.py
    |pre_processot_tests.py
    |results_calculator_tests.py
    |run_engine_tests.py
    |scorer_tests.py

```

---
