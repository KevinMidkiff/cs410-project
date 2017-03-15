# cs410-project
Intro to Performance CS410 Project

## Running Test Script
>**NOTE:** This script must be ran with Python 3

The script <code>run_test.py</code> is meant for running tests and gathering wall clock time on the execution of VIC over a specific data set. The script has the following command line arguments:

```sh
usage: run_tests.py [-h] [-bin BIN] [-n N] stats_result_file tests

positional arguments:
  stats_result_file  Result file to write statistical data to
  tests              JSON file defining tests to execute

optional arguments:
  -h, --help         show this help message and exit
  -bin BIN           Location of the VIC exe to execute
  -n N               Number of iterations to execute a test
```

An example of executing this script is:

```sh
$ python3 run_test.py results.csv tests.json
```

This will execute the tests defined in <code>tests.json</code> and output the results of the tests to the <code>results.csv</code> file.

The JSON configuration file has given to this script has the following structure:

```json
{
    "tests": [
        {
            "name": "<STRING>",
            "working_dir": "<STRING>",
            "global_params": "<STRING>",
            "vic_results_dir": "<STRING>"
        },
    ]
}
```

In this JSON file, <code>tests</code> is a list of objects with the structure shown above. The keys correspond to the following data.

- <code>name</code> - Name of the test
- <code>working_dir</code> - Directory to execute the test from
- <code>global_params</code> - Location from the <code>working_dir</code> directory of the VIC global parameters file
- <code>vic_results_dir</code> - Results directory for VIC to verify exists, and to create if it does not
