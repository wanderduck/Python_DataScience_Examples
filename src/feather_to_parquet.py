"""
Helper function to quickly convert feather format to parquet format when using cudf.

This function may become unnecessary in the future, but for now, cudf, because of
current limitations with pyarrow, cannot load and read feather files on the GPU.
This creates a data bottleneck. To prevent this bottleneck, the feather file is
converted to a parquet file, which cudf can load and read on the GPU.
"""


def check_for_pyarrow() -> bool:
    """Check if user has pyarrow installed."""
    try:
        import pyarrow.feather
        import pyarrow.parquet
        print('Required package "pyarrow" was found.\nProceeding with file conversion')
        return True
    except ImportError:
        print(
            'ERROR: The package "pyarrow" is not installed.\n'
            'Please install the "pyarrow" package by running "pip install pyarrow"\n'
            'To see your currently installed packages, run "pip list"\n'
            'To check for "pyarrow" specifically, run "pip show pyarrow"'
        )
        raise ImportError('Required package "pyarrow" is not installed or cannot be found.')


def feather_to_parquet(feather_path: str, parquet_path: str) -> None:
    """
    Convert feather file format to parquet file format with the pyarrow library.

    Args:
        feather_path: Path from which to load the feather file
        parquet_path: Path to which to save the parquet file
    """
    import pyarrow.feather as feather
    import pyarrow.parquet as pq

    feather_table = feather.read_table(feather_path)
    pq.write_table(feather_table, parquet_path)
    print('File conversion complete.')


def main() -> None:
    """Main entry point for interactive feather to parquet conversion."""
    if check_for_pyarrow():
        feather_path = input('Please enter path from which to LOAD feather file: ')
        parquet_path = input('Please enter path to which to SAVE parquet file: ')
        feather_to_parquet(feather_path, parquet_path)


if __name__ == '__main__':
    main()
