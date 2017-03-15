"""Python script for executing tests on the VIC modeling tool.
"""

import argparse
import os
import json
import subprocess as sub
import time
import sys
import csv
from statistics import mean, variance, stdev
import signal

# PID of the VIC process (if running, None if it is not)
PID = None

def parse_args():
    """Parse command line arguments.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('stats_result_file', help='Result file to write statistical data to')
    parser.add_argument('tests', help='JSON file defining tests to execute')
    parser.add_argument('-bin', type=str, default='./run/vic_classic.exe',
                        help='Location of the VIC exe to execute')
    parser.add_argument('-n', type=int, default=30, 
                        help='Number of iterations to execute a test')
    return parser.parse_args()


def print_progress_bar(iteration, total, prefix='', suffix='', decimals=1, length=100, fill='█'):
    """Progress bar
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end = '\r')
    # Print New Line on Complete
    if iteration == total:
        print()


def signal_handler(pid, signum, frame):
    """Signal handler to kill vic process if CTRL-C.
    """
    global PID
    if PID is not None:
        print('Killing VIC')
        os.killpg(os.getgpid(PID), signal.SIGTERM)


def run(cmd, n):
    """Execute the given command n times and return a list of how long
    each execution took.
    """
    global PID
    times = []
    pbar = lambda i: print_progress_bar(
            i, n, prefix='\tProgress:', suffix='Complete', length=25)

    pbar(0)

    for i in range(n):
        start = time.time()
        p = sub.Popen(cmd, stdout=sub.PIPE, stderr=sub.PIPE)
        PID = p.pid
        p.communicate()
        end = time.time()
        PID = None
        times.append(end - start)
        pbar(i + 1)

    return times


def main():
    """Main
    """
    header = ['Test', 'Average', 'Variance', 'Std. Dev.']
    args = parse_args()
    
    try:
        config = None

        with open(args.tests, 'r') as f:
            config = json.load(f)

        tests = config['tests']
        binary = os.path.abspath(args.bin)
        start_dir = os.getcwd()

        if not os.path.exists(binary):
            print('ERROR: VIC executable does not exist - {}'.format(binary))
            return -1

        print('-- Setting up results file')
        with open(args.stats_result_file, 'w') as f:
            writer = csv.DictWriter(f, fieldnames=header)
            writer.writeheader()

        for test in tests:
            test_name = test['name']
            working_dir = test['working_dir']
            global_params = test['global_params']
            vic_results_dir = test['vic_results_dir']

            print('-- Running test: {}'.format(test_name))

            os.chdir(working_dir)

            if not os.path.exists(vic_results_dir):
                os.mkdir(vic_results_dir)

            times = run([binary, '-g', global_params], args.n)
            os.chdir(start_dir)

            print('-- Test finished, calculating results')

            results = {
                'Test': test_name,
                'Average': mean(times),
                'Variance': variance(times),
                'Std. Dev.': stdev(times)
            }
            
            print('-- Writing results to {}'.format(args.stats_result_file))
            with open(args.stats_result_file, 'a') as f:
                writer = csv.DictWriter(f, fieldnames=header)
                writer.writerow(results)

    except KeyError as e:
        print('ERROR: JSON config {} missing key {}'.format(args.tests, e))
        return -1
    except IOError:
        print('ERROR: JSON file {} does no exist'.format(args.tests))
        return -1
    except KeyboardInterrupt:
        print('Quitting...')

    return 0


if __name__ == '__main__':
    sys.exit(main())
