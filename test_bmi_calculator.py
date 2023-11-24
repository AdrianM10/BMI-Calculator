import pytest
from project import calculate_bmi, weight_status, get_height, get_weight, system_of_units


def mock_get_weight_kg(system_units):
    return 88

def mock_get_height_meters(system_units):
    return 1.92

def mock_get_weight_lbs(system_units):
    return 150

def mock_get_height_inches(system_units):
    return 65

def test_system_of_units(monkeypatch):
    # Mock the input function to always return 'metric'
    monkeypatch.setattr('builtins.input', lambda _: 'Metric')
    assert system_of_units() == 'metric'

    # Mock the input function to always return 'imperial'
    monkeypatch.setattr('builtins.input', lambda _: 'Imperial')
    assert system_of_units() == 'imperial'


def test_get_height(monkeypatch):
    # Mock the input function to check if height for metric is a float
    monkeypatch.setattr('builtins.input', mock_get_height_meters)
    system_units = 'metric'
    assert type(get_height(system_units)) is float
    # Mock get_height function and return height
    assert get_height(system_units) == 1.92

    # Mock the input function to check if height for imperial is a float
    monkeypatch.setattr('builtins.input', mock_get_height_inches)
    system_units = 'imperial'
    assert type(get_height(system_units)) is float
    # Mock get_height function and return height
    assert get_height(system_units) == 65



def test_get_weight(monkeypatch):
    # Mock the input function to check if weight for metric is a float
    monkeypatch.setattr('builtins.input', mock_get_weight_kg)
    system_units = 'metric'
    assert type(get_height(system_units)) is float
    # Mock get_weight function and return weight
    assert get_weight(system_units) == 88

    # Mock the input function to check if weight for imperial is a float
    monkeypatch.setattr('builtins.input', mock_get_weight_lbs)
    system_units = 'imperial'
    assert type(get_weight(system_units)) is float
    # Mock get_weight function and return weight
    assert get_weight(system_units) == 150


def test_calculate_bmi(monkeypatch):
    # Mock the metric return values of get_weight and get_height
    monkeypatch.setattr('project.get_weight', mock_get_weight_kg)
    monkeypatch.setattr('project.get_height', mock_get_height_meters)
    system_units = 'metric'
    assert round(calculate_bmi(system_units), 2) == 23.87

    # Mock the imperial return values of get_weight and get_height
    monkeypatch.setattr('project.get_weight', mock_get_weight_lbs)
    monkeypatch.setattr('project.get_height', mock_get_height_inches)
    system_units = 'imperial'
    assert round(calculate_bmi(system_units), 2) == 24.96

def test_weight_status(monkeypatch):
    # Mock the metric return values of get_weight and get_height
    monkeypatch.setattr('project.get_weight', mock_get_weight_kg)
    monkeypatch.setattr('project.get_height', mock_get_height_meters)
    system_units = 'metric'
    assert weight_status(system_units) == (23.87, 'healthy 😍')

    # Mock the imperial return values of get_weight and get_height
    monkeypatch.setattr('project.get_weight', mock_get_weight_lbs)
    monkeypatch.setattr('project.get_height', mock_get_height_inches)
    system_units = 'imperial'
    assert weight_status(system_units) == (24.96, 'obese 😭')
