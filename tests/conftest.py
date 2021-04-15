"""
The `conftest.py` file serves as a means of providing fixtures for an entire
directory. Fixtures defined in a conftest.py can be used by any test in that
package without needing to import them (pytest will automatically discover
them).

See: https://pytest.org/en/latest/reference/fixtures.html
"""

import pytest
from pyapp import PyApp


@pytest.fixture
def app():
    """Return a PyApp instance."""
    return PyApp()
