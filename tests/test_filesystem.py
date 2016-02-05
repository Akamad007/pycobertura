import mock
import pytest


def test_filesystem_directory__file_not_found():
    from pycobertura.filesystem import DirectoryFileSystem

    fs = DirectoryFileSystem('foo/bar/baz')

    expected_filepaths = {
        'Main.java': 'foo/bar/baz/Main.java',
        'search/BinarySearch.java': 'foo/bar/baz/search/BinarySearch.java',
        'search/ISortedArraySearch.java': 'foo/bar/baz/search/ISortedArraySearch.java',
        'search/LinearSearch.java': 'foo/bar/baz/search/LinearSearch.java',
    }

    for filename in expected_filepaths:
        try:
            with fs.open(filename) as f:
                pass
        except DirectoryFileSystem.FileNotFound as fnf:
            assert fnf.path == expected_filepaths[filename]


def test_filesystem_directory__returns_fileobject():
    from pycobertura.filesystem import DirectoryFileSystem

    fs = DirectoryFileSystem('tests/dummy')

    expected_filepaths = {
        'dummy/dummy.py': 'dummy/dummy/dummy.py',
    }

    for filename in expected_filepaths:
        with fs.open(filename) as f:
            assert hasattr(f, 'read')
