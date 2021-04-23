# from .qgis_plugin_tools.infrastructure.debugging import setup_pydevd


# if os.environ.get('QGIS_PLUGIN_USE_DEBUGGER') == 'pydevd':
#     if os.environ.get('IN_TESTS', "0") != "1" and os.environ.get('QGIS_PLUGIN_IN_CI', "0") != "1": # noqa
#         setup_pydevd()
from qgis.gui import QgisInterface


def classFactory(iface: QgisInterface):  # noqa: N802 ANN201
    from .plugin import Plugin

    return Plugin(iface)
