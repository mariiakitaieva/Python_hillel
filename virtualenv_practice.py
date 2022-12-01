cd /home/masha/kaif/envs
python3.9 -m venv pinguin
ls
cd..
source pinguin/bin/activate
pip install requests
pip install pytest
pip install locust
pip freeze
pip freeze > requirements.txt
pip install -r .requirements.txt
deactivate
