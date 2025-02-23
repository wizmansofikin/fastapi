---
hide:
  - navigation
---

<style>
.md-content .md-typeset h1 { display: none; }
</style>

<p align="center">
  <a href="https://fastapi.tiangolo.com"><img src="https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png" alt="FastAPI"></a>
</p>
<p align="center">
    <em>FastAPI ფრეიმვორქი, მაღალი წარმადობა, ასათვისებლად მარტივი, ეფექტური, წარმოებაში ჩაშვებისათვის გამზადებული</em>
</p>
<p align="center">
<a href="https://github.com/tiangolo/fastapi/actions?query=workflow%3ATest+event%3Apush+branch%3Amaster" target="_blank">
    <img src="https://github.com/tiangolo/fastapi/workflows/Test/badge.svg?event=push&branch=master" alt="Test">
</a>
<a href="https://coverage-badge.samuelcolvin.workers.dev/redirect/tiangolo/fastapi" target="_blank">
    <img src="https://coverage-badge.samuelcolvin.workers.dev/tiangolo/fastapi.svg" alt="Coverage">
</a>
<a href="https://pypi.org/project/fastapi" target="_blank">
    <img src="https://img.shields.io/pypi/v/fastapi?color=%2334D058&label=pypi%20package" alt="Package version">
</a>
<a href="https://pypi.org/project/fastapi" target="_blank">
    <img src="https://img.shields.io/pypi/pyversions/fastapi.svg?color=%2334D058" alt="Supported Python versions">
</a>
</p>

---

**დოკუმენტაცია**: <a href="https://fastapi.tiangolo.com" target="_blank">https://fastapi.tiangolo.com</a>

**პროგრამული კოდი**: <a href="https://github.com/tiangolo/fastapi" target="_blank">https://github.com/tiangolo/fastapi</a>

---

FastAPI არის თანამედროვე, სწრაფი (მაღალი წარმადობის მქონე), Python-ზე დაფუძნებული ვებფრეიმვორქი, რომელიც იყენებს Python-ის სტანდარტულ ტიპთა ანოტაციებს და საშუალებას გვაძლევს შევქმნათ API-ები.

მისი ძირითადი მახასიათებლები გახლავთ:

