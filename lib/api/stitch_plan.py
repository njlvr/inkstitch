# Authors: see git history
#
# Copyright (c) 2010 Authors
# Licensed under the GNU GPL version 3.0 or later.  See the file LICENSE for details.

from flask import Blueprint, g, jsonify

from ..stitch_plan import stitch_groups_to_stitch_plan


stitch_plan = Blueprint('stitch_plan', __name__)


@stitch_plan.route('')
def get_stitch_plan():
    if not g.extension.get_elements():
        return dict(colors=[], stitch_blocks=[], commands=[])

    metadata = g.extension.get_inkstitch_metadata()
    collapse_len = metadata['collapse_len_mm']
    patches = g.extension.elements_to_stitch_groups(g.extension.elements)
    stitch_plan = stitch_groups_to_stitch_plan(patches, collapse_len=collapse_len)

    return jsonify(stitch_plan)
