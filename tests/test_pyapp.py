"""
Test suite for PyApp.
"""

from pyapp import PyApp


class TestPyApp:
    """Test suite for PyApp class."""

    def test_creation(self, app):
        """Test app creation."""
        assert isinstance(app, PyApp) is True

    def test_run(self, app):
        """Test the capability of doing something really wonderful."""
        result = app.run()
        assert result == "Doing something wonderful... done!"
