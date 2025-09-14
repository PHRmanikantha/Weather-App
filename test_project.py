import pytest
from project import kelvin_to_celsius, format_weather, get_weather, display_weather

def test_kelvin_to_celsius():
    assert kelvin_to_celsius(300) == 26.85
    assert kelvin_to_celsius(273.15) == 0.0
    assert kelvin_to_celsius(310) == 36.85

def test_format_weather():
    sample_data = {
        "name": "Hyderabad",
        "sys": {"country": "IN"},
        "weather": [{"description": "clear sky"}],
        "main": {"temp": 30, "humidity": 40},
        "wind": {"speed": 5},
    }
    result = format_weather(sample_data)
    assert result["location"] == "Hyderabad, IN"
    assert result["condition"] == "Clear Sky"
    assert result["temperature"] == 30
    assert result["humidity"] == 40
    assert result["wind_speed"] == 5

def test_get_weather_invalid_city(monkeypatch):
    """Simulate invalid API response for city."""
    class MockResponse:
        def json(self):
            return {"cod": "404", "message": "city not found"}
    def mock_get(*args, **kwargs):
        return MockResponse()

    monkeypatch.setattr("requests.get", mock_get)
    result = get_weather("InvalidCity")
    assert result is None  # should return None for invalid city

def test_display_weather(capsys):
    """Check that display_weather prints correct output."""
    info = {
        "location": "Hyderabad, IN",
        "condition": "Clear Sky",
        "temperature": 30,
        "humidity": 40,
        "wind_speed": 5,
    }
    display_weather(info)
    captured = capsys.readouterr()
    assert "Hyderabad, IN" in captured.out
    assert "Clear Sky" in captured.out
    assert "30C" in captured.out
