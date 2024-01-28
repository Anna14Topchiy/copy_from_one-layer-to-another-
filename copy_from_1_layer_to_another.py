import geopandas as gpd

def copy_data_between_shapefiles(source_path, target_path, output_path):
    # Чтение данных из исходного SHP-файла
    source_gdf = gpd.read_file(source_path)

    # If you want to completely replace the target shapefile, just use the source data
    updated_target_gdf = source_gdf.copy()

    # Заполнение колонки 'feature' значением 'TL' для всех скопированных данных
    updated_target_gdf['feature'] = 'TL'

    # Сохранение изменений в новый SHP-файл
    updated_target_gdf.to_file(output_path, driver='ESRI Shapefile')

if __name__ == "__main__":
    # Укажите пути к вашим SHP-файлам
    source_path = r'C:\Users\annat\OneDrive\kasko\source_preparation_for_each_country\NL\scrip_snap_points_to_line\snapped_points\snapped_tl.shp'
    target_path = r'C:\Users\annat\OneDrive\kasko\source_preparation_for_each_country\NL\scrip_snap_points_to_line\snapped_points\tl_for_bd.shp'
    output_path = r'C:\Users\annat\OneDrive\kasko\source_preparation_for_each_country\NL\scrip_snap_points_to_line\snapped_points\nl_traffic_lights.shp'

    # Вызов функции для копирования данных
    copy_data_between_shapefiles(source_path, target_path, output_path)
