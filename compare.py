import sys
import filecmp
from filecmp import dircmp

# compares files in directories
# how to use this script: compare.py [directory A] [directory B]
if len(sys.argv) == 3:
    result = filecmp.dircmp(sys.argv[1], sys.argv[2])
    common = result.common

    if len(common) >= 1:
        print(result.same_files)
    else:
        print(result.report())