#!/usr/bin/env python3

from rubikscubennnsolver import ImplementThis, SolveError, StuckInALoop
from rubikscubennnsolver.RubiksCube222 import RubiksCube222, solved_2x2x2
from rubikscubennnsolver.RubiksCube333 import RubiksCube333, solved_3x3x3
from rubikscubennnsolver.RubiksCube444 import RubiksCube444, solved_4x4x4
from rubikscubennnsolver.RubiksCube555 import RubiksCube555, solved_5x5x5
from rubikscubennnsolver.RubiksCube666 import RubiksCube666, solved_6x6x6
from rubikscubennnsolver.RubiksCube777 import RubiksCube777, solved_7x7x7
from rubikscubennnsolver.RubiksCubeNNNEven import RubiksCubeNNNEven, solved_8x8x8, solved_10x10x10, solved_12x12x12, solved_14x14x14
from rubikscubennnsolver.RubiksCubeNNNOdd import RubiksCubeNNNOdd, solved_9x9x9, solved_11x11x11, solved_13x13x13, solved_15x15x15
import argparse
import json
import logging
import os
import sys

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(filename)12s %(levelname)8s: %(message)s')
log = logging.getLogger(__name__)

# Color the errors and warnings in red
logging.addLevelName(logging.ERROR, "\033[91m   %s\033[0m" % logging.getLevelName(logging.ERROR))
logging.addLevelName(logging.WARNING, "\033[91m %s\033[0m" % logging.getLevelName(logging.WARNING))

parser = argparse.ArgumentParser()
parser.add_argument('--size', type=str, default='4x4x4')
parser.add_argument('--test-cubes', type=str, default='test_cubes.json')
parser.add_argument('--start', type=int, default=0)
args = parser.parse_args()

try:

    with open(args.test_cubes, 'r') as fh:
        test_cases = json.load(fh)

    solution_total = 0
    centers_solution_total = 0
    edges_solution_total = 0
    min_solution = None
    max_solution = None
    min_solution_kociemba_string = None
    max_solution_kociemba_string = None

    results = []
    order = 'URFDLB'

    for size in sorted(test_cases.keys()):

        if args.size != 'all' and size != args.size:
            continue

        # solve the cube
        if size == '2x2x2':
            cube = RubiksCube222(solved_2x2x2, order)

        elif size == '3x3x3':
            cube = RubiksCube333(solved_3x3x3, order)

        elif size == '4x4x4':
            cube = RubiksCube444(solved_4x4x4, order)

        elif size == '5x5x5':
            cube = RubiksCube555(solved_5x5x5, order)

        elif size == '6x6x6':
            cube = RubiksCube666(solved_6x6x6, order)

        elif size == '7x7x7':
            cube = RubiksCube777(solved_7x7x7, order)

        elif size == '8x8x8':
            cube = RubiksCubeNNNEven(solved_8x8x8, order)

        elif size == '9x9x9':
            cube = RubiksCubeNNNOdd(solved_9x9x9, order)

        elif size == '10x10x10':
            cube = RubiksCubeNNNEven(solved_10x10x10, order)

        elif size == '11x11x11':
            cube = RubiksCubeNNNOdd(solved_11x11x11, order)

        elif size == '12x12x12':
            continue # no need to test above 10x10x10
            cube = RubiksCubeNNNEven(solved_12x12x12, order)

        elif size == '13x13x13':
            continue # no need to test above 11x11x11
            cube = RubiksCubeNNNOdd(solved_13x13x13, order)

        elif size == '14x14x14':
            continue # no need to test above 10x10x10
            cube = RubiksCubeNNNEven(solved_14x14x14, order)

        elif size == '15x15x15':
            continue # no need to test above 11x11x11
            cube = RubiksCubeNNNOdd(solved_15x15x15, order)

        else:
            print("ERROR: Add support for %s" % size)
            sys.exit(1)

        cube.cpu_mode = 'normal'
        kociemba_strings = test_cases[size]
        num_test_cases = len(kociemba_strings)
        num_test_cases_executed = 0

        for (index, kociemba_string) in enumerate(kociemba_strings):

            if index < args.start:
                continue

            # Only test one of each for 'all'
            if args.size == 'all' and index > 0:
                continue

            #os.system('clear')
            log.warning("Test %d/%d %s cube: %s" % (index, num_test_cases, size, kociemba_string))
            num_test_cases_executed += 1
            kociemba_string = str(kociemba_string)
            cube.solution = []
            cube.load_state(kociemba_string, order)

            try:
                cube.solve()
                solution = cube.solution
            except Exception as e:
                results.append("\033[91m%s FAIL (exception) \033[0m: %s\n%s\n" % (size, kociemba_string, str(e)))
                continue

            # Now put the cube back in its initial state and verify the solution solves it
            # uncomment this to test compress_solution()
            #cube = RubiksCube(kociemba_string)
            #for step in solution:
            #    cube.rotate(step)

            if cube.solved():
                results.append("\033[92m%s PASS\033[0m: %s" % (size, kociemba_string))
                # cube.print_solution()
            else:
                results.append("\033[91m%s FAIL (not solved)\033[0m: %s" % (size, kociemba_string))
                cube.print_cube()
                cube.print_solution()
                break
                '''
                for result in results:
                    print(result)

                cube.print_cube()
                assert False, "Cube should be solvd but it isn't"
                '''

            solution_length = len(cube.solution)
            solution_total += solution_length
            centers_solution_total += cube.steps_to_solve_centers
            edges_solution_total += cube.steps_to_group_edges

            if min_solution is None or solution_length < min_solution:
                min_solution = solution_length
                min_solution_kociemba_string = kociemba_string

            if max_solution is None or solution_length > max_solution:
                max_solution = solution_length
                max_solution_kociemba_string = kociemba_string

        results.append("%s avg centers solution %s steps" % (size, float(centers_solution_total/num_test_cases_executed)))
        results.append("%s avg edges solution %s steps" % (size, float(edges_solution_total/num_test_cases_executed)))
        results.append("%s avg solution %s steps" % (size, float(solution_total/num_test_cases_executed)))
        results.append("%s min solution %s steps (%s)" % (size, min_solution, min_solution_kociemba_string))
        results.append("%s max solution %s steps (%s)" % (size, max_solution, max_solution_kociemba_string))
        results.append("")

    for result in results:
        print(result)

except ImplementThis:
    cube.print_cube_layout()
    raise

except SolveError:
    cube.print_cube_layout()
    cube.print_cube()
    raise

except StuckInALoop:
    cube.print_cube_layout()
    cube.print_cube()
    raise
