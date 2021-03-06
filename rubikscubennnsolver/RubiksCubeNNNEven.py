
from rubikscubennnsolver.RubiksCube444 import RubiksCube444, solved_4x4x4
from rubikscubennnsolver.RubiksCube555 import RubiksCube555, solved_5x5x5
from rubikscubennnsolver.RubiksCube666 import RubiksCube666, solved_6x6x6
from rubikscubennnsolver.RubiksCube777 import RubiksCube777, solved_7x7x7
from rubikscubennnsolver.RubiksCubeNNNEvenEdges import RubiksCubeNNNEvenEdges
from math import ceil
import logging
import sys

log = logging.getLogger(__name__)

solved_8x8x8 = 'UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUURRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB'

solved_10x10x10 = 'UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUURRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB'

solved_12x12x12 = 'UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUURRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB'

solved_14x14x14 = 'UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUURRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB'

moves_8x8x8 = ("U", "U'", "U2", "Uw", "Uw'", "Uw2", "3Uw", "3Uw'", "3Uw2", "4Uw", "4Uw'", "4Uw2",
               "L", "L'", "L2", "Lw", "Lw'", "Lw2", "3Lw", "3Lw'", "3Lw2", "4Lw", "4Lw'", "4Lw2",
               "F", "F'", "F2", "Fw", "Fw'", "Fw2", "3Fw", "3Fw'", "3Fw2", "4Fw", "4Fw'", "4Fw2",
               "R", "R'", "R2", "Rw", "Rw'", "Rw2", "3Rw", "3Rw'", "3Rw2", "4Rw", "4Rw'", "4Rw2",
               "B", "B'", "B2", "Bw", "Bw'", "Bw2", "3Bw", "3Bw'", "3Bw2", "4Bw", "4Bw'", "4Bw2",
               "D", "D'", "D2", "Dw", "Dw'", "Dw2", "3Dw", "3Dw'", "3Dw2", "4Dw", "4Dw'", "4Dw2")

moves_10x10x10 = ("U", "U'", "U2", "Uw", "Uw'", "Uw2", "3Uw", "3Uw'", "3Uw2", "4Uw", "4Uw'", "4Uw2", "5Uw", "5Uw'", "5Uw2",
                  "L", "L'", "L2", "Lw", "Lw'", "Lw2", "3Lw", "3Lw'", "3Lw2", "4Lw", "4Lw'", "4Lw2", "5Lw", "5Lw'", "5Lw2",
                  "F", "F'", "F2", "Fw", "Fw'", "Fw2", "3Fw", "3Fw'", "3Fw2", "4Fw", "4Fw'", "4Fw2", "5Fw", "5Fw'", "5Fw2",
                  "R", "R'", "R2", "Rw", "Rw'", "Rw2", "3Rw", "3Rw'", "3Rw2", "4Rw", "4Rw'", "4Rw2", "5Rw", "5Rw'", "5Rw2",
                  "B", "B'", "B2", "Bw", "Bw'", "Bw2", "3Bw", "3Bw'", "3Bw2", "4Bw", "4Bw'", "4Bw2", "5Bw", "5Bw'", "5Bw2",
                  "D", "D'", "D2", "Dw", "Dw'", "Dw2", "3Dw", "3Dw'", "3Dw2", "4Dw", "4Dw'", "4Dw2", "5Dw", "5Dw'", "5Dw2")


