# Pyhton-Api-And-Ui-Automation
Pyhton Api And Ui Automation

pip install -r req*.txt ile gereklilikler kurulmalıdır.


** UI Otomasyonu Çalıştırmak İçin Değişkenleri Passleyerek Çalıştırılmalıdır.
* CrossBrowser Olarak Çalışmaktadır. BrowserUtils.py ile driver confileri yapılabilir ve headless da çalıştırılabilir.
python3 test_search.py <browser> <searchText> <username> <password>
python3 test_search.py chrome iphone test@mail.com P4ssW0rd
python3 test_search.py firefox samsung test@mail.com P4ssW0rd

** Api Otomasyonunu Çalıştırmak İçin
Apiden dönen responselar için sadece response assertion yerine, şema validasyonlarıda eklenmiştir.

Pytest ile Çalıştırma:
pytest -v
<img width="1694" alt="image" src="https://github.com/akkaya040/Pyhton-Api-And-Ui-Automation/assets/9138241/ed0f1515-a7be-4e8b-91e9-dae37eb3217a">
Python ile çalıştırma:
python3 test_api.py
<img width="1603" alt="image" src="https://github.com/akkaya040/Pyhton-Api-And-Ui-Automation/assets/9138241/8ad77bbf-f5c5-4c5e-b1af-84279b20377a">

