import sys
import os

# config your working folder and the correponding folder
WORK_DIR = '/home/nikolaos.alexopoulos/PROJECTS/SZZ/V-SZZ/ICSE2022ReplicationPackage'

REPOS_DIR = '/home/nikolaos.alexopoulos/PROJECTS/SZZ/repo-directory/nikos'

DATA_FOLDER = os.path.join(WORK_DIR, 'data')

SZZ_FOLDER = os.path.join(WORK_DIR, 'icse2021-szz-replication-package')

DEFAULT_MAX_CHANGE_SIZE = sys.maxsize

AST_MAP_PATH = os.path.join(WORK_DIR, 'ASTMapEval_jar')

LOG_DIR = os.path.join(WORK_DIR, 'GitLogs')
