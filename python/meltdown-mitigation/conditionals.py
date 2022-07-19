"""Functions to prevent a nuclear meltdown."""


def is_criticality_balanced(temperature, neutrons_emitted):
    """
    It measures if things are critically balanced
    """
    temp_neutrons_product = temperature * neutrons_emitted

    if temperature < 800 and neutrons_emitted > 500 and temp_neutrons_product < 500000:
        return True
    return False


def reactor_efficiency(voltage, current, theoretical_max_power):
    """
    Assess reactor efficiency zone
    """
    efficiency = ((voltage * current) / theoretical_max_power) * 100

    if efficiency >= 80:
        return "green"
    if efficiency < 80 and efficiency >= 60:
        return "orange"
    if efficiency < 60 and efficiency >= 30:
        return "red"
    return "black"


def fail_safe(temperature, neutrons_produced_per_second, threshold):
    """
    Assess and return status code for the reactor
    the ratio of the the percentage of the threshold is measured
    the ratio is measured and that is used to determine the level
    """
    total_val = temperature * neutrons_produced_per_second
    ratio = total_val / threshold
    if ratio < 0.9:
        return "LOW"
    elif ratio <= 1.1:
        return "NORMAL"
    return "DANGER"
