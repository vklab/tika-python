#!/usr/bin/env python3
from subprocess import call


if __name__ == "__main__":
    call(["vklabs_pypi", "publish-package", "."])
