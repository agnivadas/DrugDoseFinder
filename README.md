# **DrugDoseFinder**  
[![GPL License](https://img.shields.io/badge/license-GNU-violet.svg)](https://www.gnu.org/licenses/gpl-3.0.en.html) [![DrugDoseFinder](https://img.shields.io/badge/source-GitHub-303030.svg?style=flat-square)](https://github.com/agnivadas/DrugDoseFinder) ![Maintenance](https://img.shields.io/maintenance/yes/2024) ![Static Badge](https://img.shields.io/badge/contributions-welcome-blue)

**An RDF-based tool to search and retrieve drug doses from a personalized knowledge graph.**




## 📋 **Description**  
`DrugDoseFinder` is a command-line Python application that allows users to search for drug names in an RDF graph and retrieve the associated dosage information. The tool leverages fuzzy string matching to suggest the best matches for user input, making it robust to minor typos or variations in drug names.

This project integrates:

RDF-based data storage using RDFLib
Fuzzy matching via FuzzyWuzzy
Structured querying to fetch drug details and dosage.
This tool is ideal for healthcare professionals and developers managing RDF-based medical datasets.

---

## 🚀 **Features**  
- **Multiple RDF File Support:** Load and combine data from multiple RDF files
- **Fuzzy Drug Name Search:** Automatically suggests the best matches for queried drug names.  
- **Dose Information Retrieval:** Fetch dosage details (rdf:hasDose) for the matched drug.
- **User-Friendly Interface:** Select from suggested results interactively.
- **Extensible RDF Integration:** Easily connect with custom RDF files containing drug data.
  

---

## 🛠️ **Technologies Used**  
- **Python 3**  
- **RDFLib:** Library for parsing and querying RDF graphs.  
- **FuzzyWuzzy:** For fuzzy string matching.


---


## ⚙️ **Requirements:**

1.Ensure you have the following dependencies installed:

- Python 3.7 or later
- Rdflib & fuzzywuzzy

```bash
pip install rdflib fuzzywuzzy python-Levenshtein
```
2. Download or clone this project.

---
## ▶️ **Usage:**

1. **Run the script with:**
```bash
python search_dose.py

```
or open the `search_dose.py` file directly.

2. **Input Drug Name:**
Enter the name of the drug you want to search. For example:
```bash
Enter the drug name to search: Atropine
```
3. **Select from Suggested Matches**
If matches are found based on fuzzy search, you'll see a list like:
```
Matches (choose the drug from below and enter number of it):


1. atropine
2. Atropine PO
3. hydrocodone/homatropine
4. difenoxin/atropine
5. atropine/pralidoxime
6. diphenoxylate/atropine
7. atropine IV/IM
```
Choose the correct option by entering its number.

4. **View Dose Information**
The tool fetches the RDF triple for dosage (rdf:hasDose):

5. **No Matches**
If no relevant matches are found, the system prompts you to raise an issue for updating the RDF data.

---
## ⚙️ **How It Works:**

1 **Load RDF Files**
- The script loads all specified RDF files(database1.rdf,database2.rdf) into an RDFLib graph.
2. **Extract Drug Names**
- The drug names are extracted using the predicate `hasName`.

3. **Fuzzy Search**

- FuzzyWuzzy compares user input to available drug names and ranks matches.

4. **User Selection**

-Users can select from suggested matches based on confidence scores.

5. **Dose Retrieval**

The RDF graph is queried for the corresponding `hasDose` triple and the dosage is displayed.

---


## 🔗 **License**

This project is licensed under the [GNU](https://choosealicense.com/licenses/agpl-3.0/) License.

---


## 🤝 **Contributing**

Contributions are welcome!

- Fork the repository
- Submit a pull request with improvements
- Any suggestion for modification of database is welcome

---

**Enjoy accurate drug name searches and precise dosage lookups! 🚀**

