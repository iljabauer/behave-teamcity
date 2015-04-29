# behave-teamcity
A formatter for behave to report test results to TeamCity via service messages.
Following events will be reported

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


