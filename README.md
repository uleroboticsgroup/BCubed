# BCubed (Blockchain-based Black Box)
BCubed is a Python library designed to facilitate traceability in autonomous systems in a cibersecure manner. It allows the creation and utilization of a black box employing blockchain technology.

## :warning: Disclaimer
This Python library has only been tested in simulated blockchain environments. Using it in other environments is at your own risk. Keep possible charges in mind.


## Getting Started

### Create and activate a virtual enviroment (recommended)
```
$ python3 -m venv .venv
$ source .venv/bin/activate
```

### Install the requirements
```
(.venv) $ pip install -r requirements.txt
```

### Install BCubed
```
(.venv) $ pip install -e <bcubed_location>
```

### Configure BCubed

1. Update the configuration data in the `bcubed-config.yaml` file.

1. Configure the environment variable named BCUBED_CONF_FILE to set the `bcubed-config.yaml` path. By default, it is set to `./bcubed-config.yaml`.

### Uninstall BCubed
```
(.venv) $ pip uninstall bcubed
```

## Acknowledgements

This research is part of the project TESCAC, financed by “European Union NextGeneration-EU, the Recovery Plan, Transformation and Resilience, through INCIBE".

<p align="center">
  <img src="./docs/INCIBE.jpg" width="100%" />
</p>
