# bon_parser
Primeste imaginea unui bon fiscal si genereaza un document cu valorile semificative identificate.<br>
Primeste fisiere .png sau .jpg si genereaza pentru fiecare cate un document .xlsx.<br>
Pentru recunoasterea caracterelor: https://github.com/tesseract-ocr/tesseract<br>
Pentru procesarea imaginilor: https://pypi.org/project/opencv-python/ (3.4.11.45) (Mai multe detalii in requirements.txt)<br>


<br>
<h3> Limitari (TODO) </h3>
<ol>
  <li> Recunoasterea caracterelor poate fi imbunatatita prin marirea numarului de proceduri de preprocesare a imaginii. </li>
  <li> Adaugarea suportului pentru diferite layout-uri de bonuri fiscale (versiunea actuala nu poate detecta obiectele care au pretul pe acelasi rand cu ele)</li>
</ol>
<br>

<h2> Exemple </h2>


<h3> Extragere obiecte </h3>

<b>Imagine</b>            |  <b>Excel</b>
:-------------------------:|:-------------------------:
![bon1](https://media.discordapp.net/attachments/705512266719690765/777893353957621780/bon.jpg?width=214&height=400)  |  ![bon1](https://cdn.discordapp.com/attachments/705512266719690765/777893549835288586/unknown.png)
<br>

<h3> Extragere unitate si cif </h3>

<b>Imagine</b>            |  <b>Excel</b>
:-------------------------:|:-------------------------:
![bon1](https://media.discordapp.net/attachments/705512266719690765/777893358001061928/bon2.jpg?width=306&height=600)  |  ![bon1](https://cdn.discordapp.com/attachments/705512266719690765/777896662814294036/unknown.png)

<br>
<h3> Alte Exemple </h3>

<b> Imagine </b>                | <b> Excel</b>
:------------------------------:|:----------------------------:
![bon3](https://media.discordapp.net/attachments/705512266719690765/777893352611643392/bon4.jpg?width=229&height=569) | ![bon3](https://cdn.discordapp.com/attachments/705512266719690765/777900094062198855/unknown.png)








