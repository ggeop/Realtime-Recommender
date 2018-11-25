[![Build Status](https://travis-ci.com/ggeop/Realtime-Recommender.svg?token=82JpHh3MEmRmWpfnbt6K&branch=master)](https://travis-ci.com/ggeop/Realtime-Recommender)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/ansicolortags.svg)](https://pypi.python.org/pypi/ansicolortags/)
[![CodeFactor](https://www.codefactor.io/repository/github/ggeop/realtime-recommender/badge)](https://www.codefactor.io/repository/github/ggeop/realtime-recommender)
[![GPLv3 license](https://img.shields.io/badge/License-GPLv3-blue.svg)](http://perso.crans.org/besson/LICENSE.html)
#:person_with_blond_hair:Realtime-Recommender
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
### Application Overview
* [Application modes](https://github.com/ggeop/Realtime-Recommender/wiki/Application-modes)
* [Application pipeline](https://github.com/ggeop/Realtime-Recommender/wiki/Application-pipeline)
---

### Licence
This work is licensed under a [GNU General Public License v3.0](https://github.com/ggeop/Realtime-Recommender/blob/master/LICENSE)
