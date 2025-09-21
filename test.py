from copy import deepcopy
import random
import sys

# Face order: U, R, F, D, L, B
FACE_NAMES = ['U', 'R', 'F', 'D', 'L', 'B']

# Colors (single-letter) for printing
COLORS = {
    'U': 'W',  # White
    'R': 'R',  # Red
    'F': 'G',  # Green
    'D': 'Y',  # Yellow
    'L': 'O',  # Orange
    'B': 'B',  # Blue
}

class Cube:
    def __init__(self):
        # Each face is a 3x3 list of color chars
        self.faces = {f: [[COLORS[f] for _ in range(3)] for _ in range(3)] for f in FACE_NAMES}

    def copy(self):
        c = Cube()
        c.faces = deepcopy(self.faces)
        return c

    def reset(self):
        self.__init__()

    # Utility: rotate a 3x3 matrix clockwise n times (n can be 1, 2, 3)
    @staticmethod
    def _rotate_face(face, n=1):
        m = deepcopy(face)
        n = n % 4
        for _ in range(n):
            m = [list(row) for row in zip(*m[::-1])]
        return m

    # Apply move by name (e.g. "R", "U'", "F2")
    def move(self, mv: str):
        mv = mv.strip()
        if mv == '':
            return
        # parse move
        base = mv[0]
        if base not in FACE_NAMES:
            raise ValueError(f"Unknown move: {mv}")
        suffix = mv[1:] if len(mv) > 1 else ''
        times = 1
        if suffix == "'":
            times = 3
        elif suffix == '2':
            times = 2
        elif suffix == '':
            times = 1
        else:
            raise ValueError(f"Unknown move suffix in {mv}")

        for _ in range(times):
            getattr(self, f'_move_{base}')()

    def apply_algorithm(self, alg: str):
        """Apply a sequence of moves separated by spaces, e.g. "R U R' U'"""
        tokens = [t for t in alg.strip().split() if t]
        for t in tokens:
            self.move(t)

    # The following implement the single clockwise turn for each face.
    # Each updates the face rotation and cycles the edge strips of adjacent faces.

    def _move_U(self):
        # Rotate U face clockwise
        self.faces['U'] = self._rotate_face(self.faces['U'], 1)
        # cycle the top rows of (F, R, B, L)
        F, R, B, L = self.faces['F'], self.faces['R'], self.faces['B'], self.faces['L']
        F_row = F[0][:]
        R_row = R[0][:]
        B_row = B[0][:]
        L_row = L[0][:]
        F[0], R[0], B[0], L[0] = R_row, B_row, L_row, F_row

    def _move_D(self):
        self.faces['D'] = self._rotate_face(self.faces['D'], 1)
        # cycle bottom rows of (F, L, B, R) but in opposite orientation compared to U
        F, L, B, R = self.faces['F'], self.faces['L'], self.faces['B'], self.faces['R']
        F_row = F[2][:]
        L_row = L[2][:]
        B_row = B[2][:]
        R_row = R[2][:]
        F[2], L[2], B[2], R[2] = L_row, B_row, R_row, F_row

    def _move_R(self):
        self.faces['R'] = self._rotate_face(self.faces['R'], 1)
        U, F, D, B = self.faces['U'], self.faces['F'], self.faces['D'], self.faces['B']
        # Save right column of U, F, D, and left column of B (note B is upside-down)
        u_col = [U[i][2] for i in range(3)]
        f_col = [F[i][2] for i in range(3)]
        d_col = [D[i][2] for i in range(3)]
        b_col = [B[2 - i][0] for i in range(3)]  # reversed
        # Assign
        for i in range(3):
            F[i][2] = u_col[i]
            D[i][2] = f_col[i]
            B[2 - i][0] = d_col[i]
            U[i][2] = b_col[i]

    def _move_L(self):
        self.faces['L'] = self._rotate_face(self.faces['L'], 1)
        U, F, D, B = self.faces['U'], self.faces['F'], self.faces['D'], self.faces['B']
        u_col = [U[i][0] for i in range(3)]
        f_col = [F[i][0] for i in range(3)]
        d_col = [D[i][0] for i in range(3)]
        b_col = [B[2 - i][2] for i in range(3)]  # reversed
        for i in range(3):
            F[i][0] = d_col[i]
            D[i][0] = b_col[i]
            B[2 - i][2] = u_col[i]
            U[i][0] = f_col[i]

    def _move_F(self):
        self.faces['F'] = self._rotate_face(self.faces['F'], 1)
        U, R, D, L = self.faces['U'], self.faces['R'], self.faces['D'], self.faces['L']
        # Save bottom row of U, left column of R, top row of D, right column of L
        u_row = U[2][:]
        r_col = [R[i][0] for i in range(3)]
        d_row = D[0][:]
        l_col = [L[i][2] for i in range(3)]
        # Assign (careful with orientations)
        for i in range(3):
            R[i][0] = u_row[2 - i]
            D[0][i] = r_col[i]
            L[i][2] = d_row[2 - i]
            U[2][i] = l_col[i]

    def _move_B(self):
        self.faces['B'] = self._rotate_face(self.faces['B'], 1)
        U, R, D, L = self.faces['U'], self.faces['R'], self.faces['D'], self.faces['L']
        u_row = U[0][:]
        r_col = [R[i][2] for i in range(3)]
        d_row = D[2][:]
        l_col = [L[i][0] for i in range(3)]
        for i in range(3):
            R[i][2] = d_row[2 - i]
            D[2][i] = l_col[i]
            L[i][0] = u_row[2 - i]
            U[0][i] = r_col[i]

    # Helpers
    def is_solved(self):
        return all(len({self.faces[f][r][c] for r in range(3) for c in range(3)}) == 1 for f in FACE_NAMES)

    def scramble(self, moves=20):
        basic = ['U', 'D', 'L', 'R', 'F', 'B']
        suffixes = ['', "'", '2']
        seq = []
        for _ in range(moves):
            m = random.choice(basic) + random.choice(suffixes)
            seq.append(m)
            self.move(m)
        return ' '.join(seq)

    def __str__(self):
        return self.render_text()

    def render_text(self):
        # Unfolded cube net (simple ASCII) - using single letters for colors
        U = self.faces['U']
        R = self.faces['R']
        F = self.faces['F']
        D = self.faces['D']
        L = self.faces['L']
        B = self.faces['B']
        lines = []

        for r in range(3):
            lines.append('      ' + ' '.join(B[r]))
        # Top (U)
        for r in range(3):
            lines.append('      ' + ' '.join(U[r]))
        # Middle (L F R B)
        for r in range(3):
            lines.append(' '.join(L[r]) + '   ' + ' '.join(F[r]) + '   ' + ' '.join(R[r]) + '   ' + ' '.join(B[r]))
        # Bottom (D)
        for r in range(3):
            lines.append('      ' + ' '.join(D[r]))
        return '\n'.join(lines)


