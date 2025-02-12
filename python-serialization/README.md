# Python - Serialization

## Description

Le projet "Python - Serialization" explore les concepts de sérialisation et de marshaling dans le but de comprendre comment les données peuvent être transformées et communiquées efficacement entre différentes parties d'un système ou même entre plusieurs systèmes. Ce projet permet d'apprendre à manipuler et à gérer les données dans des formats tels que JSON, XML et pickle, ce qui est essentiel pour les applications nécessitant la persistance des données, le calcul distribué et la communication entre composants logiciels.

### Objectifs d'apprentissage
- Comprendre les différences et similitudes entre marshaling et sérialisation.
- Implémenter la sérialisation dans des tâches pratiques.
- Comprendre comment les données sérialisées peuvent être utilisées dans des applications web, des bases de données et des communications réseau.
- Évaluer les implications de performance des différents formats de sérialisation, tels que JSON, XML et les formats binaires.

### Ressources
- [Real Python Serialization](https://realpython.com/python-serialization/)
- [Real Python: Working With JSON Data in Python](https://realpython.com/python-json/)
- [Python’s pickle documentation](https://docs.python.org/3/library/pickle.html)
- [Corey Schafer on Pickle](https://www.youtube.com/watch?v=2TwKX4X-0Vg)
- [CSV to JSON in Python](https://realpython.com/python-csv/)
- [Python XML ElementTree Guide](https://docs.python.org/3/library/xml.etree.elementtree.html)
- [Socket Programming Guide](https://realpython.com/python-sockets/)

---

## Tâches

### 0. Sérialisation de base
**Objectif** : Créer un module de sérialisation basique qui permet de sérialiser un dictionnaire Python en fichier JSON et de désérialiser ce fichier pour recréer le dictionnaire Python.

- **Fonctions à implémenter** :
  - `serialize_and_save_to_file(data, filename)`: Sérialise un dictionnaire Python et l'enregistre dans un fichier JSON.
  - `load_and_deserialize(filename)`: Charge et désérialise les données JSON à partir d'un fichier pour recréer le dictionnaire Python.

**Exemple d'exécution** :

```python
#!/usr/bin/env python3
from task_00_basic_serialization import load_and_deserialize, serialize_and_save_to_file

data_to_serialize = {
    "name": "John Doe",
    "age": 30,
    "city": "New York"
}

serialize_and_save_to_file(data_to_serialize, 'data.json')
print("Data serialized and saved to 'data.json'.")

deserialized_data = load_and_deserialize('data.json')
print("Deserialized Data:")
print(deserialized_data)
```

### 1. Pickling de classes personnalisées
**Objectif** : Apprendre à sérialiser et désérialiser des objets Python personnalisés en utilisant le module `pickle`.

- **Classe à créer** : `CustomObject`
  - Attributs : `name` (chaîne de caractères), `age` (entier), `is_student` (booléen).
  - Méthodes :
    - `serialize(self, filename)`: Sérialise l'instance actuelle de l'objet dans un fichier avec `pickle`.
    - `deserialize(cls, filename)`: Désérialise un objet à partir d'un fichier `pickle` et le retourne.

**Exemple d'exécution** :

```python
#!/usr/bin/env python3
from task_01_pickle import CustomObject

obj = CustomObject(name="John", age=25, is_student=True)
obj.display()

obj.serialize("object.pkl")

new_obj = CustomObject.deserialize("object.pkl")
new_obj.display()
```

### 2. Conversion de données CSV en format JSON
**Objectif** : Lire des données au format CSV et les convertir en format JSON.

- **Fonction à implémenter** :
  - `convert_csv_to_json(csv_filename)`: Convertit un fichier CSV en un fichier JSON.

**Exemple d'exécution** :

```python
#!/usr/bin/env python3
from task_02_csv import convert_csv_to_json

csv_file = "data.csv"
convert_csv_to_json(csv_file)
print(f"Data from {csv_file} has been converted to data.json")
```

### 3. Sérialisation et désérialisation avec XML
**Objectif** : Utiliser le format XML pour la sérialisation et la désérialisation des données.

- **Fonctions à implémenter** :
  - `serialize_to_xml(dictionary, filename)`: Sérialise un dictionnaire Python en XML.
  - `deserialize_from_xml(filename)`: Désérialise un fichier XML en dictionnaire Python.

**Exemple d'exécution** :

```python
#!/usr/bin/env python3
from task_03_xml import serialize_to_xml, deserialize_from_xml

sample_dict = {'name': 'John', 'age': '28', 'city': 'New York'}

serialize_to_xml(sample_dict, "data.xml")
deserialized_data = deserialize_from_xml("data.xml")

print(deserialized_data)
```

---

## Structure du dépôt
```
holbertonschool-higher_level_programming/
└── python-serialization/
    ├── task_00_basic_serialization.py
    ├── task_01_pickle.py
    ├── task_02_csv.py
    └── task_03_xml.py
```

---

## Commentaires

- Les fichiers doivent respecter le style PEP8.
- Veuillez vérifier la présence d'une nouvelle ligne à la fin de chaque fichier.
- Les tests doivent être réalisés et les résultats documentés.
- Les exceptions doivent être gérées, en particulier pour les fichiers non existants ou malformés.

---

**Dépôt GitHub :** [holbertonschool-higher_level_programming](https://github.com/holbertonschool-higher_level_programming/python-serialization)

---

## Auteurs

Kevin De Castro : Étudiant à la Holberton School

## License

Ce projet est sous la licence MIT.
