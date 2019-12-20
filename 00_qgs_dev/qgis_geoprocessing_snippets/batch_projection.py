
from qgis.core import *
from qgis.gui import *
save_dir = 'your_data_path'

layer = QgsVectorLayer(save_dir, "Track", "ogr")
crs = crs.createFromId(3857)
layer.setCrs(crs)
QgsMapLayerRegistry.instance().addMapLayer(layer)