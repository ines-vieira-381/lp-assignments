from life_expectancy.regions import Regions

def test_actual_countries(possible_regions):
    """
    Test the actual_countries method of the Regions enum.
    """
    assert sorted(Regions.verify_regions()) == possible_regions
    