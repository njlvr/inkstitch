# Authors: see git history
#
# Copyright (c) 2010 Authors
# Licensed under the GNU GPL version 3.0 or later.  See the file LICENSE for details.

from .utils import build_environment, write_inx_file


def generate_info_inx_files():
    env = build_environment()
    info_inx_files = ['about']
    for info in info_inx_files:
        template = env.get_template('%s.xml' % info)
        write_inx_file(info, template.render())
