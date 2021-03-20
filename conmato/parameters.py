import os
import yaml

WORKING_DIR = os.path.join(os.path.dirname(
    os.path.abspath(__file__)), '../data')

LOGGING_FILE = os.path.join(WORKING_DIR, 'logs/build.log')
SESSION_FILE = os.path.join(WORKING_DIR, 'session/session.pkl')
DEFAULT_CONFIG_FILE = 'conmato/default_config.yaml'
USER_CONFIG_FILE = 'conmato/user_config.yaml'

# # USERID in moss.standford.edu, to register check https://theory.stanford.edu/~aiken/moss/
# USERID = 203062946

# # Only show matches (in check check plajiarism) with the number of the same line > MIN_LINES
# MIN_LINES = 10


# # Only show matches (in check check plajiarism) with score of similarity > MIN_PERCENT
# MIN_PERCENT = 90

# # A regular expression that is used to transform the name of them matched files.
# TRANSFORMER = r'.*'

# NEW_SCORE = -1  # assign new score to cheating submission

# VIRTUALIZATION = True  # generate a picture?

# USER_FORMAT = r'^[0-9]{8,10}[A-Za-z]{4,10}$'

# TIMESLEEP = 1

# DEFAULT_USERNAME = '21431252KbjfGM'
# DEFAULT_PASSWORD = '4761032=<'
# USER_KEY = '757e4de2c3d19ff5a823003bbfa108aaab96d834' # get key and sceret here http://codeforces.com/settings/api
# USER_SECRET = '12872454ac44ec1bc0ada71a12bf186397ee7438'

# GROUP_ID = 'Ir5CI6f3FD'

with open(DEFAULT_CONFIG_FILE) as file:
    config = yaml.full_load(file)
GROUP_ID = config['group_id']
USERID = config['userid']
MIN_LINES = config['min_lines']
MIN_PERCENT = config['min_percent']
TRANSFORMER = config['transformer']
NEW_SCORE = config['new_score']
VIRTUALIZATION = config['virtualization']
USER_FORMAT = config['user_format']
TIMESLEEP = config['timesleep']
DEFAULT_USERNAME = config['default_username']
DEFAULT_PASSWORD = config['default_password']
USER_KEY = config['user_key']
USER_SECRET = config['user_secret']

with open(USER_CONFIG_FILE) as file:
    config = yaml.full_load(file)
if config:
    if 'group_id' in config:
        GROUP_ID = config['group_id']
    if 'userid' in config:
        USERID = config['userid']
    if 'min_lines' in config:
        MIN_LINES = config['min_lines']
    if 'min_percent' in config:
        MIN_PERCENT = config['min_percent']
    if 'transformer' in config:
        TRANSFORMER = config['transformer']
    if 'new_score' in config:
        NEW_SCORE = config['new_score']
    # if 'virtualization' in config:
    #     VIRTUALIZATION = config['virtualization']
    # if 'user_format' in config:
    #     USER_FORMAT = config['user_format']
    if 'timesleep' in config:
        TIMESLEEP = config['timesleep']
    if 'default_username' in config:
        DEFAULT_USERNAME = config['default_username']
    if 'default_password' in config:
        DEFAULT_PASSWORD = config['default_password']
    if 'user_key' in config:
        USER_KEY = config['user_key']
    if 'user_secret' in config:
        USER_SECRET = config['user_secret']

CODEFORCES_URI = 'https://codeforces.com'

LOGIN_URL = 'https://codeforces.com/enter?back=%2F'

GROUP_URL = 'http://codeforces.com/group/{}/contests'

DATA_URL = 'http://codeforces.com/group/{}/data'

STANDINGS_URL = 'http://codeforces.com/group/{}/contest/{}/standings'

STATUS_URL = 'http://codeforces.com/group/{}/contest/{}/status'

MEMBERS_URL = 'http://codeforces.com/group/{}/members'

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
