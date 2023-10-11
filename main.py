from flask import Flask
from flask import render_template

app = Flask(__name__, template_folder='template')
@app.route('/')
def index():
 return render_template("index.html")

@app.route('/pasp')
def f1():
  return '''
  <!DOCTYPE html>
  <head> 
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>replit</title>
  <link href="/static/style.css" rel="stylesheet" type="text/css" />
  </head>
  <body>
  <font size = "5">
  <div class = "topMenu">
  <a href="https://project.boghdaniakushie.repl.co" class = "menu">  Вариации проекта 
  </a>
  <a href="https://project.boghdaniakushie.repl.co/pasp" class = "menu"> Паспорт проекта </a>
  <a href="https://project.boghdaniakushie.repl.co/obos" class = "menu"> Обоснование 
  </a> 
  <a href="https://project.boghdaniakushie.repl.co/real" class = "menu"> Планирование 
  реализации </a> </div> </font>

<font size="4">
<h1 align=center> Гипотеза Коллатца </h1>
<h2 align=center> Паспорт проекта</h2> </font>

       <font size = "4">
       <table border="1">
       <tr>
       <td>Проблема</td>
       <td> <a class="underl">В случае варианта проекта 1 или 2:</a> 
 отсутствие доказательства гипотезы Коллатца. <br>
<a class="underl">В случае варианта проекта 3:</a> верно ли, что алгоритмы, схожие с алгоритмом Коллатца, также приведут любое число к единице?  
</td>
       </tr>
       <tr>
       <td>Цели</td>
       <td><a class="underl">Учебная цель:</a> освоение проектной деятельности, повышение интеллектуальных и творческих способностей во время работы над проектом. <br>
<a class="underl">Продуктовая цель:</a> <br>
    <a class="underl">В случае варианта проекта 1 или 2:</a> доказательство гипотезы Коллатца для чисел конкретного вида <br>
    <a class="underl">В случае варианта проекта 3:</a> открытие новой полезной информации о гипотезе Коллатца</td>
       </tr>
       <tr> 
       <td>Планируемый продукт</td>
       <td>Презентация с итогами проделанной работы</td>
       </tr>
       <tr> 
       <td>Целевая аудитория </td>
       <td>Группа людей, интересующаяся гипотезой Коллатца</td>
       </tr>
       <tr> 
       <td>Экспертиза качества проектов</td>
       <td>Проект признаётся успешным, если достигнута продуктовая цель проекта для соответствующего варианта проекта</td>
       </tr>
       <tr> 
       <td>Сроки выполнения </td>
       <td> Срок выполнения основной части проекта — 2 месяца. Основная часть включает в себя достижение продуктовой цели. <br>
Срок выполнения заключительной части проекта — 1 неделя.
Заключительная часть включает в себя создание презентации с итогами работы над проектом.
</td>
       </tr>
       <tr> 
       <td>Индикаторы успеха </td>
       <td>Проект признаётся успешным, если достигнута продуктовая цель проекта для соответствующего варианта проекта</td>
       </tr>
       </table>
       </font>

       <font size="2"> <div class = "ism"> Последнее изменение: 6 октября. </div> </font>
   </body> </html>
  '''

@app.route('/obos') 
def f2():
  return '''
  <!DOCTYPE html>
  <head> 
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>replit</title>
  <link href="/static/style.css" rel="stylesheet" type="text/css" />
  </head>
  <body> 
  <font size="5">
  <div class = "topMenu">
<a href="https://project.boghdaniakushie.repl.co" class = "menu">  Вариации проекта </a>
<a href="https://project.boghdaniakushie.repl.co/pasp" class = "menu"> Паспорт проекта </a>
<a href="https://project.boghdaniakushie.repl.co/obos" class = "menu"> Обоснование </a> 
<a href="https://project.boghdaniakushie.repl.co/real" class = "menu"> Планирование реализации </a> </div> </font>
  <font size="4">
  <h1 align=center> Гипотеза Коллатца </h1>
  <h2 align=center> Обоснование </h2> 
  <p> <b> Гипотеза Коллатца </b> – это одна из нерешенных проблем математики, которая была сформулирована математиком Лотаром Коллатцем ещё в 1932 году. Она гласит, что если взять любое натуральное число n, и умножать его на 3 с последующим прибавлением единицы (получая 3n+1), если оно нечётное, либо же делить его на 2, если оно чётное, то выполняя данный алгоритм, мы рано или поздно получим единицу1. Однако до сих пор никому не удалось доказать данную гипотезу. 
Я решил лучше понять, как работает данная гипотеза. 

В связи с тем, что полное доказательство гипотезы за прошедшие 90 лет так и не было найдено, оно, вероятно, крайне сложно, поэтому я решил доказать данную гипотезу только для частного случая – для чисел X.
Доказательство гипотезы для бесконечного числа чисел X поможет понять, как доказать гипотезу для всего множества чисел. </font> 
 </p> 

 <font size="2"> <div class = "ism"> Последнее изменение: 6 октября. </div> </font>
 </body> </html>
  '''

@app.route('/real')
def f3():
  return '''
  <!DOCTYPE html>
  <head> 
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>replit</title>
  <link href="/static/style.css" rel="stylesheet" type="text/css" />
  </head>
  <body> 
  <font size="5">
  <div class = "topMenu">
<a href="https://project.boghdaniakushie.repl.co" class = "menu">  Вариации проекта </a>
<a href="https://project.boghdaniakushie.repl.co/pasp" class = "menu"> Паспорт проекта </a>
<a href="https://project.boghdaniakushie.repl.co/obos" class = "menu"> Обоснование </a> 
<a href="https://project.boghdaniakushie.repl.co/real" class = "menu"> Планирование реализации </a> </div> </font> 

<font size="4">
  <h1 align=center> Гипотеза Коллатца </h1>
  <h2 align=center> Планирование реализации проекта 3.2 <font size="3">(выбран в качестве основного) </font> </h2>
  
<p> 
<font size="5">
1. Рассмотрение различных алгоритмов, описанных в п. 3.2: <br> 
— (9n+3, :6) <font size ="2"> (рассмотрение окончено, сделан вывод) </font>, <br>
— (15n+5, :10) <font size ="2"> (рассмотрение окончено, сделан вывод) </font>, <br>
— (21n+7, :14), <br>
— (27n+9, :18) <font size ="2"> (рассмотрение окончено, сделан вывод) </font>, <br>
— (33n+11, :22), <br>
и т.д. по возрастанию. <br>
Сроки - до начала-середины ноября. <br>
2. Доработка проекта, резервный срок. Сроки - до начала декабря. <br>
3. Изготовление презентации с выводом. Сроки - первая неделя декабря.
</font>
</p>

 <font size="2"> <div class = "ism"> Последнее изменение: 8 октября. </div> </font>
 </body> </html>
  
  
'''


if __name__ == "__main__":
  app.run(host='0.0.0.0', port=5001)
