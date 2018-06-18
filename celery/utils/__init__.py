# -*- coding: utf-8 -*-
"""Utility functions.

Don't import from here directly anymore, as these are only
here for backwards compatibility.
"""
from __future__ import absolute_import, print_function, unicode_literals
from celery.utils.functional import memoize  # noqa
from celery.utils.nodenames import worker_direct, nodename, nodesplit

__all__ = ('worker_direct', 'gen_task_name', 'nodename', 'nodesplit',
           'cached_property', 'uuid')

# ------------------------------------------------------------------------ #
# > XXX Compat
from celery.utils.log import LOG_LEVELS     # noqa
from celery.utils.imports import (          # noqa
    qualname as get_full_cls_name, symbol_by_name as get_cls_by_name,
    instantiate, import_from_cwd, gen_task_name,
)
from celery.utils.functional import chunks, noop        # noqa
from kombu.utils.objects import cached_property         # noqa
from kombu.utils.uuid import uuid   # noqa
gen_unique_id = uuid
