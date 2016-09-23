# ===============================================================================
# Copyright 2016 dgketchum
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance
# with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ===============================================================================

# =================================IMPORTS=======================================

from osgeo import gdal
import os
from numpy import array, zeros


def raster_array_raster():

    in_path = 'F:\ETRM_Inputs\PRISM\Precip\800m_std_all'
    tif = 'PRISMD2_NMHW2mi_20000102.tif'
    out_path = 'F:\ETRM_Results'
    out_raster = 'precip_plus_one.tif'

    dataset = gdal.Open(os.path.join(in_path, tif))

    band = dataset.GetRasterBand(1)

    raster_geo_dict = {'cols': dataset.RasterXSize, 'rows': dataset.RasterYSize, 'bands': dataset.RasterCount,
                       'data_type': band.DataType, 'projection': dataset.GetProjection(),
                       'geotransform': dataset.GetGeoTransform()}

    gdal_array = dataset.GetRasterBand(1).ReadAsArray()

    arr = array(gdal_array, dtype=float)

    zer = zeros(arr.shape)

    arr += 4.

    filename = os.path.join(out_path, out_raster)

    driver = gdal.GetDriverByName('GTiff')

    out_data_set = driver.Create(filename, raster_geo_dict['cols'], raster_geo_dict['rows'],
                                 raster_geo_dict['bands'], raster_geo_dict['data_type'])

    out_data_set.SetGeoTransform(raster_geo_dict['geotransform'])

    out_data_set.SetProjection(raster_geo_dict['projection'])

    output_band = out_data_set.GetRasterBand(1)

    output_band.WriteArray(arr, 0, 0)

if __name__ == '__main__':
    pass
# ==========================  EOF  ==============================================
