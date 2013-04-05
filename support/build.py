"""
Relocates the files for a given version of Isotope from vendor/isotope
into a Django app for use with Django staticfiles.
"""
import subprocess
import sys

PACKAGE_NAME = 'enquirejs'

STATIC_DIR = "{0}/static/{0}".format(PACKAGE_NAME)
DEFAULT_VERSION = 'master'
GIT_REPO = 'https://raw.github.com/WickyNilliams/enquire.js'
GIT_TAG = DEFAULT_VERSION
SRC_LIST = (
    'dist/enquire.js',
    'dist/enquire.min.js',
)


def wget(src):
    cmd = [
        "cd {0} && wget -N {1}/{2}/{3}".format(
            STATIC_DIR, GIT_REPO, GIT_TAG, src),
    ]
    subprocess.call(cmd, shell=True)


def main():
    global GIT_TAG  # XXX

    options = {
        "version": 'master' if len(sys.argv) is 1 else sys.argv[1],
    }
    version = options['version']
    if version == DEFAULT_VERSION:
        print "No version specified, using '{0}'".format(version)
    else:
        GIT_TAG = 'v{0}'.format(version)

    # make sure static directory exists
    subprocess.call(["mkdir -p {0}".format(STATIC_DIR)], shell=True)

    # copy files
    for src_path in SRC_LIST:
        wget(src_path)

    # update package VERSION meta
    with open("./VERSION", "w") as f:
        version = options['version']
        f.write('dev' if version == DEFAULT_VERSION else version)


if __name__ == "__main__":
    main()
