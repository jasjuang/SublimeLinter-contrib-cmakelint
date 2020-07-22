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

import sublime
from SublimeLinter.lint import Linter, util

# Settings file locations.
settings_file = 'cmakelinter.sublime-settings'
custom_style_settings = 'cmakelinter_custom.sublime-settings'


def load_settings():
    """Load settings and put their values into global scope."""

    # We set these globals.
    global filter_

    settings_global = sublime.load_settings(settings_file)
    settings_local = sublime.active_window(
    ).active_view().settings().get('CMakeLinter', {})

    def load(name, default): return settings_local.get(
        name, settings_global.get(name, default))
    # Load settings, with defaults.
    filter_ = load('filter', "")


class cmakelint(Linter):
    """Provides an interface to cmakelint."""

    defaults = {
        'selector': 'source.cmake'
    }

    def cmd(self):
        """Command for linter."""

        load_settings()
        return ('cmakelint', '--filter=+,' + filter_, '*', '@')

    regex = r'^.+:(?P<line>\d+):\s+(?P<message>.+)'
    tempfile_suffix = '-'
    error_stream = util.STREAM_BOTH  # errors are on stderr

    def split_match(self, match):
        """Extract and return values from match."""
        print("split match", self.cmd)
        (match, line, col, error,
            warning, message, near) = super().split_match(match)

        if line is not None and line == -1 and message:
            line = 0

        return match, line, col, error, warning, message, near