* **სისწრაფე**: **NodeJS**-ისა და **Go**-ს მსგავსად აქვს ძალიან მაღალი წარმადობა (რასაც Starlette-ს და Pydantic-ს უნდა ვუმადლოდეთ). [ერთ-ერთი უსწრაფესი ფრეიმვორქია Python-ის არსებულ ფრეიმვორქებს შორის](#performance).
* **ეფექტურობა**: დეველოპმენტის პროცესს აჩქარებს დაახლოებით 200-300 პროცენტით. *
* **ნაკლები პროგრამული ხარვეზი**: ადამიანის (დეველოპერის) მიერ გამოწვეული ხარვეზების ალბათობას ამცირებს დაახლოებით 40 პროცენტით. *
* **ინტუიციურობა**: შესანიშნავი თავსებადობა ტექსტურ რედაქტორებთან. <abbr title="ასევე ცნობილია, როგორც: ავტოდასრულება, ავტომატური დასრულება, IntelliSense-ი">კოდის ავტოდასრულების</abbr> ფუნქციონალი ხელმისაწვდომია სრული მასშტაბით. ნაკლებ დროს დახარჯავთ ხარვეზების აღმოფხვრაში.
* **სიმარტივე**: ტექნოლოგია შემუშავებულია იმგვარად, რომ მარტივად გამოსაყენებელი და ასათვისებელი იყოს. დოკუმენტაციის კითხვაში ნაკლებ დროს დახარჯავთ.
* **კომპაქტურობა**: კოდის დუბლიკაციის საჭიროება მინიმუმამდეა დაყვანილი. თითოეული პარამეტრის განსაზღვრით აქტიურდება მრავალი ფუნქციონალი. პროგრამული ხარვეზების წარმოქმნის ალბათობა მინიმუმამდეა დაყვანილი.
* **მდგრადობა**: მიიღებთ წარმოებაში ჩაშვებისათვის გამზადებულ კოდს. ამას გარდა, მიიღებთ ავტომატურად გენერირებულ ინტერაქციულ დოკუმენტაციას.
* **სტანდარტებზე დაფუძნებულობა**: დაფუძნებულია (და სრულად თავსებადია) API-იებისთვის განსაზღვრულ ღია სტანდარტებზე: <a href="https://github.com/OAI/OpenAPI-Specification" class="external-link" target="_blank">OpenAPI</a> (ადრე ცნობილი იყო, როგორც Swagger) და <a href="https://json-schema.org/" class="external-link" target="_blank">JSON Schema</a>.

<small>* ზემოთ მოცემული შეფასებები ეფუძნება წარმოებაში ჩაშვებულ (რეალურ) აპლიკაციებზე მომუშავე შიდა დეველოპმენტის გუნდის მიერ ჩატარებულ ტესტებს.</small>

## სპონსორები

<!-- sponsors -->

{% if sponsors %}
{% for sponsor in sponsors.gold -%}
<a href="{{ sponsor.url }}" target="_blank" title="{{ sponsor.title }}"><img src="{{ sponsor.img }}" style="border-radius:15px"></a>
{% endfor -%}
{%- for sponsor in sponsors.silver -%}
<a href="{{ sponsor.url }}" target="_blank" title="{{ sponsor.title }}"><img src="{{ sponsor.img }}" style="border-radius:15px"></a>
{% endfor %}
{% endif %}

<!-- /sponsors -->

<a href="https://fastapi.tiangolo.com/fastapi-people/#sponsors" class="external-link" target="_blank">სხვა სპონსორები</a>

## მოსაზრებები

"_[...] ბოლო დროს, ძალიან ხშირად ვიყენებ **FastAPI**-ს. [...] სიმართლე გითხრათ, მის გამოყენებას ვაპირებ ყველა იმ **ML სერვისისთვის Microsoft-ში**, რაზეც კი ჩემი გუნდი მუშაობს. აღნიშნული სერვისებიდან ზოგიერთი ინტეგრირებულია **Windows**-ის ბირთვში, ზოგი კი — **Office**-ის პროდუქტებში._"

<div style="text-align: right; margin-right: 10%;">Kabir Khan - <strong>Microsoft</strong> <a href="https://github.com/tiangolo/fastapi/pull/26" target="_blank"><small>(ref)</small></a></div>

---

"_ჩვენ გამოვიყენეთ **FastAPI** ბიბლიოთეკა **REST** სერვერის შესაქმნელად, რომლის დანიშნულება გახლავთ სხვადასხვა **პროგნოზების** გაკეთება. [Ludwig-ისთვის]_"

<div style="text-align: right; margin-right: 10%;">Piero Molino, Yaroslav Dudin, and Sai Sumanth Miryala - <strong>Uber</strong> <a href="https://eng.uber.com/ludwig-v0-2/" target="_blank"><small>(ref)</small></a></div>

---

"_**Netflix**-ის სახელით მოხარული ვარ გაცნობოთ ჩვენი **კრიზისის მართვის** ორკესტრაციის სისტემის, **Dispatch**-ის წყაროს ღია რელიზის შესახებ! [რომელიც შექმნილია **FastAPI**-ის გამოყენებით]_"

<div style="text-align: right; margin-right: 10%;">Kevin Glisson, Marc Vilanova, Forest Monsen - <strong>Netflix</strong> <a href="https://netflixtechblog.com/introducing-dispatch-da4b8a2a8072" target="_blank"><small>(ref)</small></a></div>

---

"_**FastAPI**-ით ცამდე აღფრთოვანებული ვარ. მისი გამოყენება ძალიან სახალისოა!_"

<div style="text-align: right; margin-right: 10%;">Brian Okken - <strong><a href="https://pythonbytes.fm/episodes/show/123/time-to-right-the-py-wrongs?time_in_sec=855" target="_blank">Python Bytes</a> podcast host</strong> <a href="https://twitter.com/brianokken/status/1112220079972728832" target="_blank"><small>(ref)</small></a></div>

---

"_გულწრფელად გეუბნებით, თქვენი ნამუშევარი ძალიან სანდოდ და დახვეწილად გამოიყურება. სწორედ ეს არის ის, რაც მინდოდა **Hug**-ი ყოფილიყო — მართლაც შთამაგონებელია იმის დანახვა, რომ ვიღაცამ შეძლო ამის შექმნა._"

<div style="text-align: right; margin-right: 10%;">Timothy Crosley - <strong><a href="https://www.hug.rest/" target="_blank">Hug</a> creator</strong> <a href="https://news.ycombinator.com/item?id=19455465" target="_blank"><small>(ref)</small></a></div>

---

"_თუ **თანამედროვე ფრეიმვორქს** ეძებთ, რომლითაც REST API-ების შექმნაა შესაძლებელი, გადახედეთ **FastAPI**-ს [...] იგი არის სწრაფი, მარტივად გამოსაყენებელი და ადვილად შესასწავლი [...]_"

"_ჩვენ გადავაწყვეთ ჩვენი **API**-ები **FastAPI**-ზე [...] ვფიქრობ, აღნიშნული ფრეიმვორქი გულგრილს არავის დატოვებს [...]_"

<div style="text-align: right; margin-right: 10%;">Ines Montani - Matthew Honnibal - <strong><a href="https://explosion.ai" target="_blank">Explosion AI</a> founders - <a href="https://spacy.io" target="_blank">spaCy</a> creators</strong> <a href="https://twitter.com/_inesmontani/status/1144173225322143744" target="_blank"><small>(ref)</small></a> - <a href="https://twitter.com/honnibal/status/1144031421859655680" target="_blank"><small>(ref)</small></a></div>

---

"_თუ ვინმე აპირებს შექმნას Python-ზე დაფუძნებული, წარმოებაში ჩასაშვებად ვარგისი API-ი, **FastAPI**-ის გამოყენებას ვურჩევ. ეს არის **დახვეწილი**, **მარტივად გამოსაყენებელი** და **მასშტაბირებადი** ტექნოლოგია. იგი გახდა API-ების შემუშავების ჩვენეული სტრატეგიის **ქვაკუთხედი** და სწორედ მისი გამოყენებითაა შემუშავებული ჩვენი არაერთი ავტომატიზაციის სისტემა და სერვისები, მათ შორის ჩვენი ვირტუალური TAC ინჟინერი._"

<div style="text-align: right; margin-right: 10%;">Deon Pillsbury - <strong>Cisco</strong> <a href="https://www.linkedin.com/posts/deonpillsbury_cisco-cx-python-activity-6963242628536487936-trAp/" target="_blank"><small>(ref)</small></a></div>

---

## **Typer**: ბრძანებათა სტრიქონის FastAPI

<a href="https://typer.tiangolo.com" target="_blank"><img src="https://typer.tiangolo.com/img/logo-margin/logo-margin-vector.svg" style="width: 20%;"></a>

თუკი მუშაობთ <abbr title="ბრძანებათა სტრიქონი">CLI</abbr> აპლიკაციაზე, რომელიც ვებ API-ის ნაცვლად გამოყენებულ იქნება ტერმინალში, თვალი შეავლეთ <a href="https://typer.tiangolo.com/" class="external-link" target="_blank">**Typer**-ს</a>.

**Typer**-ი არის FastAPI-ის პატარა ძამიკო. იგი ჩაფიქრებულია, როგორც **FastAPI ბრძანებათა სტრიქონისათვის**. ⌨️ 🚀

## მოთხოვნები

FastAPI მხრებზე შემოსდგომია ისეთ გიგანტებს, როგორებიცაა:

* <a href="https://www.starlette.io/" class="external-link" target="_blank">Starlette</a>: ვების ნაწილში.
* <a href="https://docs.pydantic.dev/" class="external-link" target="_blank">Pydantic</a>: მონაცემების ნაწილში.

## ინსტალაცია

<div class="termy">

```console
$ pip install fastapi

---> 100%
```

</div>

## მაგალითი

### შევქმნათ

* შექმენით `main.py` ფაილი შემდეგი შიგთავსით:

```Python
from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
```

<details markdown="1">
<summary>ან გამოიყენეთ <code>async def</code>...</summary>

თუ თქვენი კოდი იყენებს `async` / `await` კონსტრუქციას, გამოიყენეთ `async def`:

```Python hl_lines="9  14"
from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
```

**შენიშვნა**:

თუ თქვენ ჯერ არ ხართ გარკვეული აღნიშნულ საკითხში, <a href="https://fastapi.tiangolo.com/async/#in-a-hurry" target="_blank">`async`-ისა და `await`-ის შესახებ</a> დოკუმენტაციაში გადახედეთ განყოფილებას, სათაურით: _„გეჩქარებათ?“_.

</details>

### გავუშვათ

გაუშვით სერვერი შემდეგი ბრძანებით:

<div class="termy">

```console
$ fastapi dev main.py

 ╭────────── FastAPI CLI - Development mode ───────────╮
 │                                                     │
 │  Serving at: http://127.0.0.1:8000                  │
 │                                                     │
 │  API docs: http://127.0.0.1:8000/docs               │
 │                                                     │
 │  Running in development mode, for production use:   │
 │                                                     │
 │  fastapi run                                        │
 │                                                     │
 ╰─────────────────────────────────────────────────────╯

INFO:     Will watch for changes in these directories: ['/home/user/code/awesomeapp']
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [2248755] using WatchFiles
INFO:     Started server process [2248757]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

</div>

<details markdown="1">
<summary><code>fastapi dev main.py</code> ბრძანების შესახებ...</summary>

`fastapi dev` ბრძანება კითხულობს თქვენს `main.py` ფაილს, მასში **FastAPI** აპლიკაციას აიდენტიფიცირებს და <a href="https://www.uvicorn.org" class="external-link" target="_blank">Uvicorn</a>-ის გამოყენებით უშვებს სერვერს.

ნაგულისხმევად, ლოკალური დეველოპმენტისთვის, `fastapi dev` ბრძანებით გაშვებული სერვერისთვის აქტივირებული იქნება ავტოგადატვირთვის ფუნქცია.

ამ საკითხთან დაკავშირებით დამატებითი ინფორმაცია შეგიძლიათ წაიკითხოთ <a href="https://fastapi.tiangolo.com/fastapi-cli/" target="_blank">FastAPI CLI-ის დოკუმენტაციაში</a>.

</details>

### შევამოწმოთ

ბრაუზერში გახსენით შემდეგი ბმული: <a href="http://127.0.0.1:8000/items/5?q=somequery" class="external-link" target="_blank">http://127.0.0.1:8000/items/5?q=somequery</a>.

დაინახავთ JSON ფორმატის მქონე მონაცემს:

```JSON
{"item_id": 5, "q": "somequery"}
```

ამგვარად, თქვენ უკვე შექმენით API, რომელიც:

* იღებს HTTP მოთხოვნებს შემდეგ _მისამართებზე_: `/` და `/items/{item_id}`.
* ორივე _მისამართი_ ამუშავებს `GET` <em>ოპერაციას</em> (ასევე ცნობილია, როგორც HTTP _მეთოდი_).
* `/items/{item_id}` _მისამართს_ გააჩნია _მარშრუტის პარამეტრი_ `item_id`, რომელიც უნდა იყოს მთელი რიცხვის (`int`) ტიპის.
* `/items/{item_id}` მისამართი შეიცავს სტრიქონის (`str`) ტიპის არასავალდებულო `q` _საძიებო (query) პარამეტრს_.

### ინტერაქციული API დოკუმენტაცია

გახსენით თქვენი ბრაუზერი და შედით ბმულზე: <a href="http://127.0.0.1:8000/docs" class="external-link" target="_blank">http://127.0.0.1:8000/docs</a>.

დაინახავთ ავტომატურად გენერირებულ ინტერაქციულ API დოკუმენტაციას (რომელიც უზრუნველყოფილია <a href="https://github.com/swagger-api/swagger-ui" class="external-link" target="_blank">Swagger UI</a>-ის მიერ):

![Swagger UI](https://fastapi.tiangolo.com/img/index/index-01-swagger-ui-simple.png)

### ალტერნატიული API დოკუმენტაცია

ბრაუზერში გახსენით შემდეგი ბმული: <a href="http://127.0.0.1:8000/redoc" class="external-link" target="_blank">http://127.0.0.1:8000/redoc</a>.

დაინახავთ ალტერნატიულ ავტომატურად გენერირებულ დოკუმენტაციას (რომელიც უზრუნველყოფილია <a href="https://github.com/Rebilly/ReDoc" class="external-link" target="_blank">ReDoc</a>-ის მიერ):

![ReDoc](https://fastapi.tiangolo.com/img/index/index-02-redoc-simple.png)

## გაუმჯობესების მაგალითი

მოდით, შევცვალოთ `main.py` ფაილის შიგთავსი იმგვარად, რომ `PUT` ოპერაციით შევძლოთ მონაცემების მიღება.

მოვახდინოთ მოთხოვნის შიგთავსის პროტოტიპის დეკლარაცია Python-ის სტანდარტული ტიპების გამოყენებით. ამ შესაძლებლობას Pydantic-ს უნდა ვუმადლოდეთ.

```Python hl_lines="4  9-12  25-27"
from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}
```

ცვლილებების შენახვის შემდეგ, `fastapi dev` ბრძანებით გაშვებული სერვერი, წესით და რიგით, ავტომატურად გადაიტვირთება.

### გავაუმჯობესოთ ინტერაქციული API დოკუმენტაცია

ბრაუზერში გახსენით შემდეგი ბმული: <a href="http://127.0.0.1:8000/docs" class="external-link" target="_blank">http://127.0.0.1:8000/docs</a>.

* ინტერაქციული API დოკუმენტაცია ავტომატურად განახლდება და ახლად დამატებული შიგთავსის პროტოტიპიც გამოჩნდება:

![Swagger UI](https://fastapi.tiangolo.com/img/index/index-03-swagger-02.png)

* დააწკაპუნეთ „Try it out“ ღილაკზე. ეს საშუალებას მოგცემთ, ხელით გაწეროთ პარამეტრების მნიშვნელობები და API-სთან უშუალო ინტერაქციით დაკავდეთ:

![Swagger UI interaction](https://fastapi.tiangolo.com/img/index/index-04-swagger-03.png)

* შემდგომ ამისა, დააწკაპუნეთ „Execute“ ღილაკზე, რითაც თქვენ მიერ გახსნილი ინტერფეისი დაუკავშირდება API-ს, გაგზავნის თქვენ მიერ განსაზღვრულ პარამეტრებს, მიიღებს მოთხოვნის შედეგებს და გამოიტანს ეკრანზე:

![Swagger UI interaction](https://fastapi.tiangolo.com/img/index/index-05-swagger-04.png)

### გავაუმჯობესოთ ალტერნატიული API დოკუმენტაცია

ახლა კი, ბრაუზერში გახსენით შემდეგი ბმული: <a href="http://127.0.0.1:8000/redoc" class="external-link" target="_blank">http://127.0.0.1:8000/redoc</a>.

* ახლად დამატებული საძიებო პარამეტრი და შიგთავსის პროტოტიპი ალტერნატიულ დოკუმენტაციაშიც პოვებს ასახვას:

![ReDoc](https://fastapi.tiangolo.com/img/index/index-06-redoc-02.png)

### შეჯამება

ამრიგად, პარამეტრების, შიგთავსის პროტოტიპებისა და სხვა ტიპების დეკლარირებას ახორციელებთ **ერთჯერადად**. როგორც ფუნქციისათვის პარამეტრების განსაზღვრისას ხდება.

ამას აკეთებთ Python-ის თანამედროვე, სტანდარტული ტიპების გამოყენებით.

არ გჭირდებათ რომელიმე ცალკეული ბიბლიოთეკისთვის დამახასიათებელი განსხვავებული სინტაქსის, მეთოდების ან კლასების შესწავლა.

იყენებთ მხოლოდ და მხოლოდ სტანდარტულ **Python**-ს.

მაგალითისათვის, `int`-ის შემთხვევაში:

```Python
item_id: int
```

ან შედარებით რთული `Item` მოდელისთვის:

```Python
item: Item
```

...და ამ ერთი დეკლარაციით თქვენ მიიღებთ:

* რედაქტორის მხარდაჭერას. მათ შორის:
    * კოდის ავტოდასრულებას.
    * ტიპთა ვალიდურობის შემოწმებას.
* მონაცემთა ვალიდაციას:
    * ავტომატურად გენერირებულ და მარტივად გასაგებ ცდომილების შეტყობინებებს, როდესაც მონაცემები ვალიდური არ იქნება.
    * ვალიდაციას თუნდაც უკიდურესად კომპლექსური (მაგ.: მრავალშრიანი) JSON მონაცემებისათვის.
* შემავალ მონაცემთა <abbr title="ასევე ცნობილია, როგორც: სერიალიზება, პარსირება, კლასიფიცირება">გარდაქმნას</abbr>: ქსელიდან შემომავალი მონაცემების გადათარგმნას Python-ისთვის გასაგებ მონაცემებად და ტიპებად. შესაძლებელია შემდეგი სახის მონაცემების წაკითხვა და გარდაქმნა:
    * JSON.
    * მარშრუტის (Path) პარამეტრები.
    * საძიებო (Query) პარამეტრები.
    * Cookie-ები.
    * თავსართები (Headers).
    * ფორმები.
    * ფაილები.
* გამომავალ მონაცემთა <abbr title="ასევე ცნობილია, როგორც: სერიალიზება, პარსირება, კლასიფიცირება">გარდაქმნას</abbr>: Python-ის მონაცემებისა და ტიპების გადათარგმნას ქსელურ მონაცემებად (JSON-ში). შესაძლებელია შემდეგი სახის მონაცემების გარდაქმნა:
    * Python-ის ტიპები (`str`, `int`, `float`, `bool`, `list` და სხვ.).
    * `datetime` ობიექტები.
    * `UUID` ობიექტები.
    * მონაცემთა ბაზის მოდელები.
    * ...და მრავალი სხვა.
* ავტომატურად გენერირებულ ინტერაქციულ API დოკუმენტაციას, რომელიც მოიცავს 2 ალტერნატიულ ინტერფეისს. ესენია:
    * Swagger UI.
    * ReDoc.

---

მოდით, მივუბრუნდეთ წინა მაგალითს და გავაანალიზოთ, რას და როგორ გააკეთებს **FastAPI**:

* `GET` და `PUT` ოპერაციებისათვის შეამოწმებს, არის თუ არა `item_id` პარამეტრი მითითებული მისამართში.
* `GET` და `PUT` ოპერაციებისათვის გადაამოწმებს, არის თუ არა `item_id` პარამეტრი `int` ტიპის.
    * თუ ეს ასე არ იქნება, კლიენტი იხილავს გამოსადეგ, მარტივად გასაგებ ცდომილების შეტყობინებას.
* `GET` ოპერაციებისათვის შეამოწმებს, არის თუ არა მისამართში წარმოდგენილი არასავალდებულო საძიებო (query) პარამეტრი, სახელად `q` (მაგ.: `http://127.0.0.1:8000/items/foo?q=somequery`).
    * ვინაიდან `q` პარამეტრი კოდში განსაზღვრულია `= None` ბოლოსართით, იგი არასავალდებულოა.
    * `None`-ის არარსებობის შემთხვევაში, იგი იქნებოდა სავალდებულო (მსგავსად მოთხოვნის შიგთავსისა `PUT` ოპერაციის შემთხვევაში).
