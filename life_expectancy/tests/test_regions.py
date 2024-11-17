from life_expectancy.regions import Regions

def test_actual_countries():
    """
    Test the actual_countries method of the Regions enum.
    """
    expected_countries = [
        "AL", "AM", "AT", "AZ", "BE", "BG", "BY", "CH", "CY", "CZ", 
        "DE", "DK", "EE", "EL", "ES", "FI", "FR", "FX", "GE", "HR", 
        "HU", "IE", "IS", "IT", "LI", "LT", "LU", "LV", "MD", "ME", 
        "MK", "MT", "NL", "NO", "PL", "PT", "RO", "RS", "RU", "SE", 
        "SI", "SK", "SM", "TR", "UA", "UK", "XK"
    ]
    assert sorted(Regions.verify_regions()) == sorted(expected_countries)
    