# BCubed
BCubed is a Python package library designed to facilitate traceability in autonomous systems in a cibersecure manner. It allows the creation and utilization of a black box employing blockchain technology. The nomenclature of the system is derived from the term "blockchain-based black box.


## Virtual environment (recommended)
### Create and activate a virtual enviroment
```
$ python3 -m venv .venv
$ source .venv/bin/activate
```


## Requirements
### Install the requirements
```
(.venv) $ pip install -r requirements.txt
```


## Install BCubed
```
(.venv) $ pip install -e <bcubed_location>
```


## Tests
### Run all tests with coverage generation
```
(.venv) $ pytest --cov=src --cov-report=lcov --cov-report xml --cov-report term
```


## Uninstall BCubed
```
(.venv) $ pip uninstall bcubed
```

## Acknowledgements

This research is part of the project TESCAC, financed by “European Union NextGeneration-EU, the Recovery Plan, Transformation and Resilience, through INCIBE".

<p align="center">
  <img src="./docs/INCIBE.jpg" width="100%" />
</p>