* `/items/{item_id}` მისამართზე `PUT` ოპერაციისას, წაიკითხავს მოთხოვნის შიგთავსს, როგორც JSON ფორმატის მქონე მონაცემს. ამასთან:
    * შეამოწმებს, არის თუ არა განსაზღვრული `str` ტიპის სავალდებულო `name` ატრიბუტი.
    * შეამოწმებს, არის თუ არა განსაზღვრული `float` ტიპის სავალდებულო `price` ატრიბუტი.
    * შეამოწმებს, მოთხოვნის შიგთავსში არის თუ არა წარმოდგენილი `bool` ტიპის არასავალდებულო `is_offer` ატრიბუტი.
    * ყველაფერი ეს იმუშავებს ნებისმიერი სახის (მაგ.: მრავალშრიანი) JSON მონაცემისათვის.
* ავტომატურად გარდაქმნის JSON-ს სხვა ფორმატის მქონე მონაცემად და პირიქით.
* OpenAPI-ით მოახდენს ყველაფრის დოკუმენტირებას, რაც გამოსადეგი იქნება:
    * ინტერაქციული დოკუმენტაციის სისტემებისათვის.
    * კლიენტის კოდის ავტომატიზებული გენერირების სისტემებისათვის სხვადასხვა ენაში.
* უშუალოდ უზრუნველყოფს 2 ალტერნატიული ინტერაქციული დოკუმენტაციის ვებინტერფეისის არსებობას.

