# -*- coding: utf-8 -*-
"""
/***************************************************************************
 UrbanRadioCober
                                 A QGIS plugin
 urban radiocober simulator plugin for omnidirectional radio coverage in urban enviroment
                             -------------------
        begin                : 2015-11-11
        copyright            : (C) 2015 by  Mario Salazar, Leonardo Cifuentes, Jhon Castaneda
        email                : dlcifuentesl@gmail.com, mario_salazarb@hotmail.com, jhonjaingambiental@gmail.com.
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load UrbanRadioCober class from file UrbanRadioCober.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .urban_radiocober import UrbanRadioCober
    return UrbanRadioCober(iface)
