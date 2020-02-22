import os

WORKING_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../data')

USERID = 608207320 # USERID in moss.standford.edu, to register check https://theory.stanford.edu/~aiken/moss/

MIN_LINES=10 # Only show matches (in check check plajiarism) with the number of the same line > MIN_LINES

MIN_PERCENT=90 # Only show matches (in check check plajiarism) with score of similarity > MIN_PERCENT

TRANSFORMER=r'.*' # A regular expression that is used to transform the name of them matched files.

NEW_SCORE=-1 # assign new score to cheating submission

VIRTUALIZATION=True # generate a picture?

TIMESLEEP = 1

DEFAULT_USERNAME='21431252KbjfGM'
DEFAULT_PASSWORD='4761032=<'

CODEFORCES_URI='https://codeforces.com'

GROUP_ID='Ir5CI6f3FD'

LOGIN_URL='https://codeforces.com/enter?back=%2F'

GROUP_URL='http://codeforces.com/group/Ir5CI6f3FD/contests'

STANDINGS_URL='http://codeforces.com/group/Ir5CI6f3FD/contest/{}/standings'

STATUS_URL='http://codeforces.com/group/Ir5CI6f3FD/contest/{}/status'

MEMBERS_URL='http://codeforces.com/group/Ir5CI6f3FD/members'

LANGUAGES = (
        "c",
        "cc",
        "java",
        "ml",
        "pascal",
        "ada",
        "lisp",
        "scheme",
        "haskell",
        "fortran",
        "ascii",
        "vhdl",
        "verilog",
        "perl",
        "matlab",
        "python",
        "mips",
        "prolog",
        "spice",
        "vb",
        "csharp",
        "modula2",
        "a8086",
        "javascript",
        "plsql")