==========
WikiRep
===========

sample execution:
```sh
python main.py -vvv makedump Love War Rain Tree God
python main.py -vvv parse
python main.py -vvv build

python main.py -vvv get_value "roots of gods are love happiness and freedom while leaves are very important"
INFO:MAIN:vector = [ 1.22261306  0.18109712  0.07278491  1.53118789  0.46724431]

python main.py -vvv compare --text1 "roots of gods are love happiness and freedom while leaves are very important" --text2 "belive trust happines destroy crash dead people and cityes global war"
INFO:MAIN:correlation = 0.218889787332
```