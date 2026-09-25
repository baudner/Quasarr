# -*- coding: utf-8 -*-

import unittest

from quasarr.constants import (
    TIMEOUT_SLOW_MODE_DEFAULT_MULTIPLIER,
    _read_slow_mode_multiplier,
)


class ReadSlowModeMultiplierTests(unittest.TestCase):
    def test_unset_uses_default(self):
        self.assertEqual(
            _read_slow_mode_multiplier(None), TIMEOUT_SLOW_MODE_DEFAULT_MULTIPLIER
        )

    def test_valid_value_is_used(self):
        self.assertEqual(_read_slow_mode_multiplier("6"), 6)
        self.assertEqual(_read_slow_mode_multiplier(" 4 "), 4)

    def test_invalid_values_fall_back_to_default(self):
        for value in ("", "abc", "2.5", "0", "-3"):
            with self.subTest(value=value):
                self.assertEqual(
                    _read_slow_mode_multiplier(value),
                    TIMEOUT_SLOW_MODE_DEFAULT_MULTIPLIER,
                )


if __name__ == "__main__":
    unittest.main()
