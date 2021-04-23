import logging

from qgis.core import QgsMapLayer

from ..qgis_plugin_tools.tools.custom_logging import bar_msg
from ..qgis_plugin_tools.tools.decorations import log_if_fails
from ..qgis_plugin_tools.tools.exceptions import QgsPluginException
from ..qgis_plugin_tools.tools.i18n import tr
from ..qgis_plugin_tools.tools.resources import plugin_name

LOGGER = logging.getLogger(plugin_name())


class Printer:
    @log_if_fails
    def print_layer_name(self, layer: QgsMapLayer) -> None:

        try:
            LOGGER.info(
                tr("Printing layer name"),
                extra=bar_msg(tr("Layer name is {}", layer.name())),
            )
        except ValueError:
            raise QgsPluginException("Error occurred", bar_msg("Select layer first!"))
