# behave-teamcity
A formatter for behave to report test results to TeamCity via service messages.

## Features

| behave           | TeamCity            |
| ---              | ---                 |
| Feature start    | Test suite start    |
| Feature end      | Test suite finished |
| Scenario start   | Test start          |
| Scenario end     | Test finished       |
| Scenario failed  | Test failed         |
| Skipped Scenario | Ignored test        |   


## Installation
```bash
pip install behave-teamcity
````

## Usage
You can specify the formatter directly in the command line using the -f argument:
```bash
behave -f behave_teamcity:TeamcityFormatter
```
or
```bash
behave --format behave_teamcity:TeamcityFormatter
```

You can also register the formatter to be available through a simple name:
```ini
# -- FILE: behave.ini
[behave.formatters]
teamcity = behave_teamcity:TeamcityFormatter
```
and the use it like:
```bash
behave --f teamcity
```


