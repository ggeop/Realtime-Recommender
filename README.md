[![Build Status](https://travis-ci.com/ggeop/Realtime-Recommender.svg?token=82JpHh3MEmRmWpfnbt6K&branch=master)](https://travis-ci.com/ggeop/Realtime-Recommender)
[![CodeFactor](https://www.codefactor.io/repository/github/ggeop/realtime-recommender/badge)](https://www.codefactor.io/repository/github/ggeop/realtime-recommender)
[![GPLv3 license](https://img.shields.io/badge/License-GPLv3-blue.svg)](http://perso.crans.org/besson/LICENSE.html)
# :partly_sunny:Realtime-Recommender
## About the Project
This application is a blueprint of a **Recommender Engine** with various functionalities. The recommender could support different models and different transformation pipelines.
![alt text](https://github.com/ggeop/Realtime-Recommender/blob/master/imgs/recommendation_engine.png)

---

### Depedencies

 Technologies | Libraries
 ---|---
[*Python 3.x*](https://www.python.org/downloads/release/python-360/), [*Apache Streaming Spark*](https://spark.apache.org/streaming/) + [*Apache Kafka*](https://kafka.apache.org/) (soon!)  | [Gensim](https://radimrehurek.com/gensim/tutorial.html), [Scikit-learn](https://scikit-learn.org/stable/), [Pandas](https://pandas.pydata.org/), [Numpy](http://www.numpy.org/)


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
|    |model_feeder.py
|    |model_manager.py
|    |post_processor.py
|    |pre_processot.py
|    |results_calculator.py
|    |run_engine.py
|    |settings.py
|    |__models\
|    |__
|       |__init__.py
|       |Word2Vec_model.py
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
### Application Overview
* [Application modes](https://github.com/ggeop/Realtime-Recommender/wiki/Application-modes)
* [Application pipeline](https://github.com/ggeop/Realtime-Recommender/wiki/Application-pipeline)
---

### Licence
This work is licensed under a [GNU General Public License v3.0](https://github.com/ggeop/Realtime-Recommender/blob/master/LICENSE)