---

ჯერჯერობით ჩვენ რაც განვიხილეთ, მხოლოდ და მხოლოდ ზედაპირია აისბერგისა, მაგრამ, ასე თუ ისე, ალბათ გაიაზრეთ ამ ყველაფრის მუშაობის ზოგადი პრინციპი.

სცადეთ შემდეგ ხაზში ცვლილების შეტანა:

```Python
    return {"item_name": item.name, "item_id": item_id}
```

...ადრე:

```Python
        ... "item_name": item.name ...
```

...ახლა:

```Python
        ... "item_price": item.price ...
```

...და დააკვირდით, როგორ მოახდენს თქვენი ტექსტური რედაქტორი ატრიბუტების ავტოდასრულებას და მათი ტიპების იდენტიფიცირებას:

![editor support](https://fastapi.tiangolo.com/img/vscode-completion.png)

მეტად სრულყოფილი მაგალითის სანახავად, სადაც განხილული იქნება უფრო მეტი საკითხი, იხილეთ <a href="https://fastapi.tiangolo.com/tutorial/">სახელმძღვანელო — მომხმარებლის გზამკვლევი</a>.

**გაფრთხილება სპოილერის შესახებ**: მომხმარებლის გზამკვლევი მოიცავს შემდეგ საკითხებს:

* **პარამეტრების** დეკლარირება სხვა წყაროებიდან, როგორებიცაა: **თავსართები (headers)**, **cookie-ები**, **ფორმის ველები** და **ფაილები**.
* **შემმოწმებლებისათვის (ვალიდატორებისათვის) შეზღუდვების** დაწესება, როგორებიცაა: `maximum_length` ან `regex`.
* ძალიან მძლავრი და მარტივად გამოსაყენებელი **<abbr title="ასევე ცნობილი, როგორც კომპონენტები, რესურსები, პროვაიდერები, სერვისები, injectable-ები">პაკეტების ინექცირების</abbr>** სისტემა.
* უსაფრთხოება და ავთენტიკაცია, მათ შორის **OAuth2**-ის მხარდაჭერა **JWT ტოკენებით** და **HTTP Basic** ავთენტიკაცია.
* მეტად სიღრმისეული (მაგრამ ისეთივე მარტივი) მეთოდოლოგიები **კომპლექსური (მრავალშრიანი) JSON მოდელების** დეკლარირებისათვის (მადლობა Pydantic-ს).
* **GraphQL**-ის ინტეგრირება <a href="https://strawberry.rocks" class="external-link" target="_blank">Strawberry</a>-სთან და სხვა ბიბლიოთეკებთან ერთად.
* არაერთი სხვა ფუნქციონალი (მადლობა Starlette-ს), როგორებიცაა:
    * **ვებსოკეტები**
    * HTTPX-ზე და `pytest`-ზე დაფუძნებული უმარტივესი ტესტები
    * **CORS**
    * **Cookie სესიები**
    * ...და მრავალი სხვა.

## წარმადობა

TechEmpower-ის მიუკერძოებელი ტესტები ცხადყოფენ, რომ Uvicorn-ით გაშვებული **FastAPI**-ზე დაფუძნებული აპლიკაციები <a href="https://www.techempower.com/benchmarks/#section=test&runid=7464e520-0dc2-473d-bd34-dbdfd7e85911&hw=ph&test=query&l=zijzen-7" class="external-link" target="_blank">წარმოაჩენენ FastAPI-ს, როგორც ერთ-ერთ უსწრაფეს ფრეიმვორქს Python-ის არსებულ ფრეიმვორქებს შორის</a>. მას წინ უსწრებენ მხოლოდ Starlette-ი და Uvicorn-ი (რომლებსაც, თავის მხრივ, FastAPI-ი იყენებს). (*)

ამ ყველაფრის უკეთ გასააზრებლად იხილეთ შემდეგი განყოფილება: <a href="https://fastapi.tiangolo.com/benchmarks/" class="internal-link" target="_blank">წარმადობის ტესტები (Benchmarks)</a>.

## პაკეტები

Pydantic-ის მიერ გამოიყენება შემდეგი პაკეტები:

* <a href="https://github.com/JoshData/python-email-validator" target="_blank"><code>email_validator</code></a> — მეილის ვალიდაციისათვის.
* <a href="https://docs.pydantic.dev/latest/usage/pydantic_settings/" target="_blank"><code>pydantic-settings</code></a> — პარამეტრების სამართავად.
* <a href="https://docs.pydantic.dev/latest/usage/types/extra_types/extra_types/" target="_blank"><code>pydantic-extra-types</code></a> — Pydantic-თან ერთად გამოყენებადი დამატებითი ტიპებისათვის.

Starlette-ის მიერ გამოიყენება შემდეგი პაკეტები:

* <a href="https://www.python-httpx.org" target="_blank"><code>httpx</code></a> — სავალდებულოა, თუკი გსურთ, რომ გამოიყენოთ `TestClient`-ი .
* <a href="https://jinja.palletsprojects.com" target="_blank"><code>jinja2</code></a> — სავალდებულოა, თუკი გსურთ, რომ გამოიყენოთ შაბლონის ნაგულისხმევი კონფიგურაცია.
* <a href="https://github.com/Kludex/python-multipart" target="_blank"><code>python-multipart</code></a> — სავალდებულოა, თუკი გსურთ, რომ გქონდეთ ფორმების <abbr title="HTTP მოთხოვნიდან შემომავალი მონაცემების კონვერტირება Python-ისთვის გასაგებ მონაცემებად">„პარსინგის“</abbr> შესაძლებლობა `request.form()`-ის გამოყენებით.

FastAPI / Starlette-ის მიერ გამოიყენება შემდეგი პაკეტები:

* <a href="https://www.uvicorn.org" target="_blank"><code>uvicorn</code></a> — სერვერისთვის, რომელიც ემსახურება თქვენი აპლიკაციის ჩატვირთვას და მუშაობას.
* `fastapi-cli` — უზრუნველყოფს `fastapi` ბრძანების ხელმისაწვდომობას.

`fastapi`-ის ინსტალირებისას, მასთან ერთად ინსტალირდება ზემოთ ჩამოთვლილი სტანდარტული პაკეტებიც.

დამატებითი არასავალდებულო პაკეტები გახლავთ:

* <a href="https://github.com/ijl/orjson" target="_blank"><code>orjson</code></a> — სავალდებულოა, თუკი გსურთ, რომ გამოიყენოთ `ORJSONResponse`-ი.
* <a href="https://github.com/esnme/ultrajson" target="_blank"><code>ujson</code></a> — სავალდებულოა, თუკი გსურთ, რომ გამოიყენოთ `UJSONResponse`-ი.

## `fastapi-slim`

თუ არ გჭირდებათ დამატებითი არასავალდებულო სტანდარტული პაკეტები, `fastapi`-ის ნაცვლად დააინსტალირეთ `fastapi-slim`-ი.

როდესაც ინსტალაციას ახორციელებთ შემდეგი ბრძანებით:

```bash
pip install fastapi
```

...ინსტალირდება იგივე კოდი და პაკეტები, რაც დაინსტალირდებოდა შემდეგი ბრძანების გამოყენების შემთხვევაში:

```bash
pip install "fastapi-slim[standard]"
```

არასავალდებულო სტანდარტულ პაკეტებში იგულისხმება ზემოთ მოხსენიებული პაკეტები.

## ლიცენზია

აღნიშნულ პროექტზე ვრცელდება MIT ლიცენზიით გათვალისწინებული წესები და პირობები.
