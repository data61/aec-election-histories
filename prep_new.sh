./manage.py makemigrations aec
./manage.py migrate
./manage.py flush --noinput

./manage.py import_data -A ~/workspace/resources/tosspots/tosspots.yaml -B ~/workspace/resources/tosspots/ -v1
./manage.py import_data -A ~/workspace/resources/aec_res_injests/HoR.1903-early.yaml -B ~/workspace/resources/aec_resources/ -v2 --arg=year:1903 --arg=party_column:Party_fulll

./manage.py import_data -A ~/workspace/resources/aec_res_injests/HoR.1903-early.yaml -B ~/workspace/resources/aec_resources/ -v1 -D --arg=year:1906 --arg=party_column:Party_fulll

./manage.py import_data -A ~/workspace/resources/aec_res_injests/HoR.1903-early.yaml -B ~/workspace/resources/aec_resources/ -v1 -D --arg=year:1910 --arg='party_column:Party full'

./manage.py import_data -A ~/workspace/resources/aec_res_injests/HoR.1903-early.yaml -B ~/workspace/resources/aec_resources/ -v1 -D --arg=year:1913 --arg='party_column:Party full'

./manage.py import_data -A ~/workspace/resources/aec_res_injests/HoR.1903-early.yaml -B ~/workspace/resources/aec_resources/ -v1 -D --arg=year:1914 --arg='party_column:Party full'

./manage.py import_data -A ~/workspace/resources/aec_res_injests/HoR.1903-early.yaml -B ~/workspace/resources/aec_resources/ -v1 -D --arg=year:1917 --arg='party_column:Party full'

./manage.py import_data -A ~/workspace/resources/aec_res_injests/HoR.1919-x.yaml -B ~/workspace/resources/aec_resources/ -v1 -D --arg=year:1919

./manage.py import_data -A ~/workspace/resources/aec_res_injests/HoR.1919-x.yaml -B ~/workspace/resources/aec_resources/ -v1 -D--arg=year:1922
./manage.py import_data -A ~/workspace/resources/aec_res_injests/HoR.1919-x.yaml -B ~/workspace/resources/aec_resources/ -v1 -D--arg=year:1925

./manage.py import_data -A ~/workspace/resources/aec_res_injests/HoR.1919-x.yaml -B ~/workspace/resources/aec_resources/ -v1 -D--arg=year:1928
./manage.py import_data -A ~/workspace/resources/aec_res_injests/HoR.1919-x.yaml -B ~/workspace/resources/aec_resources/ -v1 -D--arg=year:1929