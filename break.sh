cd ~/workspace/git/aec
export PYTHONPATH=aec_election_history:~/workspace/git/django-data-importer

rm db.sqlite3
rm aec_election_history/aec/election/migrations/*.py
rm aec_election_history/aec/party/migrations/*.py
rm aec_election_history/aec/person/migrations/*.py

# ./manage.py import_data -A ~/workspace/aec_res_injests/1903HoR.yaml -B ~/workspace/aec_resources/ -v3 -D
