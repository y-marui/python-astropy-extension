import astropy.units as u
import matplotlib.pyplot as plt
import numpy as np

from astropy_extension.visualization import labeled_quantity_support


def test_labeled_quantity_support_simple():
    x = np.linspace(0, 2 * np.pi, 100) * u.rad
    y = np.sin(x) * u.V

    with labeled_quantity_support("Angle", "Volt"):
        plt.plot(x, y)

    ax = plt.gca()
    xlabel = ax.get_xlabel()
    ylabel = ax.get_ylabel()
    plt.close()

    assert xlabel == "Angle ($\\mathrm{rad}$)"
    assert ylabel == "Volt ($\\mathrm{V}$)"


# def test_labeled_quantity_support_exp():
#     x = np.linspace(0, 2*np.pi, 100) * u.Unit(u.rad)
#     y = np.sin(x) * u.Unit(1e-6 * u.V)

#     with labeled_quantity_support("Angle", "Volt"):
#         plt.plot(x, y)

#     ax = plt.gca()
#     xlabel = ax.get_xlabel()
#     ylabel = ax.get_ylabel()
#     plt.close()

#     assert xlabel == 'Angle ($\\mathrm{rad}$)'
#     assert ylabel == 'Volt ($\\mathrm{10^{-6}\\,V}$)'

# def test_labeled_quantity_support_exp_no1():
#     x = np.linspace(0, 2*np.pi, 100) * u.Unit(u.rad)
#     y = np.sin(x) * u.Unit(1e-6 / u.V)

#     with labeled_quantity_support("Angle", "Volt"):
#         plt.plot(x, y)

#     ax = plt.gca()
#     xlabel = ax.get_xlabel()
#     ylabel = ax.get_ylabel()
#     plt.close()

#     assert xlabel == 'Angle ($\\mathrm{rad}$)'
#     assert ylabel == 'Volt ($\\mathrm{10^{-6}\\,/V}$)'