# Small BFS solver (naive) for demonstration only.
# WARNING: This only finds solutions for states within the given depth limit.
# Do not expect it to solve general scrambles (full cube God's number ~20).

def bfs_solve(start_cube: Cube, max_depth=6):
    from collections import deque
    moves = [f for f in FACE_NAMES]
    suffixes = ['', "'", '2']
    moves_all = [m + s for m in moves for s in suffixes]

    if start_cube.is_solved():
        return ''

    seen = set()
    def cube_key(c: Cube):
        return tuple(''.join(''.join(row) for row in c.faces[f]) for f in FACE_NAMES)

    q = deque()
    q.append((start_cube.copy(), []))
    seen.add(cube_key(start_cube))

    while q:
        cube, seq = q.popleft()
        if len(seq) >= max_depth:
            continue
        for m in moves_all:
            c2 = cube.copy()
            c2.move(m)
            k = cube_key(c2)
            if k in seen:
                continue
            if c2.is_solved():
                return ' '.join(seq + [m])
            seen.add(k)
            q.append((c2, seq + [m]))
    return None


# Simple CLI
def repl():
    c = Cube()
    print("Rubik's Cube simulator. Type 'help' for commands.")
    while True:
        try:
            inp = input('> ').strip()
        except (EOFError, KeyboardInterrupt):
            print('\nBye')
            return
        if not inp:
            continue
        cmd, *rest = inp.split(maxsplit=1)
        arg = rest[0] if rest else ''
        cmd = cmd.lower()
        if cmd in ('exit', 'quit', 'q'):
            print('Bye')
            return
        elif cmd == 'help':
            print("Commands:\n  show                 - print cube\n  move <alg>          - apply algorithm, e.g. move R U R' U'\n  moves <alg>         - same as move\n  scramble [n]        - scramble with n random moves (default 20)\n  reset               - reset to solved\n  solved?             - check solved\n  bfs [maxdepth]      - try naive BFS solve (maxdepth default 6)\n  exit/quit           - quit")
        elif cmd in ('show', 'display'):
            print(c)
        elif cmd in ('move', 'moves'):
            if not arg:
                print("Provide moves, e.g. move R U R' U'")
                continue
            try:
                c.apply_algorithm(arg)
            except Exception as e:
                print('Error applying moves:', e)
        elif cmd == 'scramble':
            n = 20
            if arg:
                try:
                    n = int(arg)
                except:
                    print('Invalid number; using 20')
            seq = c.scramble(n)
            print('Scramble:', seq)
        elif cmd == 'reset':
            c.reset()
            print('Reset to solved')
        elif cmd in ('solved?', 'issolved', 'is_solved'):
            print('Solved' if c.is_solved() else 'Not solved')
        elif cmd == 'bfs':
            depth = 6
            if arg:
                try:
                    depth = int(arg)
                except:
                    print('Invalid depth; using 6')
            print(f'Trying BFS up to depth {depth} (may be slow)')
            sol = bfs_solve(c, max_depth=depth)
            if sol is None:
                print('No solution found within depth', depth)
            else:
                print('Solution:', sol)
        else:
            # allow direct move sequences without 'move' keyword
            # e.g. "R U R' U'"
            try:
                c.apply_algorithm(inp)
            except Exception as e:
                print('Unknown command or invalid moves. Type help for commands.')


if __name__ == '__main__':
    repl()
