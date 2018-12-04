#!/usr/bin/python3
import os, sys, urllib.parse


if __name__ == '__main__':
    url = sys.argv[1] if len(sys.argv) > 1 else os.environ['QUTE_URL']
    pattern = '*.{}/*'.format(urllib.parse.urlparse(url)[1])

    patterns_path = os.path.join(os.environ['QUTE_CONFIG_DIR'],
                                 'javascript_enabled_patterns.txt')
    with open(patterns_path, 'a') as patterns:
        patterns.write(pattern + '\n')

    with open(os.environ['QUTE_FIFO'], 'w') as fifo:
        fifo.write('set --pattern {} content.javascript.enabled '
                   'true\n'.format(pattern))
        fifo.write('reload\n')
