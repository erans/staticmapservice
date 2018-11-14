# Configuration file of staticmapservice

TILE_SERVER = 'http://a.tile.osm.org/{z}/{x}/{y}.png'
IS_TMS = False

# Default values can be overwritten in each request
DEFAULT_WIDTH = '300'
DEFAULT_HEIGHT = '200'
DEFAULT_ZOOM = '10'

# Maximum values can't be overwritten
MAX_WIDTH = '800'
MAX_HEIGHT = '800'
MAX_ZOOM = '19'
MAX_PNV = '30' # Map won't contain more points, nodes and vertices than this value