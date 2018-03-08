django-admin makemigrations
django-admin migrate
# django-admin flush --noinput

django-admin import_data -A ./resources/elections/elections.yaml -B ./resources/elections/ -v1
django-admin import_data -A ./resources/aec_res_injests/HoR.1903-early.yaml -B ./resources/aec_resources/ -v2 --arg=year:1903 --arg=party_column:Party_fulll

django-admin import_data -A ./resources/aec_res_injests/HoR.1903-early.yaml -B ./resources/aec_resources/ -v1 -D --arg=year:1906 --arg=party_column:Party_fulll

django-admin import_data -A ./resources/aec_res_injests/HoR.1903-early.yaml -B ./resources/aec_resources/ -v1 -D --arg=year:1910 --arg='party_column:Party full'

django-admin import_data -A ./resources/aec_res_injests/HoR.1903-early.yaml -B ./resources/aec_resources/ -v1 -D --arg=year:1913 --arg='party_column:Party full'

django-admin import_data -A ./resources/aec_res_injests/HoR.1903-early.yaml -B ./resources/aec_resources/ -v1 -D --arg=year:1914 --arg='party_column:Party full'

django-admin import_data -A ./resources/aec_res_injests/HoR.1903-early.yaml -B ./resources/aec_resources/ -v1 -D --arg=year:1917 --arg='party_column:Party full'

django-admin import_data -A ./resources/aec_res_injests/HoR.1919-x.yaml -B ./resources/aec_resources/ -v1 -D --arg=year:1919

django-admin import_data -A ./resources/aec_res_injests/HoR.1919-x.yaml -B ./resources/aec_resources/ -v1 -D --arg=year:1922
django-admin import_data -A ./resources/aec_res_injests/HoR.1919-x.yaml -B ./resources/aec_resources/ -v1 -D --arg=year:1925

django-admin import_data -A ./resources/aec_res_injests/HoR.1919-x.yaml -B ./resources/aec_resources/ -v1 -D --arg=year:1928
django-admin import_data -A ./resources/aec_res_injests/HoR.1919-x.yaml -B ./resources/aec_resources/ -v1 -D --arg=year:1929
django-admin import_data -A ./resources/aec_res_injests/HoR.1919-x.yaml -B ./resources/aec_resources/ -v1 -D --arg=year:1931
django-admin import_data -A ./resources/aec_res_injests/HoR.1919-x.yaml -B ./resources/aec_resources/ -v1 -D --arg=year:1934
django-admin import_data -A ./resources/aec_res_injests/HoR.1919-x.yaml -B ./resources/aec_resources/ -v1 -D --arg=year:1937
django-admin import_data -A ./resources/aec_res_injests/HoR.1919-x.yaml -B ./resources/aec_resources/ -v1 -D --arg=year:1943
django-admin import_data -A ./resources/aec_res_injests/HoR.1919-x.yaml -B ./resources/aec_resources/ -v1 -D --arg=year:1946
django-admin import_data -A ./resources/aec_res_injests/HoR.1919-x.yaml -B ./resources/aec_resources/ -v1 -D --arg=year:1949
django-admin import_data -A ./resources/aec_res_injests/HoR.1919-x.yaml -B ./resources/aec_resources/ -v1 -D --arg=year:1949
django-admin import_data -A ./resources/aec_res_injests/HoR.1919-x.yaml -B ./resources/aec_resources/ -v1 -D --arg=year:1951
django-admin import_data -A ./resources/aec_res_injests/HoR.1919-x.yaml -B ./resources/aec_resources/ -v1 -D --arg=year:1954
django-admin import_data -A ./resources/aec_res_injests/HoR.1919-x.yaml -B ./resources/aec_resources/ -v1 -D --arg=year:1955
django-admin import_data -A ./resources/aec_res_injests/HoR.1919-x.yaml -B ./resources/aec_resources/ -v1 -D --arg=year:1958
django-admin import_data -A ./resources/aec_res_injests/HoR.1919-x.yaml -B ./resources/aec_resources/ -v1 -D --arg=year:1961
django-admin import_data -A ./resources/aec_res_injests/HoR.1919-x.yaml -B ./resources/aec_resources/ -v1 -D --arg=year:1963
django-admin import_data -A ./resources/aec_res_injests/HoR.1919-x.yaml -B ./resources/aec_resources/ -v1 -D --arg=year:1966
django-admin import_data -A ./resources/aec_res_injests/HoR.1919-x.yaml -B ./resources/aec_resources/ -v1 -D --arg=year:1972
django-admin import_data -A ./resources/aec_res_injests/HoR.1919-x.yaml -B ./resources/aec_resources/ -v1 -D --arg=year:1974
django-admin import_data -A ./resources/aec_res_injests/HoR.1919-x.yaml -B ./resources/aec_resources/ -v1 -D --arg=year:1987
