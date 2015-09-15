#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Jason Juang
# Copyright (c) 2015 Jason Juang
#
# License: MIT
#

"""This module exports the cmakelint plugin class."""

from SublimeLinter.lint import Linter, util


class cmakelint(Linter):

    """Provides an interface to cmakelint."""

    syntax = 'cmake'
    cmd = ('cmakelint', '*', '@')
    regex = r'^.+:(?P<line>\d+):\s+(?P<message>.+)'
    tempfile_suffix = '-'
    error_stream = util.STREAM_BOTH  # errors are on stderr
    comment_re = r'\s*/[/*]'
    inline_settings = None
    inline_overrides = 'filter'

    def split_match(self, match):
        """Extract and return values from match."""
        (match, line, col, error,
            warning, message, near) = super().split_match(match)

        if line is not None and line == -1 and message:
            line = 0

        return match, line, col, error, warning, message, near
