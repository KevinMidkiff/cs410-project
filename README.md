# cs410-project
Intro to Performance CS410 Project

## Project Structure
The folder structure of the project breaks into four main directories. The table below contains all of these main directories with brief descriptions of what they each contain.

| Directory  |                                      Description                                       |
| :--------: | -------------------------------------------------------------------------------------- |
| build      | Contains the VIC model source code, and needed scripts for compilation.                |
| data       | Contains the VIC input data used in our study, as well as other data we found.         |
| results    | Contains the results from the tests we executed.                                       |
| run        | Contains the VIC release and debug executables compiled for Linux <code>x86_64</code>. |

## Building VIC
To compile the VIC binaries you will need to have the following dependencies installed.

- Make
- Build Essentials

After installing these on your system, execute the following commands.

```sh
$ cd build/
$ ./build.sh
```

The above commands will build both the release and debug versions of the VIC executable and put them in the <code>run</code> directory.

## Running VIC
To run the VIC executable, you will need to have first compile the binary, and then you will need an input data set with a global parameters file. For the Stehekin data set, execute the following commands.

```sh
$ cd data/Stehekin/
$ ../../run/vic_classic.exe -g parameters/global_param.STEHE.txt
```

> **NOTE:** Use <code>vic_classic_debug.exe</code> for the VIC executable to use the debug version of VIC.

## Running the Test Script
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

## License
This repo contains code from the VIC model source code, and is therefore subject to their licensing. For more information visit their documentation or GitHub repository linked below.
- [VIC GitHub](https://github.com/UW-Hydro/VIC)
- [VIC Documentation](http://vic.readthedocs.io/en/master/)
