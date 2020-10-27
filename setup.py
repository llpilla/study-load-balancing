"Setup file to install any missing Python3 packages if needed"

try:
    import matplotlib
except ImportError:
    import pip
    pip(['install', '--user', 'matplotlib'])
