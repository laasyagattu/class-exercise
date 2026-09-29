import logging

logger = logging.getLogger(__name__)


def show_overview(df):
    """Display basic information about a DataFrame."""
    # TODO 1:
    # Log a DEBUG message containing the shape.
    # Print the shape, first five rows, column names, and data types.
    logger.debug(f"DataFrame is {df.shape} large")
    print(df.shape)
    print(df.head(5))
    print(df.columns) 
    print(df.dtypes)
    return df 


def remove_duplicates(df):
    """Remove exact duplicate rows."""
    # TODO 2:
    # Remove exact duplicate rows.
    # Log a DEBUG message containing the before and after row counts.
    # Return the resulting DataFrame.
    before = df.copy()
    df = df.drop_duplicates()
    logger.debug(f"DataFrame initial row count: {len(before)} \n after removing duplicates row count: {len(df)}")
    return df


def drop_missing_rows(df):
    """Remove rows containing missing values."""
    # TODO 3:
    # Drop rows containing one or more missing values.
    # Log a DEBUG message containing the before and after row counts.
    # Return the resulting DataFrame.
    before = df.copy()
    df = df.dropna()
    logger.debug(f"DataFrame initial row count: {len(before)} \n after dropping missing row count: {len(df)}")
    return df
