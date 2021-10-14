# Authors: see git history
#
# Copyright (c) 2010 Authors
# Licensed under the GNU GPL version 3.0 or later.  See the file LICENSE for details.

import os
import sys
from os.path import dirname

from jinja2 import Environment, FileSystemLoader

_top_path = dirname(dirname(dirname(os.path.realpath(__file__))))
inx_path = os.path.join(_top_path, "inx")
template_path = os.path.join(_top_path, "templates")
version_path = _top_path


def build_environment():
    env = Environment(
        loader=FileSystemLoader(template_path),
        autoescape=True,
        extensions=['jinja2.ext.i18n']
    )

    with open(os.path.join(version_path, 'LICENSE'), 'r') as license:
        env.globals["inkstitch_license"] = "".join(license.readlines())

    if "BUILD" in os.environ:
        # building a ZIP release, with inkstitch packaged as a binary
        # About extension: add version information
        with open(os.path.join(version_path, 'VERSION'), 'r') as version:
            env.globals["inkstitch_version"] = "%s" % version.readline()
        # Command tag and icons path
        if sys.platform == "win32":
            env.globals["command_tag"] = '<command location="inx">../bin/inkstitch.exe</command>'
            env.globals["image_path"] = '../bin/icons/'
        elif sys.platform == "darwin":
            env.globals["command_tag"] = '<command location="inx">../../MacOS/inkstitch</command>'
            env.globals["image_path"] = '../../Resources/icons/'
        else:
            env.globals["command_tag"] = '<command location="inx">../bin/inkstitch</command>'
            env.globals["image_path"] = '../bin/icons/'
    else:
        # user is running inkstitch.py directly as a developer
        env.globals["command_tag"] = '<command location="inx" interpreter="python">../inkstitch.py</command>'
        env.globals["image_path"] = '../icons/'
        env.globals["inkstitch_version"] = "Manual Install"
    return env


def write_inx_file(name, contents):
    inx_file_name = "inkstitch_%s.inx" % name
    with open(os.path.join(inx_path, inx_file_name), 'w', encoding="utf-8") as inx_file:
        print(contents, file=inx_file)
