from os import path

json_zip_download_url = "http://mtgjson.com/json/AllSets-x.json.zip"
output_data_folder = path.abspath('spellbook/data')
json_zip_path = path.join(output_data_folder, 'AllSets-x.json.zip')
json_data_path = path.join(output_data_folder, 'AllSets-x.json')
pretty_json_path = path.join(output_data_folder, 'AllSets-x-pretty.json')
