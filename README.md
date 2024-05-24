# summarization-dataset
Multimodal summarization dataset for Russian

## Structure
At the moment, the dataset contains 480 papers from 8 scientific domains: linguistics, history, law, medicine, journalism, computer science, economics, chemistry.

Each paper in the dataset occupies one folder, which contains the following files:

* `name.txt` - name of the paper
* `abstract.txt` - its abstract
* `text.txt` - its full text
* `image_number.png` - figures
* `table_number.png` - tables 
* `figures.json` - descriptions of figures
* `tables.json` - descriptions of tables

## Statistics

|   **Domain**  | **Length (chars)** | **Length (tokens)** | **Figures** | **Tables** |
|:-------------:|:------------------:|:-------------------:|:-----------:|:----------:|
| _Economics_   |      1 316 995     |       151 284       |      32     |     25     |
| _Chemistry_   |       938 743      |       109 859       |     159     |   **150**  |
| _History_     |      1 540 251     |       184 407       |      2      |     17     |
| _IT_          |      1 002 115     |       114 721       |   **238**   |     27     |
| _Journalism_  |      1 377 087     |       174 064       |      45     |     12     |
| _Law_         |      1 243 153     |       143 675       |      0      |      2     |
| _Linguistics_ |    **1 557 481**   |     **190 478**     |      1      |      1     |
| _Medicine_    |       963 178      |       107 449       |      19     |     45     |
| Total         |      9 939 003     |      1 175 937      |     496     |     279    |

## Citation

In Progress...