class RubiksCubeNNNEven(RubiksCubeNNNEvenEdges):
    """
    Inheritance model
    -----------------

            RubiksCube
                |
        RubiksCubeNNNEvenEdges
           /            \
    RubiksCubeNNNEven RubiksCube666
    """

    def phase(self):
        return 'Solve Even NxNxN'

    def make_plus_sign(self):
        """
        Pair the middle two columns/rows in order to convert this Even cube into
        an Odd cube...this allows us to use the 7x7x7 solver later.  It makes what
        looks like a large "plus" sign on each cube face thus the name of this
        method.
        """
        center_orbit_count = int((self.size - 4)/2)

        # Make a big "plus" sign on each side, this will allow us to reduce the
        # centers to a series of 7x7x7 centers
        for center_orbit_id in range(center_orbit_count):

            # Group UD centers
            # - create a fake 6x6x6 to solve the inside 4x4 block
            fake_666 = RubiksCube666(solved_6x6x6, 'URFDLB')

            for index in range(1, 217):
                fake_666.state[index] = 'x'
            fake_666.cpu_mode = self.cpu_mode

            start_666 = 0
            start_NNN = 0

            for x in range(6):
                start_NNN_row1 = int(start_NNN + (((self.size/2) - 2) * self.size) + ((self.size/2) - 1))
                start_NNN_row2 = start_NNN_row1 + self.size
                start_NNN_row3 = start_NNN_row2 + self.size
                start_NNN_row4 = start_NNN_row3 + self.size

                #fake_666.state[start_666+8] = self.state[start_NNN_row1 - (center_orbit_id * self.size)]
                fake_666.state[start_666+9] = self.state[start_NNN_row1+1 - (center_orbit_id * self.size)]
                fake_666.state[start_666+10] = self.state[start_NNN_row1+2 - (center_orbit_id * self.size)]
                #fake_666.state[start_666+11] = self.state[start_NNN_row1+3 - (center_orbit_id * self.size)]

                fake_666.state[start_666+14] = self.state[start_NNN_row2 - center_orbit_id]
                fake_666.state[start_666+15] = self.state[start_NNN_row2+1]
                fake_666.state[start_666+16] = self.state[start_NNN_row2+2]
                fake_666.state[start_666+17] = self.state[start_NNN_row2+3 + center_orbit_id]

                fake_666.state[start_666+20] = self.state[start_NNN_row3 - center_orbit_id]
                fake_666.state[start_666+21] = self.state[start_NNN_row3+1]
                fake_666.state[start_666+22] = self.state[start_NNN_row3+2]
                fake_666.state[start_666+23] = self.state[start_NNN_row3+3 + center_orbit_id]

                #fake_666.state[start_666+26] = self.state[start_NNN_row4 + (center_orbit_id * self.size)]
                fake_666.state[start_666+27] = self.state[start_NNN_row4+1 + (center_orbit_id * self.size)]
                fake_666.state[start_666+28] = self.state[start_NNN_row4+2 + (center_orbit_id * self.size)]
                #fake_666.state[start_666+29] = self.state[start_NNN_row4+3 + (center_orbit_id * self.size)]
                start_666 += 36
                start_NNN += (self.size * self.size)

            fake_666.sanity_check()

            # Group LR centers (in turn groups FB)
            fake_666.lt_init()
            fake_666.print_cube()
            fake_666.group_centers_guts(oblique_edges_only=True)
            #fake_666.print_solution()
            fake_666.print_cube()

            # Apply the 6x6x6 solution to our cube
            half_size = str(int(self.size/2))
            wide_size = str(int(half_size) - 1 - center_orbit_id)

            for step in fake_666.solution:
                if step.startswith("3"):
                    self.rotate(half_size + step[1:])
                elif "w" in step:
                    self.rotate(wide_size + step)
                else:
                    self.rotate(step)
            fake_666 = None

        log.info("Big plus sign formed, %d steps in" % self.get_solution_len_minus_rotates(self.solution))
        self.print_cube()

    def solve_inside_777(self, center_orbit_id, max_center_orbits, width, cycle, max_cycle):
        fake_777 = RubiksCube777(solved_7x7x7, 'URFDLB')

        for index in range(1, 295):
            fake_777.state[index] = 'x'
        fake_777.cpu_mode = self.cpu_mode

        start_777 = 0
        start_NNN = 0
        row0_midpoint = ceil(self.size/2)

        log.info("Start center_orbit_id, %d, max_center_orbits %s, width %s, cycle %s, max_cycle %s" %\
            (center_orbit_id, max_center_orbits, width, cycle, max_cycle))

        for x in range(6):
            mid_NNN_row1 = start_NNN + row0_midpoint + (self.size * (max_center_orbits - center_orbit_id + 1))
            start_NNN_row1 = mid_NNN_row1 - (2 + cycle)
            end_NNN_row1 = mid_NNN_row1 + (2 + cycle) + 1

            start_NNN_row5 = start_NNN_row1 + ((width-1) * self.size)
            mid_NNN_row5 = mid_NNN_row1 + ((width-1) * self.size)
            end_NNN_row5 = end_NNN_row1 + ((width-1) * self.size)

            mid_NNN_row3 = int(mid_NNN_row1 + ((width/2) * self.size) - self.size)
            start_NNN_row3 = mid_NNN_row3 - (2 + center_orbit_id)
            end_NNN_row3 = mid_NNN_row3 + (2 + center_orbit_id) + 1

            start_NNN_row2 = start_NNN_row3 - (self.size * (cycle+1))
            start_NNN_row4 = start_NNN_row3 + (self.size * (cycle+1)) + self.size

            end_NNN_row2 = end_NNN_row3 - (self.size * (cycle+1))
            end_NNN_row4 = end_NNN_row3 + (self.size * (cycle+1)) + self.size

            mid_NNN_row2 = int((start_NNN_row2 + end_NNN_row2)/2)
            mid_NNN_row4 = int((start_NNN_row4 + end_NNN_row4)/2)

            row1_col1 = start_NNN_row1
            row1_col2 = start_NNN_row1+1
            row1_col3 = mid_NNN_row1
            row1_col4 = end_NNN_row1-1
            row1_col5 = end_NNN_row1

            row2_col1 = start_NNN_row2
            row2_col2 = start_NNN_row2+1
            row2_col3 = mid_NNN_row2
            row2_col4 = end_NNN_row2-1
            row2_col5 = end_NNN_row2

            row3_col1 = start_NNN_row3
            row3_col2 = start_NNN_row3+1
            row3_col3 = mid_NNN_row3
            row3_col4 = end_NNN_row3-1
            row3_col5 = end_NNN_row3

            row4_col1 = start_NNN_row4
            row4_col2 = start_NNN_row4+1
            row4_col3 = mid_NNN_row4
            row4_col4 = end_NNN_row4-1
            row4_col5 = end_NNN_row4

            row5_col1 = start_NNN_row5
            row5_col2 = start_NNN_row5+1
            row5_col3 = mid_NNN_row5
            row5_col4 = end_NNN_row5-1
            row5_col5 = end_NNN_row5

            log.info("%d: start_NNN_row1 %d, mid_NNN_row1 %d, end_NNN_row1 %d" % (x, start_NNN_row1, mid_NNN_row1, end_NNN_row1))
            log.info("%d: start_NNN_row2 %d, mid_NNN_row2 %d, end_NNN_row2 %d" % (x, start_NNN_row2, mid_NNN_row2, end_NNN_row2))
            log.info("%d: start_NNN_row3 %d, mid_NNN_row3 %d, end_NNN_row3 %d" % (x, start_NNN_row3, mid_NNN_row3, end_NNN_row3))
            log.info("%d: start_NNN_row4 %d, mid_NNN_row4 %d, end_NNN_row4 %d" % (x, start_NNN_row4, mid_NNN_row4, end_NNN_row4))
            log.info("%d: start_NNN_row5 %d, mid_NNN_row5 %d, end_NNN_row5 %d" % (x, start_NNN_row5, mid_NNN_row5, end_NNN_row5))

            log.info("%d: row1 %d, %d, %d, %d, %d" % (x, row1_col1, row1_col2, row1_col3, row1_col4, row1_col5))
            log.info("%d: row2 %d, %d, %d, %d, %d" % (x, row2_col1, row2_col2, row2_col3, row2_col4, row2_col5))
            log.info("%d: row3 %d, %d, %d, %d, %d" % (x, row3_col1, row3_col2, row3_col3, row3_col4, row3_col5))
            log.info("%d: row4 %d, %d, %d, %d, %d" % (x, row4_col1, row4_col2, row4_col3, row4_col4, row4_col5))
            log.info("%d: row5 %d, %d, %d, %d, %d\n\n" % (x, row5_col1, row5_col2, row5_col3, row5_col4, row5_col5))

            if ((center_orbit_id == 0 and cycle == 0) or
                (center_orbit_id == max_center_orbits and cycle == max_cycle)):
                fake_777.state[start_777+9] = self.state[row1_col1]
                fake_777.state[start_777+10] = self.state[row1_col2]
                fake_777.state[start_777+11] = self.state[row1_col3]
                fake_777.state[start_777+12] = self.state[row1_col4]
                fake_777.state[start_777+13] = self.state[row1_col5]

                fake_777.state[start_777+16] = self.state[row2_col1]
                fake_777.state[start_777+17] = self.state[row2_col2]
                fake_777.state[start_777+18] = self.state[row2_col3]
                fake_777.state[start_777+19] = self.state[row2_col4]
                fake_777.state[start_777+20] = self.state[row2_col5]

                fake_777.state[start_777+23] = self.state[row3_col1]
                fake_777.state[start_777+24] = self.state[row3_col2]
                fake_777.state[start_777+25] = self.state[row3_col3]
                fake_777.state[start_777+26] = self.state[row3_col4]
                fake_777.state[start_777+27] = self.state[row3_col5]

                fake_777.state[start_777+30] = self.state[row4_col1]
                fake_777.state[start_777+31] = self.state[row4_col2]
                fake_777.state[start_777+32] = self.state[row4_col3]
                fake_777.state[start_777+33] = self.state[row4_col4]
                fake_777.state[start_777+34] = self.state[row4_col5]

                fake_777.state[start_777+37] = self.state[row5_col1]
                fake_777.state[start_777+38] = self.state[row5_col2]
                fake_777.state[start_777+39] = self.state[row5_col3]
                fake_777.state[start_777+40] = self.state[row5_col4]
                fake_777.state[start_777+41] = self.state[row5_col5]

            else:
                #fake_777.state[start_777+9] = self.state[row1_col1]
                fake_777.state[start_777+10] = self.state[row1_col2]
                fake_777.state[start_777+11] = self.state[row1_col3]
                fake_777.state[start_777+12] = self.state[row1_col4]
                #fake_777.state[start_777+13] = self.state[row1_col5]

                fake_777.state[start_777+16] = self.state[row2_col1]
                fake_777.state[start_777+17] = self.state[row2_col2]
                fake_777.state[start_777+18] = self.state[row2_col3]
                fake_777.state[start_777+19] = self.state[row2_col4]
                fake_777.state[start_777+20] = self.state[row2_col5]

                fake_777.state[start_777+23] = self.state[row3_col1]
                fake_777.state[start_777+24] = self.state[row3_col2]
                fake_777.state[start_777+25] = self.state[row3_col3]
                fake_777.state[start_777+26] = self.state[row3_col4]
                fake_777.state[start_777+27] = self.state[row3_col5]

                fake_777.state[start_777+30] = self.state[row4_col1]
                fake_777.state[start_777+31] = self.state[row4_col2]
                fake_777.state[start_777+32] = self.state[row4_col3]
                fake_777.state[start_777+33] = self.state[row4_col4]
                fake_777.state[start_777+34] = self.state[row4_col5]

                #fake_777.state[start_777+37] = self.state[row5_col1]
                fake_777.state[start_777+38] = self.state[row5_col2]
                fake_777.state[start_777+39] = self.state[row5_col3]
                fake_777.state[start_777+40] = self.state[row5_col4]
                #fake_777.state[start_777+41] = self.state[row5_col5]

            start_777 += 49
            start_NNN += (self.size * self.size)

        # Group LR centers (in turn groups FB)
        fake_777.sanity_check()
        fake_777.print_cube()
        fake_777.lt_init()

        # Apply the 7x7x7 solution to our cube
        half_size = str( ceil(self.size/2) - 1 - cycle )
        wide_size = str( ceil(self.size/2) - 2 - center_orbit_id)

        if ((center_orbit_id == 0 and cycle == 0) or
            (center_orbit_id == max_center_orbits and cycle == max_cycle)):
            fake_777.group_centers_guts()
        else:
            fake_777.group_centers_guts(oblique_edges_only=True)

        for step in fake_777.solution:
            if step.startswith("3"):
                self.rotate(half_size + step[1:])
            elif "w" in step:
                self.rotate(wide_size + step)
            else:
                self.rotate(step)

        self.print_cube()
        log.info("End center_orbit_id, %d, max_center_orbits %s, width %s, cycle %s, max_cycle %s" %\
            (center_orbit_id, max_center_orbits, width, cycle, max_cycle))

    def group_centers_guts(self):
        self.make_plus_sign()

        max_center_orbits = int((self.size - 3) / 2) - 2

        for center_orbit_id in range(max_center_orbits+1):
            width = self.size - 2 - ((max_center_orbits - center_orbit_id) * 2)
            max_cycle = int((width - 5)/2)

            for cycle in range(max_cycle+1):
                self.solve_inside_777(center_orbit_id, max_center_orbits, width, cycle, max_cycle)

        log.info("Centers are solved, %d steps in" % self.get_solution_len_minus_rotates(self.solution))
        self.print_cube()
